import os
import pandas as pd
from datetime import datetime
from src.indian_flight_price_prediction.logger import logger
from src.indian_flight_price_prediction.entity.config_entity import (DataValidationConfig,)


class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config


    def validate_all_columns(self) ->bool:
        try:
            all_schema = self.config.all_schema.keys()
            column_validation_status = []

            with open(self.config.STATUS_FILE, 'a') as f:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\n{'='*27}\n")
                f.write(f"Validation Timestamp: {current_time}\n")
                f.write(f"{'='*27}\n")
                for file_path in self.config.unzip_data_files:
                    data = pd.read_csv(file_path)
                    all_cols = list(data.columns)
                    f.write(f"\n{'='*27}\n")
                    f.write(f"Validation Report: {file_path.name}\n")
                    f.write(f"{'='*27}\n")
                    for col in all_cols:
                        if col not in all_schema:
                            is_valid = False
                            f.write(f"Column {col} not found in schema.Validation Status : {is_valid}.\n")
                        else:
                            if data[col].dtype == self.config.all_schema[col]:
                                is_valid = True
                                expected_dtype = str(self.config.all_schema[col])
                                actual_dtype = str(data[col].dtype)
                                f.write(f"Column: {col:<13} | Expected: {expected_dtype:<7} | Found: {actual_dtype:<7} | Match \n")
                            else:
                                is_valid = False
                                f.write(f"Column: {col:<13} | Expected: {expected_dtype:<7} | Found: {actual_dtype:<7} | Mis-match \n")
                        column_validation_status.append(is_valid)
                
                validation_status = all(column_validation_status)
                f.write(f"\n{'-'*40}\n")
                f.write(f"Validation Status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e