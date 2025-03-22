from src.chicken_disease_classification.config.configuration import configManager
from src.chicken_disease_classification.components.training import Training
from src.chicken_disease_classification.components.prepare_callbacks import PrepareCallback
from src.chicken_disease_classification.entity.config_entity import trainingconfig
from src.chicken_disease_classification import logger


STAGE_NAME = "Training"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = configManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list=callback_list)
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<") 
    except Exception as e:
        raise e 
    