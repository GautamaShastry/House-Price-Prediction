from mlProject.config.configuration import ConfigManager
from mlProject.components.data import DataIngestion
from mlProject import logger

STAGE_NAME  = "Data Ingestion Stage"

class DataTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()
        data_config = config.get_data_config()
        data_ingestion = DataIngestion(config=data_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e