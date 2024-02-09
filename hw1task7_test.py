import Task_7
import unittest
from io import StringIO
from unittest.mock import patch
from random import choice

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["3", "4"])
    def test_main_input_calls(self, mock_input):
        Task_7.main() 
        expected_calls = ["Length: ", "Number of sides: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', side_effect=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_7.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = [[11, 14, '1835.66542'], [9, 10, '618.18242'], [3, 19, '156.31759'], [3, 18, '140.29612'], [9, 6, '222.54567'], [3, 15, '97.42786'], [5, 11, '208.17777'], [8, 3, '43.45584'], [11, 16, '2397.60382'], [3, 18, '140.29612'], [6, 17, '750.84403'], [5, 18, '557.43468'], [10, 10, '769.42088'], [10, 17, '2223.62636'], [4, 16, '256.00000'], [7, 6, '130.82085'], [8, 17, '1395.41544'], [8, 11, '584.23968'], [10, 7, '377.01623'], [8, 10, '482.84271'], [9, 5, '154.54560'], [8, 7, '236.59293'], [2, 20, '0.00000'], [4, 17, '289.00000'], [8, 4, '77.25483']]
        sample = choice(list(data))
        expected_output = f"Area: {float(sample[2]):.5f}\n"
        self._test_with_input(sample[:2], expected_output)

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a", "b"]), \
             self.assertRaises(ValueError):
            Task_7.main()
