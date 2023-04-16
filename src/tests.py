import unittest
from middleware import Expression

class SimpleMathOperationsTest(unittest.TestCase):
    
    def testA(self):
        equation = "3+2"
        assert Expression(equation).result == 5
    
    def testB(self):
        equation = "3-2"
        assert Expression(equation).result == 1

    def testC(self):
        equation = "0+0"
        assert Expression(equation).result == 0

    def testD(self):
        equation = "2+0"
        assert Expression(equation).result == 2

    def testE(self):
        equation = "2-0"
        assert Expression(equation).result == 2

    def testF(self):
        equation = "0-2"
        assert Expression(equation).result == -2

    def testG(self):
        equation = "10-15"
        assert Expression(equation).result == -5

    def testH(self):
        equation = "5-10-20"
        assert Expression(equation).result == -25

    def testI(self):
        equation = "10+20+30+40+50"
        assert Expression(equation).result == 150

    def testJ(self):
        equation = "-10+5"
        assert Expression(equation).result == -5

    def testK(self):
        equation = "-10-20-30-40-50"
        assert Expression(equation).result == -150

class MulDivTests(unittest.TestCase):

    def test_mul(self):
        equation = "2*3"
        assert Expression(equation).result == 6
    def test_div(self):
        equation = "6/3"
        assert Expression(equation).result == 2
    def test_mul_div(self):
        equation = "2*3/6"
        assert Expression(equation).result == 1
    def test_div_float(self):
        equation = "2/3"
        assert Expression(equation).result == 0.6666666666666666
    def test_div_mul_float(self):
        equation = "2/3*6"
        assert Expression(equation).result == 4
    def test_mult_by_zero_left(self):
        equation = "0*2"
        assert Expression(equation).result == 0
    def test_mult_by_zero_right(self):
        equation = "5*0"
        assert Expression(equation).result == 0
    def test_div_by_one(self):
        equation = "2/1"
        assert Expression(equation).result == 2
    def test_order_mul_div(self):
        equation = "2*3/6"
        assert Expression(equation).result == 1

class OrderPowMathLib(unittest.TestCase):

    def test_order_of_pow(self):
        equation = "3^2^3"
        assert Expression(equation).result == 6561

    def test_pow_and_mul(self):
        equation = "2^3*4"
        assert Expression(equation).result == 32

    def test_negative_number_root(self):
        equation = "-9^(1/2)"
        assert Expression(equation).result == -3

    def test_order(self):
        equation = "2+2*20/4"
        assert Expression(equation).result == 12

    def test_order_with_brackets(self):
        equation = "(2+2)*20/(5-1)"
        assert Expression(equation).result == 20

    def test_factorial_pow(self):
        equation = "3!^2"
        assert Expression(equation).result == 36
    
    def test_negative_number_root_brackets(self):
        equation = "(-8)^(1/3)"
        assert Expression(equation).result == -2

    def test_negative_number_pow(self):
        equation = "(-2)^(3)"
        assert Expression(equation).result == -8

    def test_float_number_pow(self):
        equation = "3.5^2"
        assert Expression(equation).result == 12.25

    def test_div_by_zero(self):
        equation = "2/0"
        assert Expression(equation).result == "undef"

    def test_negative_factorial(self):
        equation = "(-3)!"
        assert Expression(equation).result == "undef"
    
    def test_negative_root(self):
        equation = "(-4)^(1/2)"
        assert Expression(equation).result == "undef"

    def test_unnatural_factorial(self):
        equation = "3.5!"
        assert Expression(equation).result == "undef"
    
    def test_zero_factorial(self):
        equation = "0!"
        assert Expression(equation).result == 1
    

if __name__ == '__main__':
    unittest.main()
