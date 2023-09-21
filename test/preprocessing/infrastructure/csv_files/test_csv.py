import os
import pandas as pd
from src.preprocessing.infrastructure.get_data import GetData
class TestCsv():
    def __init__(self) -> None:
        self.GetDataFunctionRight = GetData(os.getenv('FILENAME'))
        self.GetDataFunctionWrong = GetData('error_file.csv')
        self.typeof_expect_variable: str = str(pd.core.frame.DataFrame)
        self.total_errors: int = 0
        self.total_test: int = 0
    
    def test_all(self):
        '''
            It calls all the test functions.
            Args:
                None
            Return:
                Array[2] : Integers
        '''
        self.test_readable()

        return [self.total_test, self.total_errors]

    def test_readable(self): 
        '''
            It checks if it is importing pandas dataframes.
            Params:
                None
            Return:
                array[2]: integers
        '''
        self.total_test += 1
        typeof_variable = str(type(self.GetDataFunctionRight.read_data('csv')))
        if typeof_variable != self.typeof_expect_variable: self.total_errors += 1