import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_phrase(self):
        self.assertEqual(english_to_french('Welcome'),'Bienvenue')
    def test_english_number(self):
        self.assertNotEqual(english_to_french('for'),'Trois')
    def test_french_phrase(self):
        self.assertEqual(french_to_english('bonne nuit'),'Good night')
    def test_french_number(self):
        self.assertNotEqual(french_to_english('deux'), 'one')

if __name__ == '__main__':
    unittest.main()