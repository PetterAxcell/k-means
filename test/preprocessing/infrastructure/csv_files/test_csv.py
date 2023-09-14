import pandas as pd
import os
import unittest
from src.preprocessing.infrastructure.get_data import GetData
class TestCsv():
    def __init__(self) -> None:
        self.GetDataFunction = GetData(os.getenv('FILENAME'))
        self.total_errors = 0
    
    def make_test(self):
        self.readable()
        return self.total_errors


    def readable(self):
        try: 
            self.GetDataFunction.read_data('csv')
        except:
            self.total_errors += 1
