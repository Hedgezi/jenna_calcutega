import unittest
from middleware import *

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
        self.assertRaises(ZeroDivisionError, Expression(equation))

    def test_negative_factorial(self):
        equation = "(-3)!"
        self.assertRaises(ValueError, Expression(equation).result)
    
    def test_negative_root(self):
        equation = "(-4)^(1/2)"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_unnatural_factorial(self):
        equation = "3.5!"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_zero_factorial(self):
        equation = "0!"
        assert Expression(equation).result == 1

    def test_remainder_of_division(self):
        equation = "5%2"
        assert Expression(equation).result == 1

    def test_remaider_of_division_by_zero(self):
        equation = "5%0"
        self.assertRaises(ZeroDivisionError, Expression(equation).result)

    def test_remainder_of_division_by_one(self):
        equation = "5%1"
        assert Expression(equation).result == 0
    def test_remainder_of_division_by_negative_number_without_brackets(self):
        equation = "5%-2"
        assert Expression(equation).result == -1

    def test_remainder_of_division_by_negative_number_with_brackets(self):
        equation = "5%(-2)"
        assert Expression(equation).result == -1


class AdvancedTestsMathLib(unittest.TestCase):

    def test_factorial_and_arithmetic_operations(self):
        equation = "4!-5!/5+3!"
        assert Expression(equation).result == 6

    def test_factorial_and_arithmetic_operations_with_brackets(self):
        equation = "(4!-5!)/(2+3!)"
        assert Expression(equation).result == -12

    def test_factorial_and_arithmetic_operations_with_brackets_and_negative_numbers(self):
        equation = "(-4!-5!)/(2+3!)"
        assert Expression(equation).result == -18

    def test_float_brackerts(self):
        equation = "(1.2*6.3/2*(0.5+0.75))"
        assert Expression(equation).result == 4.725

    def test_float_brackerts_2(self):
        equation = "((2.7^2 - 1.5*3)*7.1)"
        assert Expression(equation).result == 19.809

    def test_brackets_not_close(self):
        equation = "(2+3-5"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_brackets_not_open(self):
        equation = "2+3)-5"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_arithmetics_operation_near(self):
        equation = "2+*3-^4"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_arithmetics_operation_near_2(self):
        equation = "2+3-4*"
        self.assertRaises(ValueError, Expression(equation).result)

    def test_factorial_float_brackets(self):
        equation = "(3+3.5)!"
        self.assertRaises(ValueError, Expression(equation).result)

class BracketsTestMathLib(unittest.TestCase):
    def test_brackets_1(self):
        equation = "((((3+7)/(3-1))*(6!-5!))-5^2"
        assert Expression(equation).result == 2975

    def test_brackets_2(self):
        equation = "(((3+7)))"
        assert Expression(equation).result == 10

    def test_brackets_3(self):
        equation = "(2+3)!"
        assert Expression(equation).result == 120

    def test_brackets_4(self):
        equation = "(2+3.5^2-8.25)!/(32%11)"
        assert Expression(equation).result == 72

    def test_brackets_5(self):
        equation = "(5+1)*(2+3)"
        assert Expression(equation).result == 30

    def test_brackets_6(self):
        equation = "((5+7)*(3-4)*((3^2)-4^(1/2))/10"
        assert Expression(equation).result == -8.4

    def test_brackets_7(self):  
        equation = "(2+3)*(2+3)!"
        assert Expression(equation).result == 600
    
    def test_big_numbers(self):
        equation = "1000000000000000000+3246864214690521467"
        assert Expression(equation).result == 4246864214690521467
    
    def test_big_numbers_2(self):    
        equation = "1000000000000000000*10000"
        assert Expression(equation).result == 10000000000000000000000

if __name__ == '__main__':
    unittest.main()
