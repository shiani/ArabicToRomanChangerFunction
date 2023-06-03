import unittest

class RomanNumeralConversionTests(unittest.TestCase):

    def test_valid_values(self):
        # Test valid values and their expected Roman numeral representations
        test_cases = [
            (1, 'I'),
            (4, 'IV'),
            (9, 'IX'),
            (40, 'XL'),
            (90, 'XC'),
            (400, 'CD'),
            (500, 'D'),
            (900, 'CM'),
            (1000, 'M'),
            (3999, 'MMMCMXCIX'),
        ]

        for value, expected_result in test_cases:
            result = to_roman_numeral(value)
            self.assertEqual(result, expected_result)

    def test_invalid_values(self):
        # Test invalid values that should raise a ValueError
        invalid_values = [
            -1,
            0,
            4000,
            3.5,
            'abc',
            None,
        ]

        for value in invalid_values:
            with self.assertRaises(ValueError):
                to_roman_numeral(value)

    def test_random_values(self):
        # Test random values and their expected Roman numeral representations
        random_test_cases = [
            (2, 'II'),
            (16, 'XVI'),
            (49, 'XLIX'),
            (137, 'CXXXVII'),
            (512, 'DXII'),
            (1987, 'MCMLXXXVII'),
            (2019, 'MMXIX'),
            (3456, 'MMMCDLVI'),
        ]

        for value, expected_result in random_test_cases:
            result = to_roman_numeral(value)
            self.assertEqual(result, expected_result)
            
    def test_functionality(self):
        # all the examples in wikipedia's Roman numerals page
        self.assertEqual(to_roman_numeral(39), 'XXXIX')
        self.assertEqual(to_roman_numeral(246), 'CCXLVI')
        self.assertEqual(to_roman_numeral(789), 'DCCLXXXIX')
        self.assertEqual(to_roman_numeral(2421), 'MMCDXXI')
        self.assertEqual(to_roman_numeral(160), 'CLX')
        self.assertEqual(to_roman_numeral(207), 'CCVII')
        self.assertEqual(to_roman_numeral(1009), 'MIX')
        self.assertEqual(to_roman_numeral(1066), 'MLXVI')
        self.assertEqual(to_roman_numeral(1776), 'MDCCLXXVI')
        self.assertEqual(to_roman_numeral(1918), 'MCMXVIII')
        self.assertEqual(to_roman_numeral(1954), 'MCMLIV')
        self.assertEqual(to_roman_numeral(2014), 'MMXIV')
        
        
if __name__ == '__main__':
    unittest.main()
