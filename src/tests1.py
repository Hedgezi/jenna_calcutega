import unittest
from mathlib import evaluate

class SimpleMathOperationsTestCase(unittest.TestCase):
    def testA(self):
        equation = "3+2"
        assert mathlib.evaluate(equation) == 5
    
    def testB(self):
        equeation = "3-2"
        assert mathlib.evaluate(equation) == 1

    def testC(self):
        equation = "0+0"
        assert mathlib.evaluate(equation) == 0

    def testD(self):
        equation = "2+0"
        assert mathlib.evaluate(equation) == 2

    def testE(self):
        equation = "2-0"
        assert mathlib.evaluate(equation) == 2

    def testF(self):
        equation = "0-2"
        assert mathlib.evaluate(equation) == -2

    def testG(self):
        equation = "10-15"
        assert mathlib.evaluate(equation) == -5

    def testH(self):
        equation = "5-10-20"
        assert mathlib.evaluate(equation) == -25

    def testI(self):
        equation = "10+20+30+40+50"
        assert mathlib.evaluate(equation) == 150

    def testJ(self):
        equation = "-10+5"
        assert mathlib.evaluate(equation) == -5

    def testK(self):
        equation = "-10-20-30-40-50"
        assert mathlib.evaluate(equation) == -150

if __name__ == '__main__':
    unittest.main()
