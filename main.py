from src.chicken_disease_classification import logger
from src.chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.chicken_disease_classification.pipeline.stage_02_base_model_preperation import PrepareBaseModelTrainingPipeline
from src.chicken_disease_classification.pipeline.stage_03_prepare_callbacks import PrepareCallbacksTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:  
    logger.error(f"Error occurred in {STAGE_NAME} stage: {e}")
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME} stage: {e}")
    raise e

STAGE_NAME = "Prepare Callbacks"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_callbacks = PrepareCallbacksTrainingPipeline()
    prepare_callbacks.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME} stage: {e}")
    raise e
