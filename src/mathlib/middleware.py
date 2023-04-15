truly_binary_operations = '*/%^'
half_binary_operations = '+-'

class BinaryOperationError(Exception):
    pass

class IncorrectBracketsError(Exception):
    pass

def check_experssion(expr: str):
    brackets_count = 0
    for i, elem in enumerate(expr):
        if elem == '(':
            brackets_count += 1
        elif elem == ')':
            brackets_count -= 1
        
        if elem in truly_binary_operations:
            if i == 0 or i == len(expr) - 1:
                raise BinaryOperationError()
            
            if not (expr[i-1].isdigit() or expr[i-1] == ')') and (expr[i+1].isdigit() or expr[i+1] == '('):
                raise BinaryOperationError()
            
        if elem in half_binary_operations:
            if i == len(expr) - 1 and (not (expr[i+1].isdigit() or expr[i+1] == '(')):
                raise BinaryOperationError()     
            

    if brackets_count != 0:
        raise IncorrectBracketsError()