from mlproject.config.configuraion import ConfigurationManger
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManger()
        model_evaluation_config = config.get_evaluation_config()
        model_trainer_config = ModelEvaluation(config=model_evaluation_config)
        model_trainer_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
    except Exception as e:
        logger.exception(e)
        raise e