from src.chicken_disease_classification.components.prepare_callback import PrepareCallback
from src.chicken_disease_classification.config.configuration import configManager
from src.chicken_disease_classification import logger

STAGE_NAME = "Prepare Callbacks"

class PrepareCallbacksTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = configManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callback = PrepareCallback(config=prepare_callbacks_config)
            callbacks = prepare_callback.get_tb_ckpt_callbacks()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = PrepareCallbacksTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<") 
    except Exception as e:
        logger.exception(e)
        raise e