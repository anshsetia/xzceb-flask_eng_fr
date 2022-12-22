import unittest

from translator import englishtofrench
from translator import frenchtoenglish

class Test_e2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('None'),'')
        self.assertNotEqual(englishtofrench('bye'),'bonju')

class Test_f2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish('bonjour'),'Hello')
        self.assertNotEqual(frenchtoenglish('None'),'')
        self.assertNotEqual(frenchtoenglish('bonju'),'bye')

unittest.main()