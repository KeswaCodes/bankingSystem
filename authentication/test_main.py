import unittest
from unittest.mock import patch
from unittest import TestCase
from authenticate import *

class TestAuthentication(TestCase):

    def testUserExists(self):
        with patch('authenticate.userExists') as mock:
            mock.return_value = False
            username = "zinksw092"
            self.assertFalse(userExists(username))

        pass
    pass