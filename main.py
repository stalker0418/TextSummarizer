# from textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

from src.textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline

pipleline_Stage_name = "Data Ingestion Stage"

try:
    logger.info(f"Starting {pipleline_Stage_name}")
    data_ingestion = dataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{pipleline_Stage_name} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e
