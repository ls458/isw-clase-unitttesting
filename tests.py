#! /usr/bin/env python
#
# Emiliano Reynares <reynares.emiliano@gmail.com>

import unittest
from scicalc import SciCalc

class TestLog(unittest.TestCase):
    def test_1(self):
        calc = SciCalc()
        r = calc.inverseOfLogX(10)
        self.assertEqual(1, r)

    def test_zerodivision(self):
             with self.assertRaises(ZeroDivisionError):
                 calc = SciCalc()
                 r = calc.inverseOfLogX(1)

if __name__ == '__main__':
    unittest.main()
