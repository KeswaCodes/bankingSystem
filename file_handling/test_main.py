import unittest
from unittest.mock import patch 
from unittest import TestCase
from validate import *

class TestValidation(TestCase):

    @patch('validate.validInput', return_value = False)
    def testInvalidNameFormat(self, mock_patch):
            with self.subTest('Testing incorrect name/surname format'):
                self.assertFalse(validInput(["Zinhle Keswa"], "name"))
                self.assertFalse(validInput(["Zin123"], "name"))
                self.assertFalse(validInput(["$"], "username")) # testing that special characters are not accepted

            with self.subTest("Testing for invalid username provided"):
                self.assertFalse(validInput(["zinksw"], "username"))

if __name__ == "__main__":
    unittest.main()