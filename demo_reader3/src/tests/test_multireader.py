#tests/test_multireader.py

import unittest
import demo_reader.test_multireader

class TestMultireader(unittest.TestCase):
    def test_initialization(self):
        demo_reader.test_multireader.MultiReader('test_file.txt')