import unittest
import translator


class Test(unittest.TestCase):


    def test_null_eng_to_fr(self):
        """Null input english to french"""
        self.assertIsNone(translator.englishToFrench(''))

    def test_null_fr_to_eng(self):
        """Null input french to english"""
        self.assertIsNone(translator.frenchToEnglish(''))

    def test_eng_to_fr(self):
        """Eng-Fr Hello"""
        self.assertEqual('Bonjour', translator.englishToFrench('Hello'))

    def test_fr_to_eng(self):
        """Fr-Eng Bonjour"""
        self.assertEqual('Hello', translator.frenchToEnglish('Bonjour'))
    '''

if __name__ == '__main__':
    unittest.main()
