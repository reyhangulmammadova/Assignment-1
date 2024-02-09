import Task_2
import unittest
from unittest.mock import patch
from io import StringIO
from random import choice


class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["150"])
    def test_main_input_calls(self, mock_input):
        #with self.assertRaises(SystemExit):
        Task_2.main()
        expected_calls = ["Minute: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_2.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = {950: [15, 50], 272: [4, 32], 129: [2, 9], 882: [14, 42], 117: [1, 57], 326: [5, 26], 488: [8, 8], 727: [12, 7], 560: [9, 20], 279: [4, 39], 539: [8, 59], 554: [9, 14], 785: [13, 5], 873: [14, 33], 226: [3, 46], 10: [0, 10], 255: [4, 15], 417: [6, 57], 157: [2, 37], 810: [13, 30], 516: [8, 36], 121: [2, 1], 567: [9, 27], 646: [10, 46], 53: [0, 53], 730: [12, 10], 323: [5, 23], 187: [3, 7], 875: [14, 35], 4: [0, 4], 849: [14, 9], 427: [7, 7], 481: [8, 1], 549: [9, 9], 978: [16, 18], 904: [15, 4], 240: [4, 0], 815: [13, 35], 729: [12, 9], 703: [11, 43], 720: [12, 0], 848: [14, 8], 212: [3, 32], 572: [9, 32], 925: [15, 25], 377: [6, 17], 747: [12, 27], 871: [14, 31], 912: [15, 12], 298: [4, 58], 180: [3, 0], 965: [16, 5], 791: [13, 11], 84: [1, 24], 248: [4, 8], 237: [3, 57], 161: [2, 41], 369: [6, 9], 832: [13, 52], 956: [15, 56], 242: [4, 2], 290: [4, 50], 947: [15, 47], 123: [2, 3], 778: [12, 58], 526: [8, 46], 814: [13, 34], 37: [0, 37], 26: [0, 26], 209: [3, 29], 652: [10, 52], 86: [1, 26], 174: [2, 54], 738: [12, 18], 95: [1, 35], 277: [4, 37], 409: [6, 49], 748: [12, 28], 937: [15, 37], 880: [14, 40], 850: [14, 10], 196: [3, 16], 360: [6, 0], 335: [5, 35], 597: [9, 57], 679: [11, 19], 892: [14, 52], 883: [14, 43], 886: [14, 46], 370: [6, 10], 651: [10, 51], 514: [8, 34], 914: [15, 14], 628: [10, 28], 972: [16, 12], 931: [15, 31], 570: [9, 30], 62: [1, 2], 693: [11, 33], 400: [6, 40]}
        key, value = choice(list(data.items()))
        self._test_with_input(f'{key}', f"{key} minutes = {value[0]} hours {value[1]} minutes\n")

    def test_invalid_input(self):
        with patch('builtins.input', return_value='abc'), \
             self.assertRaises(ValueError):
            Task_2.main()
