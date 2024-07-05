from mlProject import logger
from mlProject.pipeline.stage_01 import DataTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>> starting {STAGE_NAME} <<<<<<")
    data = DataTrainingPipeline()
    data.main()
    logger.info(f"<<<<<<  {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e