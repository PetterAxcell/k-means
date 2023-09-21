import os
import pandas as pd
from src.preprocessing.infrastructure.get_data import GetData
FILENAME = str(os.getenv('FILENAME'))
KIND_FILE = str(os.getenv('KIND_FILE'))
DATAFRAME = pd.core.frame.DataFrame
class Preprocessing():
    def __init__(self) -> None:
        self.data: DATAFRAME = GetData(FILENAME).read_data(KIND_FILE)
    