import os
from test.preprocessing.infrastructure.csv_files.test_csv import TestCsv
class DataTests():
    def __init__(self) -> None:
        self.check_csv = bool(int(os.getenv('CSV_FILE')))
        self.class_test_csv = TestCsv()
        self.number_test : int = 0                    
        self.number_fails : int = 0            
    def test_all(self):
        '''
            This function calls all kind of data test: csv, xlsx
            Args:
                None
            Returns:
                array[2]: integers
        '''
        if self.check_csv:
            result_csv_test = self.class_test_csv.test_all()
            self.number_test += result_csv_test[0]
            self.number_fails += result_csv_test[1]
        return [self.number_test, self.number_fails]
