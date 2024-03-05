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
        data = [[5, 6, '64.95191'], [6, 6, '93.53074'], [6, 14, '552.04207'], [6, 18, '918.74765'], [9, 19, '2305.68034'], [3, 7, '32.70521'], [1, 3, '0.43301'], [10, 10, '769.42088'], [11, 8, '584.23968'], [1, 12, '11.19615'], [9, 19, '2305.68034'], [2, 20, '126.27503'], [7, 7, '178.06171'], [12, 15, '2540.50026'], [7, 11, '458.91636'], [1, 4, '1.00000'], [4, 9, '98.90919'], [10, 14, '1533.45019'], [2, 6, '10.39230'], [6, 10, '276.99152'], [11, 15, '2134.72591'], [6, 17, '818.47771'], [4, 18, '408.33229'], [9, 5, '139.35867'], [10, 15, '1764.23629']]
        sample = choice(list(data))
        expected_output = f"Area: {float(sample[2]):.5f}\n"
        self._test_with_input(sample[:2], expected_output)

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a", "b"]), \
             self.assertRaises(ValueError):
            Task_7.main()
