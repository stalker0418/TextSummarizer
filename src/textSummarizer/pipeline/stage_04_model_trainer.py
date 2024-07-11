from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.model_trainer import ModelTrainer

class modelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def train_model(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        trainer = ModelTrainer(config = model_training_config)
        trainer.train()
