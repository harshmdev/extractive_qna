from extractive_qna.config.configuration import ConfigurationManager
from extractive_qna.components.data_validation import DataValidation
from extractive_qna.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
