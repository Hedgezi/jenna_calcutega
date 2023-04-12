import unittest
from mathlib.mathlib import evaluate

class SimpleMathOperationsTest(unittest.TestCase):
    
    def testA(self):
        equation = "3+2"
        assert evaluate(equation) == 5
    
    def testB(self):
        equation = "3-2"
        assert evaluate(equation) == 1

    def testC(self):
        equation = "0+0"
        assert evaluate(equation) == 0

    def testD(self):
        equation = "2+0"
        assert evaluate(equation) == 2

    def testE(self):
        equation = "2-0"
        assert evaluate(equation) == 2

    def testF(self):
        equation = "0-2"
        assert evaluate(equation) == -2

    def testG(self):
        equation = "10-15"
        assert evaluate(equation) == -5

    def testH(self):
        equation = "5-10-20"
        assert evaluate(equation) == -25

    def testI(self):
        equation = "10+20+30+40+50"
        assert evaluate(equation) == 150

    def testJ(self):
        equation = "-10+5"
        assert evaluate(equation) == -5

    def testK(self):
        equation = "-10-20-30-40-50"
        assert evaluate(equation) == -150

class MulDivTests(unittest.TestCase):

    def test_mul(self):
        equation = "2*3"
        assert evaluate(equation) == 6
    def test_div(self):
        equation = "6/3"
        assert evaluate(equation) == 2
    def test_mul_div(self):
        equation = "2*3/6"
        assert evaluate(equation) == 1
    def test_div_float(self):
        equation = "2/3"
        assert evaluate(equation) == 0.6666666666666666
    def test_div_mul_float(self):
        equation = "2/3*6"
        assert evaluate(equation) == 4
    def test_mult_by_zero_left(self):
        equation = "0*2"
        assert evaluate(equation) == 0
    def test_mult_by_zero_right(self):
        equation = "5*0"
        assert evaluate(equation) == 0
    def test_div_by_one(self):
        equation = "2/1"
        assert evaluate(equation) == 2
    def test_order_mul_div(self):
        equation = "2*3/6"
        assert evaluate(equation) == 1

class OrderPowMathLib(unittest.TestCase):

    def test_order_of_pow(self):
        equation = "3^2^3"
        assert evaluate(equation) == 6561

    def test_pow_and_mul(self):
        equation = "2^3*4"
        assert evaluate(equation) == 32

    def test_negative_number_root(self):
        equation = "-9^(1/2)"
        assert evaluate(equation) == -3

    def test_order(self):
        equation = "2+2*20/4"
        assert evaluate(equation) == 12

    def test_order_with_brackets(self):
        equation = "(2+2)*20/(5-1)"
        assert evaluate(equation) == 20

    def test_factorial_pow(self):
        equation = "3!^2"
        assert evaluate(equation) == 36
    
    def test_negative_number_root_brackets(self):
        equation = "(-8)^(1/3)"
        assert evaluate(equation) == -2

    def test_negative_number_pow(self):
        equation = "(-2)^(3)"
        assert evaluate(equation) == -8

    def test_float_number_pow(self):
        equation = "3.5^2"
        assert evaluate(equation) == 12.25

    def test_div_by_zero(self):
        equation = "2/0"
        assert evaluate(equation) == "undef"

    def test_negative_factorial(self):
        equation = "(-3)!"
        assert evaluate(equation) == "undef"
    
    def test_negative_root(self):
        equation = "(-4)^(1/2)"
        assert evaluate(equation) == "undef"

    def test_unnatural_factorial(self):
        equation = "3.5!"
        assert evaluate(equation) == "undef"
    
    def test_zero_factorial(self):
        equation = "0!"
        assert evaluate(equation) == 1
    

if __name__ == '__main__':
    unittest.main()
