import os
from test.entry_test import EntryTest
from test.preprocessing.infrastructure.csv_files.test_csv import TestCsv
class DataTests(EntryTest):
    def __init__(self):
        super().__init__()
        self.check_csv = bool(int(os.getenv('CSV_FILE')))
        self.test_csv_functions = TestCsv()

    def check_data(self):
        if self.check_csv:
            total = self.test_csv_functions.make_test()
        return total
