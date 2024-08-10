from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering
import tensorflow as tf
# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('model/tokenizer_squad')
model = TFAutoModelForQuestionAnswering.from_pretrained('model/finetuned_squad')

# Prepare your inputs
c="The Amazon Rainforest, often referred to as the lungs of earth, spans over 5.5 million square kilometers in South America. It is home to an incredibly diverse array of flora and fauna, including more than 400 billion individual trees representing 16,000 species. The rainforest plays a critical role in regulating the global climate by absorbing vast amounts of carbon dioxide. It also supports indigenous communities who have lived there for thousands of years, relying on the forest for food, shelter, and medicine. However, deforestation poses a significant threat to this vital ecosystem, driven primarily by logging, agriculture, and mining activities. Conservation efforts are underway to protect the Amazon, but challenges remain due to economic pressures and illegal activities."
inputs = tokenizer("How many individual trees are in the Amazon Rainforest?", c, return_tensors='tf')

# Get predictions
outputs = model(inputs)
start_logits = outputs.start_logits
end_logits = outputs.end_logits

# Decode the predictions
start_index = tf.argmax(start_logits, axis=-1).numpy()[0]
end_index = tf.argmax(end_logits, axis=-1).numpy()[0]
answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_index:end_index+1]))

print("Answer:", answer)
