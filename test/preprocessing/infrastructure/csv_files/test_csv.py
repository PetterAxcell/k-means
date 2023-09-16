import pandas as pd
import os
from src.preprocessing.infrastructure.get_data import GetData
from test.preprocessing.infrastructure.data_tests import DataTests
class TestCsv(DataTests):
    def __init__(self) -> None:
        super().__init__()
        self.GetDataFunctionRight = GetData(os.getenv('FILENAME'))
        self.GetDataFunctionWrong = GetData('error_file.csv')
        self.typeof_expect_variable = str(pd.core.frame.DataFrame)
        self.total_errors = 0
    
    def make_test(self):
        self.test_readable()
        return self.total_errors

    def test_readable(self): 
        typeof_variable = str(type(self.GetDataFunctionRight.read_data('csv')))
        self.assertEqual(typeof_variable, self.typeof_expect_variable)
        # self.GetDataFunctionWrong.read_data('csv')
        # print('test_csv->test_readable')
        # with self.assertRaises(TypeError):
        #     print('here')
