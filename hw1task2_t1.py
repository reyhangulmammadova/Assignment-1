
import Task_2
import unittest
from unittest.mock import patch

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["150"])
    def test_main_input_calls(self, mock_input):
        #with self.assertRaises(SystemExit):
        Task_2.main()
        expected_calls = ["Deqiqe-> "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

