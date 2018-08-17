import unittest

import sys
sys.path.append('..')

from algs4.In import In


class InTest(unittest.TestCase):

    def test_charset(self):
        self.assertEqual(In.CHARSET_NAME, "UTF-8")

    def test_language(self):
        self.assertEqual(In.LOCALE, 0)

