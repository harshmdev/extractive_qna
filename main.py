from extractive_qna.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from extractive_qna.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from extractive_qna.pipeline.stage_03_data_transformation import DataTransformationPipeline
from extractive_qna.logging import logger


STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation Stage"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<\n\nx===x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation Stage"

try:
    logger.info(f"started>>>{STAGE_NAME}<<<started")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"Completed>>{STAGE_NAME}<<<Completed")
except Exception as e:
    logger.exception(e)
    raise e