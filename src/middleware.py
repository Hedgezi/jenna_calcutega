import mathlib

truly_binary_operations = '*/%^'
half_binary_operations = '+-'

class BinaryOperationError(Exception):
    pass

class IncorrectBracketsError(Exception):
    pass

# to add: ()() = ()*()

# def add_multiply_between_brackets(expr: str):
#     for i, elem in enumerate(expr):
#         if 
#     return expr

def check_experssion(expr: str):
    for i, elem in enumerate(expr):
        
        if elem in truly_binary_operations:
            if i == 0 or i == len(expr) - 1:
                raise BinaryOperationError()
            
            if not (expr[i-1].isdigit() or expr[i-1] in [')', '!']) and (expr[i+1].isdigit() or expr[i+1] == '('):
                raise BinaryOperationError()
            
        if elem in half_binary_operations:
            if i == len(expr) - 1 and (not (expr[i+1].isdigit() or expr[i+1] == '(')):
                raise BinaryOperationError()     

def check_brackets(expr: str):
    brackets = []
    for elem in expr:
        if elem == '(':
            brackets.append(elem)
        elif elem == ')':
            if len(brackets) == 0:
                raise IncorrectBracketsError()
            else:
                brackets.pop()
    if len(brackets) != 0:
        raise IncorrectBracketsError()
    
def add_zeros(expr: str):
    for i, elem in enumerate(expr):
        if elem == '-':
            if i == 0:
                expr = '0' + expr
            elif not expr[i - 1].isdigit() and expr[i - 1] != ')':
                expr = expr[:i] + '0' + expr[i:]
    return expr

def prepare_expression(expr: str):
    temp = expr.replace(' ', '')
    check_brackets(temp)
    check_experssion(temp)
    temp = add_zeros(temp)
    return temp

if __name__ == '__main__':
    line = input()
    print(mathlib.evaluate(prepare_expression(line)))
