import os
from extractive_qna.constants import *
from extractive_qna.entity import DataTransformationConfig
from extractive_qna.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
import pandas as pd
import operator

class DataTransformation:
    
    def __init__(self , config: DataTransformationConfig,max_length=400,stride=100):
        self.config = config
        self.tokenizer=AutoTokenizer.from_pretrained(MODEL_NAME)
        self.max_length=max_length
        self.stride=stride
        
    # Utility function to find the *last* occurrence of a sequence.
    def rindex(self,lst, value):
        import operator
        x = len(lst) - operator.indexOf(reversed(lst), value) - 1
        return x
    
    def prepare_dataset(self,examples):
        # Some tokenizers don't strip spaces. If there happens to be question text
        # with excessive spaces, the context may not get encoded at all.
        examples["question"] = [q.lstrip() for q in examples["question"]]
        examples["context"] = [c.lstrip() for c in examples["context"]]

        # Tokenize.
        tokenized_examples = self.tokenizer(
            examples['question'],
            examples['context'],
            truncation="only_second",
            max_length = self.max_length,
            stride=self.stride,
            return_overflowing_tokens=True,
            return_offsets_mapping=True,
            padding="max_length"
        )

        # We'll collect a list of starting positions and ending positions.
        tokenized_examples['start_positions'] = []
        tokenized_examples['end_positions'] = []

        # Work through every sequence.
        for seq_idx in range(len(tokenized_examples['input_ids'])):
            seq_ids = tokenized_examples.sequence_ids(seq_idx)
            offset_mappings = tokenized_examples['offset_mapping'][seq_idx]

            cur_example_idx = tokenized_examples['overflow_to_sample_mapping'][seq_idx]
            answer = examples['answers'][cur_example_idx]
            answer_text = answer['text'][0]
            answer_start = answer['answer_start'][0]
            answer_end = answer_start + len(answer_text)

            context_pos_start = seq_ids.index(1)
            context_pos_end = self.rindex(seq_ids, 1)

            s = e = 0
            if (offset_mappings[context_pos_start][0] <= answer_start and
                offset_mappings[context_pos_end][1] >= answer_end):
                i = context_pos_start
                while offset_mappings[i][0] < answer_start:
                    i += 1
                if offset_mappings[i][0] == answer_start:
                    s = i
                else:
                    s = i - 1

                j = context_pos_end
                while offset_mappings[j][1] > answer_end:
                    j -= 1
                if offset_mappings[j][1] == answer_end:
                    e = j
                else:
                    e = j + 1

            tokenized_examples['start_positions'].append(s)
            tokenized_examples['end_positions'].append(e)

        return tokenized_examples
    
    def convert(self):
        dataset_squad=load_from_disk(self.config.data_path)
        dataset_squad_tf=dataset_squad.map(self.prepare_dataset,batched=True,remove_columns=dataset_squad["train"].column_names,num_proc=1)
        dataset_squad_tf=dataset_squad_tf.remove_columns(["offset_mapping","overflow_to_sample_mapping"])
        dataset_squad_tf.save_to_disk(os.path.join(self.config.root_dir,"squad_dataset"))


