from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def evaluate_model(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise e