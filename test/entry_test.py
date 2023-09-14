'''
 This file implies the number of tests that the code has to do.
'''
import os
from test.preprocessing.infrastructure.data_tests import DataTests 
class EntryTest():
    def __init__(self):
        self.preprocessing_flag = os.getenv('PREPROCESSING_TEST')
        self.data_tests = DataTests()
        self.errors = 0
    
    def make_tests(self):
        self.errors = self.data_tests.check_data()

    def get_results(self):
        self.make_tests()
        return self.errors