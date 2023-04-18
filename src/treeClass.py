"""@package treeClass
Module with Classes to build expression tree from postfix expression
 

"""

import math

class EqNode:
    """ Equation tree node class to represent data (operators/operands) and two child nodes."""
    def __init__(self, data):
        """Constructor"""
        self.left = None
        self.right = None
        self.data = data
    """Prints node data
    @param self The object pointer"""
    def printNode(self):
        print(self.data)

class Stack():
    """ Stack class for easier way to represent stacks."""
    def __init__(self):
        """Constructor"""
        self.arr = []
    
    """Function to push element into stack.
    @param self The object pointer
    @param data Data to be pushed into stack"""
    def push(self, data):
        self.arr.append(data)

    """Function to pop top element from stack. If empty - do nothing.
    @param self The object pointer"""
    def pop(self):
        try:
            return self.arr.pop(-1)
        except:
            pass
    
    """Function to get top element from stack. If empty - do nothing.
    @param self The object pointer"""
    def top(self):
        try:
            return self.arr[-1]
        except:
            pass

    """Function to get stack size.
    @param self The object pointer"""
    def size(self):
        return len(self.arr)

class EqTree:
    """ Expression tree class for building and evaluating postfix expression"""
    def __init__(self, postfix_expr):
        """Constructor"""
        self.expr = postfix_expr
        self.root = None
        self.build_tree(self.expr)

    """Checks if element is an operator
    @param self The object pointer
    @param element Expression element to be checked"""
    def is_operator(self, element):
        opertrs = ["!", "+", "-", "*", "/", "%", "^"]
        if element in opertrs:
            return True
        return False

    """Builds expression tree from expression
    @param self The object pointer
    @param expr Postfix expression"""
    def build_tree(self, expr):
        tree_stack = Stack()
        self.root = EqNode(expr[-1]) 
        tree_stack.push(self.root)
        
        for i in reversed(expr[:-1]):
            # print(f"Building: <{i}>")
            curr_node = tree_stack.top()
            if curr_node.right is None:
                temp_node = EqNode(i)
                curr_node.right = temp_node
                if self.is_operator(i):
                    tree_stack.push(temp_node)
                # Temporary section
                # if curr_node.data == '!':
                #     curr_node.left = EqNode(0)
                # Temporary section
            else: 
                while curr_node.data == '!':
                    curr_node = tree_stack.pop()
                temp_node = EqNode(i)
                curr_node.left = temp_node
        
                tree_stack.pop()
                if self.is_operator(i):
                    tree_stack.push(temp_node)
    




    """Recursive evaluating of tree
    @param self The object pointer
    @param curr_node Current node to be evaluated"""
    def evaluate_tree(self, curr_node):
        if curr_node is None:
            return 0

        if curr_node.left is None and curr_node.right is None:
            return float(curr_node.data)

        

        left = self.evaluate_tree(curr_node.left)
        right = self.evaluate_tree(curr_node.right)
        
        if curr_node.data == "+":
            return left + right
        elif curr_node.data == "-":
            return left - right
        elif curr_node.data == "*":
            return left * right
        elif curr_node.data == "/":
            return left / right
        elif curr_node.data == "^":
            return left ** right
        elif curr_node.data == '!':
            return math.factorial(int(right))
        elif curr_node.data == '%':
            return left % right

    


# if __name__ == "__main__":
#    postfixExp = "ab+ef*g*-"
#    et = EqTree(postfixExp)
#    et.infixExp()