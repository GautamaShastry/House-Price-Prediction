import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def clean_data(self, data):
        # Perform data cleaning operations here
        cleaned_data = data.dropna(subset=['total_bedrooms'])
        return cleaned_data

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        # data cleaning(drop all rows with missing values)
        cleaned_data = self.clean_data(data)
        
        # split the data into training and testing sets, (0.9,0.1) splits.
        train, test = train_test_split(cleaned_data, test_size=0.1)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("splitted data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        