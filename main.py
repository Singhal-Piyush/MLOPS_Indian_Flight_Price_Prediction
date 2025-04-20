from src.indian_flight_price_prediction.logger import logger
from src.indian_flight_price_prediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed >>>>>>>>\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


logger.info("Logging test")