from extractive_qna.config.configuration import ConfigurationManager
from extractive_qna.components.data_transformation import DataTransformation
from extractive_qna.logging import logger


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()