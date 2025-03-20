import os 
import zipfile
import urllib.request as request
from src.chicken_disease_classification.utils.common import get_size
from src.chicken_disease_classification import logger
from src.chicken_disease_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
                logger.info(f"{filename} downloaded! with the following info: {headers}")
            except Exception as e:
                logger.error(f"Error occurred while downloading the file: {e}")
                raise e  # Raise the exception to stop execution
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        
        # Verify the file exists and has content
        if not os.path.exists(self.config.local_data_file) or os.path.getsize(self.config.local_data_file) == 0:
            raise FileNotFoundError(f"Failed to download file to {self.config.local_data_file}")
            
    def extract_zip_file(self):
        # Check if file exists before trying to extract
        if not os.path.exists(self.config.local_data_file):
            raise FileNotFoundError(f"Zip file not found at {self.config.local_data_file}")
            
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"File extracted successfully to {unzip_path}")
        except zipfile.BadZipFile:
            logger.error(f"File is not a valid zip file: {self.config.local_data_file}")
            raise