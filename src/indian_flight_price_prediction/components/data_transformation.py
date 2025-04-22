import os
from src.indian_flight_price_prediction.logger import logger
from src.indian_flight_price_prediction.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # split the data into training and test set (0.75, 0.25)
        train, test = train_test_split(data, train_size= 0.75)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index = False)

        logger.info("Splited data into training and test split")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)