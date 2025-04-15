import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.7777777777777777],
            'variance': [[9.555555555555557, 0.6666666666666666, 13.555555555555555], [4.0, 10.666666666666666, 6.333333333333333], 8.209876543209875],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 3.6817870057290873], [2.0, 3.265986323710904, 2.516611478423583], 2.8635642126552705],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 34]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=5)
        self.assertAlmostEqual(actual['variance'][2], expected['variance'][2], places=5)
        self.assertAlmostEqual(actual['standard deviation'][2], expected['standard deviation'][2], places=5)
        self.assertEqual(actual['max'][2], expected['max'][2])
        self.assertEqual(actual['min'][2], expected['min'][2])
        self.assertEqual(actual['sum'][2], expected['sum'][2])

    def test_calculate_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
