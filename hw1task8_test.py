import Task_8
import unittest
from unittest.mock import patch
from io import StringIO
from random import choice


class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["50"])
    def test_main_input_calls(self, mock_input):
        Task_8.main()
        expected_calls = ["Temperature (C): "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_8.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = {-162: '-259.60', -289: '-488.20', 152: '305.60', -17: '1.40', -36: '-32.80', 125: '257.00', 201: '393.80', 192: '377.60', -47: '-52.60', -269: '-452.20', -135: '-211.00', 263: '505.40', -95: '-139.00', -187: '-304.60', -223: '-369.40', -298: '-504.40', -155: '-247.00', 117: '242.60', 116: '240.80', -93: '-135.40', -66: '-86.80', 95: '203.00', 288: '550.40', 296: '564.80', 147: '296.60', -229: '-380.20', 52: '125.60', -16: '3.20', 18: '64.40', -24: '-11.20', 4: '39.20', -282: '-475.60', -262: '-439.60', -86: '-122.80', 115: '239.00', 239: '462.20', 42: '107.60', -67: '-88.60', 272: '521.60', 187: '368.60', -237: '-394.60', 55: '131.00', -26: '-14.80', -126: '-194.80', -53: '-63.40', -100: '-148.00', 190: '374.00', -215: '-355.00', 168: '334.40', -201: '-329.80'}
        key, value = choice(list(data.items()))
        self._test_with_input(f'{key}', f"{key} Celcius = {float(value):.2f} Fahrenheit\n")

    def test_invalid_input(self):
        with patch('builtins.input', return_value='abc'), \
             self.assertRaises(ValueError):
            Task_8.main()
