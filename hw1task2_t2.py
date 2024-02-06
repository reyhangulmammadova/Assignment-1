import Task_2
import unittest
from io import StringIO
from unittest.mock import patch

class TestMainFunction(unittest.TestCase):
    def test_input_and_output(self):
        input_values = ['150']
        expected_output = "150 deqiqe =  2 saat 30 deqiqedir\n"
        
        with patch('builtins.input', side_effect=input_values), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_2.main()

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_invalid_input(self):
        input_values = ['abc']
        
        with patch('builtins.input', side_effect=input_values), \
             self.assertRaises(ValueError):
            Task_2.main()
