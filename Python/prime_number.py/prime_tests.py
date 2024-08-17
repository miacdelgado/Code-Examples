import unittest

from is_prime import is_prime
  
class Test_Config(unittest.TestCase):
    def test_question_c_test_1(self):
        self.assertEqual(False, is_prime(4))
    def test_question_c_test_2(self):
        self.assertEqual(True, is_prime(5))
    def test_question_c_test_3(self):
        self.assertEqual(True, is_prime(11))