import os
import urllib.request as request
import zipfile
from src.indian_flight_price_prediction.logger import logger
from src.indian_flight_price_prediction.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config
    
    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

            logger.info(f"{filename} downloading with following info :\n {headers}!!")
        else:
            logger.info(f"Dataset file already exists locally.")

    # extract zip file
    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        zip_file_path = self.config.local_data_file
        # if not zip_file_path.endswith(".zip"):
        #     zip_file_path += ".zip"

        with zipfile.ZipFile(zip_file_path, 'r' ) as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Data extracted to {unzip_path}")