import unittest
# changed importing of mathlib
from mathlib import mathlib
# from mathlib import evaluate

class TestSimpleMathLib(unittest.TestCase):
    def testA(self):
        equation = "3+2"
        assert mathlib.evaluate(equation) == 5
    
    def testB(self):
        equation = "3-2"
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

class MovDivMathLib(unittest.TestCase):

    def testA(self):
        equation = "0*2"
        assert mathlib.evaluate(equation) == 0
    def testB(self):
        equation = "2/1"
        assert mathlib.evaluate(equation) == 2
    def testC(self):
        equation = "2*3/6"
        assert mathlib.evaluate(equation) == 1

class OrderPowMathLib(unittest.TestCase):

    def test_order_of_pow(self):
        equation = "3^2^3"
        assert mathlib.evaluate(equation) == 6561

    def test_pow_and_mul(self):
        equation = "2^3*4"
        assert mathlib.evaluate(equation) == 32

    def test_negative_number_root(self):
        equation = "-9^(1/2)"
        assert mathlib.evaluate(equation) == -3

    def test_order(self):
        equation = "2+2*20/4"
        assert mathlib.evaluate(equation) == 12

    def test_order_with_brackets(self):
        equation = "(2+2)*20/(5-1)"
        assert mathlib.evaluate(equation) == 20

    def test_factorial_pow(self):
        equation = "3!^2"
        assert mathlib.evaluate(equation) == 36
    
    def test_negative_number_root_brackets(self):
        equation = "(-8)^(1/3)"
        assert mathlib.evaluate(equation) == -2

    def test_negative_number_pow(self):
        equation = "(-2)^(3)"
        assert mathlib.evaluate(equation) == -8

    def test_float_number_pow(self):
        equation = "3.5^2"
        assert mathlib.evaluate(equation) == 12.25

    #5/0, 3.5!, (-3)!, (-4)^(1/2) non defined
    

if __name__ == '__main__':
    unittest.main()
