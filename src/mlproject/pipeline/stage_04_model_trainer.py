from mlproject.config.configuraion import ConfigurationManger
from mlproject.components.modeL_trainer_04 import ModelTrainer
from mlproject import logger


STAGE_NAME = "Model Trainer Stage"



class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == '__main__':
    try:
        logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
    except Exception as e:
        logger.exception(e)
        raise e