from mlproject.config.configuraion import ConfigurationManger
from mlproject.components.data_validation_02  import DataValidation
from mlproject import logger


STAGE_NAME = "Data Validation Stage"

class DataValidtationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManger()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
        obj = DataValidtationTrainingPipeline()
        obj.main()
        logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
    except Exception as e:
        logger.exception(e)
        raise e