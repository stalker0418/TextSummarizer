from src.textSummarizer.conponents.data_validation import DataValidation
from src.textSummarizer.config.configuration import ConfigurationManager


class dataValidationTrainingPipeline:
    def __init__(self):
        pass

    def validate_all_files_exist(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()