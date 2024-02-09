import Task_3
import unittest
from io import StringIO
from unittest.mock import patch
from random import choice

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["2024"])
    def test_main_input_calls(self, mock_input):
        Task_3.main() 
        expected_calls = ["Enter 4 digit number: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_3.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = {4689: [4, 6, 8, 9], 1879: [1, 8, 7, 9], 1310: [1, 3, 1, 0], 7990: [7, 9, 9, 0], 2818: [2, 8, 1, 8], 9643: [9, 6, 4, 3], 8489: [8, 4, 8, 9], 8249: [8, 2, 4, 9], 1424: [1, 4, 2, 4], 1025: [1, 0, 2, 5], 1483: [1, 4, 8, 3], 9542: [9, 5, 4, 2], 9333: [9, 3, 3, 3], 6775: [6, 7, 7, 5], 6249: [6, 2, 4, 9], 5316: [5, 3, 1, 6], 4308: [4, 3, 0, 8], 9977: [9, 9, 7, 7], 3437: [3, 4, 3, 7], 7597: [7, 5, 9, 7], 4190: [4, 1, 9, 0], 7959: [7, 9, 5, 9], 2089: [2, 0, 8, 9], 2403: [2, 4, 0, 3], 2430: [2, 4, 3, 0], 3809: [3, 8, 0, 9], 7395: [7, 3, 9, 5], 4454: [4, 4, 5, 4], 6079: [6, 0, 7, 9], 6553: [6, 5, 5, 3], 7856: [7, 8, 5, 6], 7334: [7, 3, 3, 4], 4911: [4, 9, 1, 1], 3050: [3, 0, 5, 0], 7231: [7, 2, 3, 1], 6192: [6, 1, 9, 2], 4377: [4, 3, 7, 7], 7723: [7, 7, 2, 3], 7498: [7, 4, 9, 8], 9308: [9, 3, 0, 8], 9644: [9, 6, 4, 4], 2335: [2, 3, 3, 5], 9682: [9, 6, 8, 2], 3667: [3, 6, 6, 7], 6058: [6, 0, 5, 8], 4878: [4, 8, 7, 8], 7836: [7, 8, 3, 6], 8980: [8, 9, 8, 0], 4945: [4, 9, 4, 5], 7999: [7, 9, 9, 9], 5555: [5, 5, 5, 5], 3081: [3, 0, 8, 1], 3013: [3, 0, 1, 3], 8602: [8, 6, 0, 2], 4536: [4, 5, 3, 6], 9316: [9, 3, 1, 6], 1763: [1, 7, 6, 3], 2572: [2, 5, 7, 2], 1407: [1, 4, 0, 7], 3037: [3, 0, 3, 7], 1844: [1, 8, 4, 4], 1533: [1, 5, 3, 3], 7943: [7, 9, 4, 3], 1282: [1, 2, 8, 2], 9969: [9, 9, 6, 9], 7091: [7, 0, 9, 1], 4268: [4, 2, 6, 8], 2656: [2, 6, 5, 6], 9046: [9, 0, 4, 6], 6325: [6, 3, 2, 5], 8321: [8, 3, 2, 1], 1071: [1, 0, 7, 1], 3954: [3, 9, 5, 4], 9117: [9, 1, 1, 7], 5943: [5, 9, 4, 3], 6465: [6, 4, 6, 5], 3018: [3, 0, 1, 8], 2663: [2, 6, 6, 3], 7309: [7, 3, 0, 9], 8613: [8, 6, 1, 3], 7299: [7, 2, 9, 9], 6122: [6, 1, 2, 2], 8336: [8, 3, 3, 6], 6774: [6, 7, 7, 4], 7951: [7, 9, 5, 1], 4836: [4, 8, 3, 6], 5828: [5, 8, 2, 8], 6234: [6, 2, 3, 4], 1886: [1, 8, 8, 6], 7711: [7, 7, 1, 1], 1827: [1, 8, 2, 7], 5522: [5, 5, 2, 2], 1903: [1, 9, 0, 3], 1077: [1, 0, 7, 7], 5034: [5, 0, 3, 4], 2211: [2, 2, 1, 1], 3953: [3, 9, 5, 3], 9013: [9, 0, 1, 3], 6360: [6, 3, 6, 0], 6851: [6, 8, 5, 1]}
        key, value = choice(list(data.items()))
        prod = value[0]*value[1]*value[2]*value[3]
        expected_output = f'Digits: {value[0]} {value[1]} {value[2]} {value[3]}\n' \
                            f'Sum of digits: {value[0]} + {value[1]} + {value[2]} + {value[3]} = {sum(value)}\n' \
                            f'Product of digits: {value[0]} * {value[1]} * {value[2]} * {value[3]} = {prod}\n' 
        self._test_with_input(key, expected_output)

    def test_invalid_input(self):
        with patch('builtins.input', return_value='abc'), \
             self.assertRaises(ValueError):
            Task_3.main()
