from mlProject import logger
from mlProject.pipeline.stage_01 import DataTrainingPipeline
from mlProject.pipeline.stage_02 import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03 import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>> starting {STAGE_NAME} <<<<<<")
    data = DataTrainingPipeline()
    data.main()
    logger.info(f"<<<<<<  {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> starting {STAGE_NAME} <<<<<<")
    data = DataValidationTrainingPipeline()
    data.main()
    logger.info(f"<<<<<<  {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> starting {STAGE_NAME} <<<<<<")
    data = DataTransformationPipeline()
    data.main()
    logger.info(f"<<<<<<  {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    