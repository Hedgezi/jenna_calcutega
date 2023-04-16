import mathlib

truly_binary_operations = '*/%^'
half_binary_operations = '+-'

class BinaryOperationError(Exception):
    pass

class IncorrectBracketsError(Exception):
    pass

class Expression():
    def __init__(self, expression : str):
        self.expr = expression.replace(' ', '')
        self.check_experssion()
        self.result = self.eval_expr()

    def __str__(self) -> str:
        return str(self.result)
        

    def check_brackets(self):
        brackets = []
        for elem in self.expr:
            if elem == '(':
                brackets.append(elem)
            elif elem == ')':
                if len(brackets) == 0:
                    raise IncorrectBracketsError()
                else:
                    brackets.pop()
        if len(brackets) != 0:
            raise IncorrectBracketsError()
        


    def check_experssion(self):
        self.check_brackets()
        for i, elem in enumerate(self.expr):
            
            if elem in truly_binary_operations:
                if i == 0 or i == len(self.expr) - 1:
                    raise BinaryOperationError()
                
                if not (self.expr[i-1].isdigit() or self.expr[i-1] in [')', '!']) and (self.expr[i+1].isdigit() or self.expr[i+1] == '('):
                    raise BinaryOperationError()
                
            if elem in half_binary_operations:
                if i == len(self.expr) - 1 and (not (self.expr[i+1].isdigit() or self.expr[i+1] == '(')):
                    raise BinaryOperationError()     
                

    def add_zeros(self):
        for i, elem in enumerate(self.expr):
            if elem == '-':
                if i == 0:
                    self.expr = '0' + self.expr
                elif not self.expr[i - 1].isdigit() and self.expr[i - 1] != ')':
                    self.expr = self.expr[:i:] + '0' + self.expr[i::]
                

            
        
    def eval_expr(self):
        self.add_zeros()
        return mathlib.evaluate(self.expr)


if __name__ == '__main__':
    line = input()
    print(Expression(line))