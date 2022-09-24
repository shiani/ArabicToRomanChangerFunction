import unittest
from arabic_to_roman import to_roman_numeral


class TestArabicToRomanChangerFunction(unittest.TestCase):

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
