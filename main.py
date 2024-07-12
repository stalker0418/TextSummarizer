# from textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

from src.textSummarizer.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import dataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import dataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import modelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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
    
def data_transformation():
    try:
        pipeline_stage_name = "Data Transformation Stage"
        logger.info(f"Starting {pipeline_stage_name}")
        data_transformation = dataTransformationTrainingPipeline()
        data_transformation.transform_data()
        logger.info(f"{pipeline_stage_name} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e
    
def model_train():
    try:
        pipeline_stage_name = "Model Training Stage"
        logger.info(f"Starting {pipeline_stage_name}")
        model_trainer = modelTrainerTrainingPipeline()
        model_trainer.train_model()
        logger.info(f"{pipeline_stage_name} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e

def model_evaluation():
    try:
        pipeline_stage_name = "Model Evaluation Stage"
        logger.info(f"Starting {pipeline_stage_name}")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.evaluate_model()
        logger.info(f"{pipeline_stage_name} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e


model_evaluation()

