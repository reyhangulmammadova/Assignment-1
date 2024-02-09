import Task_6
import unittest
from io import StringIO
from unittest.mock import patch
from random import choice

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["3"])
    def test_main_input_calls(self, mock_input):
        Task_6.main() 
        expected_calls = ["Enter a number: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_6.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = {458: 105111.0, 105: 5565.0, 398: 79401.0, 195: 19110.0, 218: 23871.0, 445: 99235.0, 257: 33153.0, 493: 121771.0, 332: 55278.0, 326: 53301.0, 86: 3741.0, 45: 1035.0, 199: 19900.0, 62: 1953.0, 423: 89676.0, 272: 37128.0, 219: 24090.0, 197: 19503.0, 456: 104196.0, 388: 75466.0, 444: 98790.0, 205: 21115.0, 131: 8646.0, 34: 595.0, 61: 1891.0}
        key, val = choice(list(data.items()))
        expected_output = f"Result: {val}\n" 
        self._test_with_input(key, expected_output)

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a"]), \
             self.assertRaises(ValueError):
            Task_6.main()
