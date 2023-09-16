'''
 This file implies the number of tests that the code has to do.
'''
import unittest
class EntryTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
    
    def test_make(self):
        self.assertEqual(0, 1)
    