from middleware import *
import mathlib
from sys import stdin

num_arr = []

for line in stdin:
    num_arr += line.split()

x_line_string = "({0})/{1}".format('+'.join(num_arr), str(len(num_arr))) # x = (a+b+c+..)/n
x_line = mathlib.evaluate(x_line_string)
n_string_pow_x = "{0}*({1}^2)".format(str(len(num_arr)), x_line) # n*(x^2)
n_line_pow_x = mathlib.evaluate(n_string_pow_x)
string_sum_of_pow_x = "({0})".format('^2 +'.join(num_arr+['0'])) # (a^2 + b^2 + c^2 + ..)
line_sum_of_pow_x = mathlib.evaluate(string_sum_of_pow_x)
x_main_line = line_sum_of_pow_x - n_line_pow_x # y = (a^2 + b^2 + c^2 + ..) - n*(x^2)
n_string_main_line = "({1}/{0})^(1/2)".format(str(len(num_arr)-1), x_main_line) # (y/(n-1))^(1/2)
line_equals = mathlib.evaluate(n_string_main_line)
print(line_equals)
