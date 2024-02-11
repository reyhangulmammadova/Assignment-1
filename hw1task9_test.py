import Task_9
import unittest
from unittest.mock import patch
from io import StringIO
from random import choice


class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["3"])
    def test_main_input_calls(self, mock_input):
        Task_9.main()
        expected_calls = ["Number of loaves: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', return_value=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_9.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = {44: ['153.560', '92.14'], 79: ['275.710', '165.43'], 39: ['136.110', '81.67'], 35: ['122.150', '73.29'], 66: ['230.340', '138.20'], 38: ['132.620', '79.57'], 69: ['240.810', '144.49'], 14: ['48.860', '29.32'], 100: ['349.000', '209.40'], 47: ['164.030', '98.42'], 36: ['125.640', '75.38'], 49: ['171.010', '102.61'], 51: ['177.990', '106.79'], 91: ['317.590', '190.55'], 75: ['261.750', '157.05'], 59: ['205.910', '123.55'], 98: ['342.020', '205.21'], 88: ['307.120', '184.27'], 54: ['188.460', '113.08'], 71: ['247.790', '148.67'], 99: ['345.510', '207.31'], 57: ['198.930', '119.36'], 7: ['24.430', '14.66'], 95: ['331.550', '198.93'], 56: ['195.440', '117.26'], 30: ['104.700', '62.82'], 90: ['314.100', '188.46'], 13: ['45.370', '27.22'], 42: ['146.580', '87.95'], 92: ['321.080', '192.65'], 55: ['191.950', '115.17'], 12: ['41.880', '25.13'], 24: ['83.760', '50.26'], 96: ['335.040', '201.02'], 77: ['268.730', '161.24'], 27: ['94.230', '56.54'], 10: ['34.900', '20.94'], 28: ['97.720', '58.63'], 21: ['73.290', '43.97'], 97: ['338.530', '203.12'], 58: ['202.420', '121.45'], 16: ['55.840', '33.50'], 2: ['6.980', '4.19'], 60: ['209.400', '125.64'], 5: ['17.450', '10.47'], 93: ['324.570', '194.74'], 72: ['251.280', '150.77'], 64: ['223.360', '134.02'], 78: ['272.220', '163.33'], 41: ['143.090', '85.85']}
        key, value = choice(list(data.items()))
        self._test_with_input(f'{key}', f"Total price: {float(value[0]):.3f} dollars\nDiscount: {float(value[1]):.2f} dollars\n")

    def test_invalid_input(self):
        with patch('builtins.input', return_value='abc'), \
             self.assertRaises(ValueError):
            Task_9.main()
