"""@package middleware
Module that contains functions to prepare expression for evaluation"""

import mathlib

truly_binary_operations = '*/%^'
half_binary_operations = '+-'

"""@class BinaryOperationError
Exception that is raised when binary operation is not between two operands"""
class BinaryOperationError(Exception):
    pass

"""@class IncorrectBracketsError
Exception that is raised when incorrect number of brackets are closed or opened"""
class IncorrectBracketsError(Exception):
    pass

# to add: ()() = ()*()

# def add_multiply_between_brackets(expr: str):
#     for i, elem in enumerate(expr):
#         if 
#     return expr


"""@function check_binarity
Function that checks if binary operations are between two operands or, in case of unary operations, if they are not at the beginning or end of the expression"""
def check_binarity(expr: str):
    for i, elem in enumerate(expr):
        
        if elem in truly_binary_operations:
            if i == 0 or i == len(expr) - 1:
                raise BinaryOperationError("Error with usage of binary operator!")
            
            if not (expr[i-1].isdigit() or expr[i-1] in [')', '!']) and (expr[i+1].isdigit() or expr[i+1] == '('):
                raise BinaryOperationError("Error with usage of binary operator!")
            
        if elem in half_binary_operations:
            if i == len(expr)-1 or (not (expr[i+1].isdigit() or expr[i+1] == '(')):
                raise BinaryOperationError("Error with usage of + or -")     

"""@function check_brackets
Function that checks if number of opened brackets is equal to number of closed brackets"""
def check_brackets(expr: str):
    brackets = []
    for elem in expr:
        if elem == '(':
            brackets.append(elem)
        elif elem == ')':
            if len(brackets) == 0:
                raise IncorrectBracketsError("You have unclosed or wrong opened brackets")
            else:
                brackets.pop()
    if len(brackets) != 0:
        raise IncorrectBracketsError("You have unclosed or wrong opened brackets")
    
"""@function add_zeros
Function that adds zeros before unary minus operation"""
def add_zeros(expr: str): # good to refactor 4rl, BUT it works
    offset = 0
    while True:
        if offset == len(expr)-1:
            return expr
        for i, elem in enumerate(expr[offset:]):
            if elem == '-':
                if i == 0:
                    expr = '0' + expr
                elif not expr[offset + i - 1].isdigit() and expr[offset + i - 1] != ')' and expr[offset + i - 1] != '!':
                    lastpos = len(expr[offset+i+1:])+1
                    for j, elemin in enumerate(expr[i+1:]):
                        if not elemin.isdigit() and elemin != '.' and elemin != '!':
                            lastpos = j
                            break
                    expr = expr[:i+offset] + '(0' + expr[i+offset:i+lastpos+1+offset] + ')' + expr[i+lastpos+1+offset:]
                    offset = i + lastpos + 3
                    break
                elif i == len(expr[offset:])-1:
                    return expr
        else:
            return expr

"""@function prepare_expression
Function that prepares expression for evaluation using all other middleware functions"""
def prepare_expression(expr: str):
    temp = expr.replace(' ', '')
    check_brackets(temp)
    check_binarity(temp)
    temp = add_zeros(temp)
    return temp

if __name__ == '__main__':
    line = input()
    print(mathlib.evaluate(prepare_expression(line)))
