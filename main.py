# from textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

from src.textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import dataValidationTrainingPipeline

def data_ingestion():
    pipleline_Stage_name = "Data Ingestion Stage"

    try:
        logger.info(f"Starting {pipleline_Stage_name}")
        data_ingestion = dataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"{pipleline_Stage_name} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e

def data_validation():
    try:
        pipeline_stage_name = "Data Validation Stage"
        logger.info(f"Starting {pipeline_stage_name}")
        data_validation = dataValidationTrainingPipeline()
        data_validation.validate_all_files_exist()
        logger.info(f"{pipeline_stage_name} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e

data_validation()

