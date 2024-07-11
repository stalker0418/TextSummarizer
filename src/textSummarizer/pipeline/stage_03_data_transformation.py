
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_transformation import DataTransformation

class dataTransformationTrainingPipeline:
    def __init__(self):
        pass
    

    def transform_data(self):
        configManager = ConfigurationManager()
        data_transformation_config = configManager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()