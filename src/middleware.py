##
# @file middleware.py
# @package middleware
# @brief Module that contains functions to prepare expression for evaluation

import mathlib, logging

truly_binary_operations = '*/%^'
half_binary_operations = '+-'

##
# @brief Exception that is raised when binary operation is not between two operands
class BinaryOperationError(Exception):
    pass

##
# @brief Exception that is raised when incorrect number of brackets are closed or opened
class IncorrectBracketsError(Exception):
    pass

# to add: ()() = ()*()

# def add_multiply_between_brackets(expr: str):
#     for i, elem in enumerate(expr):
#         if 
#     return expr


##
# @brief Check if binary operations are between two operands or, in case of unary operations, if they are not at the beginning or end of the expression
# @param expr The expression, the binarity to be checked in
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

##
# @brief Check if number of opened brackets is equal to number of closed brackets
# @param expr The expression to check in
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
    
##
# @brief Add zeros before unary minus operation
# @param expr The expression to add zeros in
# @return The expression with added zeros before unary minus operation
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

##
# @brief Prepare expression for evaluation using all other middleware functions
# @param expr The expression to be prepared for evaluation
# @return The expression ready for evaluation
def prepare_expression(expr: str):
    temp = expr.replace(' ', '')
    check_brackets(temp)
    check_binarity(temp)
    temp = add_zeros(temp)
    return temp

if __name__ == '__main__':
    # Debugging
    # logging.basicConfig(level=logging.DEBUG)
    line = input()
    print(mathlib.evaluate(prepare_expression(line)))
