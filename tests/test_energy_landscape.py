import unittest
import src.energy_landscapes as EL
import numpy as np


class LandscapeTest(unittest.TestCase):

    def assertBetween(self, val, minimum, maximum):
        """Function to test whether a value lies between two other values"""
        self.assertGreaterEqual(val, minimum)
        self.assertLessEqual(val, maximum)

    def test_potentials(self):
        """Test the potential functions"""
        lj_result = EL.LJ(2)
        morse_result = EL.morse(2, 6)
        self.assertAlmostEqual(-0.0615234375, lj_result)
        self.assertAlmostEqual(-0.004951360140979389, morse_result)

    def test_get_length(self):
        """Test the function to compute vector length"""
        vector = [1, 2, -4]
        length = EL.get_length(vector)
        self.assertEqual(length, np.sqrt(21))

    def test_vec_diff(self):
        """Test the function to compute difference between two vectors"""
        vector_1 = [1, 2, -4]
        vector_2 = [0.2, -5, -3]
        vec_diff = EL.vector_difference(vector_1, vector_2)
        self.assertEqual(vec_diff, [0.8, 7, -1])

    def test_generate_particles(self):
        """Test the function to place particles randomly in a box"""
        vec_dict = EL.generate_particles(5, 5)
        self.assertEqual(len(vec_dict), 5)
        key_list = [i for i in range(0, 5)]
        for key in vec_dict:
            self.assertIn(key, key_list)
            self.assertBetween(vec_dict[key][0], 0, 5)
            self.assertBetween(vec_dict[key][1], 0, 5)
            self.assertBetween(vec_dict[key][2], 0, 5)
            key_list = [i for i in key_list if i != key]

    def test_generate_energy_dict(self):
        """Test function to generate energy dictionary from a vec_dict"""
        vec_dict = {0: [0.2, 0.5, 4.5], 1: [3.4, 2.1, 0.9], 2: [1.2, 4.4, 3.8]}
        LJ_dict = EL.generate_energy_dict(vec_dict, mode='LJ')
        self.assertAlmostEquals(LJ_dict[0], -0.002185284352807964 * 0.5)
        self.assertAlmostEquals(LJ_dict[1], -0.0017231211152378314 * 0.5)
        self.assertAlmostEquals(LJ_dict[2], -0.002972446074074645 * 0.5)


if __name__ == '__main__':
    unittest.main()
