import os
from test.preprocessing.infrastructure.csv_files.test_csv import TestCsv
class DataTests():
    def __init__(self):
        self.check_csv = bool(int(os.getenv('CSV_FILE')))
        self.test_csv_functions = TestCsv()

    def check_data(self):
        if self.check_csv:
            total = self.test_csv_functions.make_test()
        return total
    