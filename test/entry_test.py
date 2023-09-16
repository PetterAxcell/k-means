'''
 This file implies the number of tests that the code has to do.
'''
import unittest
class EntryTest(unittest.TestCase):
    def test_make(self):
        print('here2')
        self.assertEqual(0, 1)

if __name__ == "__main__":
    unittest.main()
