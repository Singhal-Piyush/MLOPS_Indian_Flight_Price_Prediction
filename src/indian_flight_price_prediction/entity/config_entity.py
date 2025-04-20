from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    # kaggle_dataset : str
    local_data_file : Path
    unzip_dir : Path