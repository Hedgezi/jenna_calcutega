##
# @file mathlib.py
# @package mathlib
# @brief Module with functions to convert and evaluate expression using expression tree

import treeClass
import logging
 
# """Priorities of operators"""
priority = {
    '!' : 3,
    '^' : 2,
    '*' : 1,
    '/' : 1,
    '%' : 1,
    '+' : 0,
    '-' : 0,
}

# """Associativity of operators"""
associativity = {
    '!' : "unar",
    '^' : "RL",
    '*' : "LR",
    '/' : "LR",
    '%' : "LR",
    '+' : "LR",
    '-' : "LR",
}

##
# @brief Check if element is an operator
# @param element Element of expression to be checked
# @return True if element is an operator, False - otherwise
def is_operator(element):
    return element in priority.keys()


##
# @brief Check if priority of the first is higher/lower/equal than priority of the second operator
# @param oper1 The first operator 
# @param oper2 The second operator
# @return 1 if priority of oper1 is higher than the priority of oper2, -1 - if lower, 0 - if equal
def check_priority(oper1, oper2):
    
    if priority[oper1] > priority[oper2]:
        return 1
    elif priority[oper1] < priority[oper2]:
        return -1
    else:
        return 0
    
##
# @brief Convert infix expression into postfix expression
# @param infix_expr Given infix expression
def to_postfix(infix_expr):
    oper_stack = treeClass.Stack()
    postfix_expr = []

    position = 0

    while position < len(infix_expr):
        # Adding operand to postfix
        elem = infix_expr[position]
                                    
        if is_operator(elem):
            top_stack = oper_stack.top()
            if top_stack == None or top_stack == '(': # Checking if stask was empty
                oper_stack.push(elem)
                position += 1
            else:
                if check_priority(elem, top_stack) == 1:
                    oper_stack.push(elem)
                    position += 1
                elif check_priority(elem, top_stack) == 0:
                    if associativity[elem] == "LR":
                        postfix_expr.append(oper_stack.pop())
                    elif associativity[infix_expr[position]] == "RL":
                        oper_stack.push(elem)
                        position += 1
                elif check_priority(elem, top_stack) == -1:
                    postfix_expr.append(oper_stack.pop())
        
        elif elem == '(':
            oper_stack.push(elem)
            position += 1
        elif elem == ')':      
            top_stack = oper_stack.top()
            while top_stack != '(':
                postfix_expr.append(oper_stack.pop())
                top_stack = oper_stack.top()
            oper_stack.pop()
            position += 1
        else:
            operand = ''
            temp_position = position
            while temp_position < len(infix_expr) and (not is_operator(infix_expr[temp_position])
                                                  and infix_expr[temp_position] != ')'):
                operand += infix_expr[temp_position]
                logging.debug(f"{temp_position} : <{operand}>")
                temp_position += 1

            postfix_expr.append(operand)
            position += (temp_position - position)
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! neverending story
    while oper_stack.size() != 0:    
        postfix_expr.append(oper_stack.pop())
    
    return postfix_expr

##
# @brief Function to be called from side modules. Evaluates an input expression. Converting into postfix, building expression tree and evaluating it
# @param input_expr Given input expression
# @return Float value of evaluated expression 
def evaluate(input_expr):
    logging.debug(f"INPUT: <{input_expr}>")
    postfix_expr = to_postfix(input_expr)
    logging.debug(f"POSTFIX INPUT: <{postfix_expr}>")
    equation_tree = treeClass.EqTree(list(postfix_expr))
    result = equation_tree.evaluate_tree(equation_tree.root)
    return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    line = input()
    print(evaluate(line))
