import pandas as pd
import os
import unittest
from src.preprocessing.infrastructure.get_data import GetData
class TestCsv(unittest.TestCase):
    def __init__(self) -> None:
        self.GetDataFunction = GetData(os.getenv('FILENAME'))
        self.total_errors = 0
    
    def make_test(self):
        self.readable()
        return self.total_errors

    def test_readable(self): 
        self.GetDataFunction.read_data('csv')
        print('test_csv->test_readable')
        with self.assertRaises(TypeError):
            print('here')
            
if __name__ == '__main__':
    unittest.main()