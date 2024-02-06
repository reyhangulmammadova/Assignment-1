
import Task2
import unittest
from io import StringIO
from unittest.mock import patch
from parameterized import parameterized

class TestMainFunction(unittest.TestCase):
    @parameterized.expand([
        (['150'], "150 deqiqe =  2 saat 30 deqiqedir\n")
    ])
   
    def test_input_and_output(self, input_values, expected_output):
        with patch('builtins.input', side_effect=lambda _: input_values.pop(0)):
            if expected_output is not None:
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    Task2.main()
                self.assertEqual(mock_stdout.getvalue(), expected_output)
            else:
                with self.assertRaises(ValueError):
                    Task2.main()
