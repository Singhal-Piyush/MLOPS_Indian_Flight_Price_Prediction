from src.indian_flight_price_prediction.logger import logger
from src.indian_flight_price_prediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.indian_flight_price_prediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.indian_flight_price_prediction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed >>>>>>>>\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed >>>>>>>>\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_tranformation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed >>>>>>>>\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

