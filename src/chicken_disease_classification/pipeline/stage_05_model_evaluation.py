from src.chicken_disease_classification.components.evaluation import Evaluation
from src.chicken_disease_classification.config.configuration import configManager
from src.chicken_disease_classification import logger
STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = configManager()
            model_evaluation_config = config.get_model_evaluation_config()
            evaluation = Evaluation(config=model_evaluation_config)
            evaluation.evaluate()
            evaluation.save_score()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e