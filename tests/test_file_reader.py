import unittest
import src.file_reader as file_reader


class TestReader(unittest.TestCase):

    def test_reader(self):
        """Test the file reader"""
        input_file = 'TEST_SAMPLE_INPUT.txt'
        input_dict = file_reader.read_input(input_file)
        self.assertEqual(input_dict['N'], 7)
        self.assertEqual(input_dict['trials'], 5)
        self.assertEqual(input_dict['cycles'], 100000)
        self.assertEqual(input_dict['amp'], 0.1)
        self.assertEqual(input_dict['temp'], 1000)
        self.assertEqual(input_dict['L'], 4)
        self.assertEqual(input_dict['mode'], 'Morse')
        self.assertEqual(input_dict['anneal'], True)
        self.assertEqual(input_dict['alpha'], 0.999999999)


if __name__ == '__main__':
    unittest.main()
