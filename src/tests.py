import unittest
from middleware import prepare_expression, IncorrectBracketsError, BinaryOperationError
from mathlib import evaluate

class SimpleMathOperationsTest(unittest.TestCase):
    
    def testA(self):
        equation = "3+2"
        assert evaluate(prepare_expression(equation)) == 5
    
    def testB(self):
        equation = "3-2"
        assert evaluate(prepare_expression(equation)) == 1

    def testC(self):
        equation = "0+0"
        assert evaluate(prepare_expression(equation)) == 0

    def testD(self):
        equation = "2+0"
        assert evaluate(prepare_expression(equation)) == 2

    def testE(self):
        equation = "2-0"
        assert evaluate(prepare_expression(equation)) == 2

    def testF(self):
        equation = "0-2"
        assert evaluate(prepare_expression(equation)) == -2

    def testG(self):
        equation = "10-15"
        assert evaluate(prepare_expression(equation)) == -5

    def testH(self):
        equation = "5-10-20"
        assert evaluate(prepare_expression(equation)) == -25

    def testI(self):
        equation = "10+20+30+40+50"
        assert evaluate(prepare_expression(equation)) == 150

    def testJ(self):
        equation = "-10+5"
        assert evaluate(prepare_expression(equation)) == -5

    def testK(self):
        equation = "-10-20-30-40-50"
        assert evaluate(prepare_expression(equation)) == -150

class MulDivTests(unittest.TestCase):

    def test_mul(self):
        equation = "2*3"
        assert evaluate(prepare_expression(equation)) == 6
    def test_div(self):
        equation = "6/3"
        assert evaluate(prepare_expression(equation)) == 2
    def test_mul_div(self):
        equation = "2*3/6"
        assert evaluate(prepare_expression(equation)) == 1
    def test_div_float(self):
        equation = "2/3"
        assert evaluate(prepare_expression(equation)) == 0.6666666666666666
    def test_div_mul_float(self):
        equation = "2/3*6"
        assert evaluate(prepare_expression(equation)) == 4
    def test_mult_by_zero_left(self):
        equation = "0*2"
        assert evaluate(prepare_expression(equation)) == 0
    def test_mult_by_zero_right(self):
        equation = "5*0"
        assert evaluate(prepare_expression(equation)) == 0
    def test_div_by_one(self):
        equation = "2/1"
        assert evaluate(prepare_expression(equation)) == 2
    def test_order_mul_div(self):
        equation = "2*3/6"
        assert evaluate(prepare_expression(equation)) == 1

class OrderPowMathLib(unittest.TestCase):

    def test_order_of_pow(self):
        equation = "3^2^3"
        assert evaluate(prepare_expression(equation)) == 6561

    def test_pow_and_mul(self):
        equation = "2^3*4"
        assert evaluate(prepare_expression(equation)) == 32

    def test_negative_number_root(self):
        equation = "-9^(1/2)"
        assert evaluate(prepare_expression(equation)) == -3

    def test_order(self):
        equation = "2+2*20/4"
        assert evaluate(prepare_expression(equation)) == 12

    def test_order_with_brackets(self):
        equation = "(2+2)*20/(5-1)"
        assert evaluate(prepare_expression(equation)) == 20

    def test_factorial_pow(self):
        equation = "3!^2"
        assert evaluate(prepare_expression(equation)) == 36
    
    def test_negative_number_root_brackets(self):
        equation = "(-8)^(1/3)"
        assert evaluate(prepare_expression(equation)) == -2

    def test_negative_number_pow(self):
        equation = "(-2)^(3)"
        assert evaluate(prepare_expression(equation)) == -8

    def test_float_number_pow(self):
        equation = "3.5^2"
        assert evaluate(prepare_expression(equation)) == 12.25

    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: evaluate(prepare_expression("2/0")))

    def test_negative_factorial(self):
        self.assertRaises(ValueError, lambda: evaluate(prepare_expression("(-3)!")))
    
    def test_negative_root(self):
        self.assertRaises(ValueError, lambda: evaluate(prepare_expression("(-4)^(1/2)")))

    def test_unnatural_factorial(self):
        self.assertRaises(ValueError, evaluate(prepare_expression("3.5!")))

    def test_zero_factorial(self):
        equation = "0!"
        assert evaluate(prepare_expression(equation)) == 1

    def test_remainder_of_division(self):
        equation = "5%2"
        assert evaluate(prepare_expression(equation)) == 1

    def test_remaider_of_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: evaluate(prepare_expression('5%0')))

    def test_remainder_of_division_by_one(self):
        equation = "5%1"
        assert evaluate(prepare_expression(equation)) == 0
        
    def test_remainder_of_division_by_negative_number_without_brackets(self):
        equation = "5%-2"
        assert evaluate(prepare_expression(equation)) == -1

    def test_remainder_of_division_by_negative_number_with_brackets(self):
        equation = "5%(-2)"
        assert evaluate(prepare_expression(equation)) == -1


