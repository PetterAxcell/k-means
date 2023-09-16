'''
    Index file.

    This project develop a k-means algorithm which can read, preprocessing 
    and calculates the k-means

    This file contains the following functions:
        * main - Entrypoint of the project
'''
import os
import unittest
from test.entry_test import EntryTest
from src.preprocessing.infrastructure.get_data import GetData

TEST_FLAG = bool(int(os.getenv('TEST')))
def main():
    '''
        Entrypoint
    '''
    if TEST_FLAG:
        print('here')
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(EntryTest)
        print(suite)
        unittest.TextTestRunner().run(suite)
        #test_result = EntryTest().get_results()
    else:
        print(GetData(os.getenv('FILENAME')).read_data('csv'))

if __name__ == "__main__":
    main()
