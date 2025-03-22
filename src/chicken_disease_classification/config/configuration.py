from src.chicken_disease_classification.constants import *
from src.chicken_disease_classification.utils.common import read_yaml, create_directories
from src.chicken_disease_classification.entity.config_entity import DataIngestionConfig
from src.chicken_disease_classification.entity.config_entity import PrepareBaseModelConfig
from src.chicken_disease_classification import logger
from src.chicken_disease_classification.utils.common import read_yaml, create_directories
from src.chicken_disease_classification.constants import *
from src.chicken_disease_classification.entity.config_entity import PrepareCallbacksConfig
import os

class configManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params.prepare_base_model
        print("we have created the folder")
        
        create_directories([config.root_dir])
        logger.info(f"created the folder {config.root_dir}")

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=params.IMAGE_SIZE,    
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES,
            params_learning_rate=params.LEARNING_RATE,
            params_include_top=params.INCLUDE_TOP,
        )
        return prepare_base_model_config
    
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([model_ckpt_dir, config.tensorboard_root_log_dir])
        
        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config
        
    