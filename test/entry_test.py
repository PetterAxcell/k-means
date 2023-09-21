'''
 This file implies the number of tests that the code has to do.
'''
import os
from test.preprocessing.infrastructure.data_tests import DataTests
class EntryTest():
    def __init__(self) -> None:
        self.number_test: int = 0
        self.number_fails: int = 0
        self.class_data_test: DataTests = DataTests()

    def test_all(self):
        '''
            This function calls all tests: preprocessing, models...
            Args:
                None
            Returns:
                array[2]: integers
        '''
        if bool(int(os.getenv('PREPROCESSING_TEST'))):
            result_preprocessing_test = self.class_data_test.test_all()
            [self.number_test, self.number_fails] += result_preprocessing_test
        
        return [self.number_test, self.number_fails]

    def get_results(self):
        '''
            This function returns the current values
            Args:
                None
            Returns:
                array[2]: integers
        '''
        return [self.number_test, self.number_fails]