class AdvancedTestsMathLib(unittest.TestCase):

    def test_factorial_and_arithmetic_operations(self):
        equation = "4!-5!/5+3!"
        assert evaluate(prepare_expression(equation)) == 6

    def test_factorial_and_arithmetic_operations_with_brackets(self): # don't work
        equation = "(4!-5!)/(2+3!)"
        assert evaluate(prepare_expression(equation)) == -12

    def test_factorial_and_arithmetic_operations_with_brackets_and_negative_numbers(self): # don't work
        equation = "(-4!-5!)/(2+3!)"
        assert evaluate(prepare_expression(equation)) == -18

    def test_float_brackerts(self):
        equation = "(1.2*6.3/2*(0.5+0.75))"
        assert evaluate(prepare_expression(equation)) == 4.725

    def test_float_brackerts_2(self):
        equation = "((2.7^2 - 1.5*3)*7.1)"
        assert evaluate(prepare_expression(equation)) == 19.809

    def test_brackets_not_close(self):
        self.assertRaises(IncorrectBracketsError, lambda: evaluate(prepare_expression("(2+3-5")))

    def test_brackets_not_open(self):
        self.assertRaises(IncorrectBracketsError, lambda: evaluate(prepare_expression("2+3)-5")))

    def test_arithmetics_operation_near(self):
        self.assertRaises(BinaryOperationError, lambda: evaluate(prepare_expression("2+*3-^4")))

    def test_arithmetics_operation_near_2(self):
        self.assertRaises(BinaryOperationError, lambda: evaluate(prepare_expression("2+3-4*")))

    def test_factorial_float_brackets(self):
        self.assertRaises(ValueError, lambda: evaluate(prepare_expression("(3+3.5)!")))

class BracketsTestMathLib(unittest.TestCase):
    def test_brackets_1(self):
        equation = "(((3+7)/(3-1))*(6!-5!))-5^2"
        assert evaluate(prepare_expression(equation)) == 2975

    def test_brackets_2(self):
        equation = "(((3+7)))"
        assert evaluate(prepare_expression(equation)) == 10

    def test_brackets_3(self):
        equation = "(2+3)!"
        assert evaluate(prepare_expression(equation)) == 120

    def test_brackets_4(self):
        equation = "(2+3.5^2-8.25)!/(32%11)"
        assert evaluate(prepare_expression(equation)) == 72

    def test_brackets_5(self):
        equation = "(5+1)*(2+3)"
        assert evaluate(prepare_expression(equation)) == 30

    def test_brackets_6(self):
        equation = "((5+7)*(3-4)*((3^2)-4^(1/2)))/10"
        assert evaluate(prepare_expression(equation)) == -8.4

    def test_brackets_7(self):  
        equation = "(2+3)*(2+3)!"
        assert evaluate(prepare_expression(equation)) == 600
    
    def test_big_numbers(self):
        equation = "1000000000000000000+3246864214690521467"
        assert evaluate(prepare_expression(equation)) == 4246864214690521467
    
    def test_big_numbers_2(self):    
        equation = "1000000000000000000*10000"
        assert evaluate(prepare_expression(equation)) == 10000000000000000000000

if __name__ == '__main__':
    # try:
    #     evaluate(prepare_expression("(-4)^(1/2)"))
    # except ValueError:
    #     print("You can't take a root from a negative number")
    #     pass
    unittest.main()
