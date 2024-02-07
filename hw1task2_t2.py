import Task_2
import unittest
from io import StringIO
from unittest.mock import patch

class TestMainFunction(unittest.TestCase):
    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_2.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_input_150(self):
        self._test_with_input('150', "150 deqiqe =  2 saat 30 deqiqedir\n")

    def test_input_62(self):
        self._test_with_input('62', "62 deqiqe =  1 saat 2 deqiqedir\n")

    def test_invalid_input(self):
        with patch('builtins.input', return_value='abc'), \
             self.assertRaises(ValueError):
            Task_2.main()

if __name__ == '__main__':
    unittest.main()
