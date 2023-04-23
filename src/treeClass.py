##
# @file treeClass.py
# @package treeClass
# @brief Module with Classes to build expression tree from postfix expression

import math, logging

##
# @brief Equation tree node class to represent data (operators/operands) and two child nodes
class EqNode:
    ##
    # @brief Constructor
    # @param self The object pointer
    # @param data Data to be stored in the node
    def __init__(self, data):
        """Constructor"""
        self.left = None
        self.right = None
        self.data = data
    
    ##
    # @brief Print node data
    # @param self The object pointer   
    def printNode(self):
        print(self.data)

##
# @brief Stack class for easier way to represent stacks.
class Stack():
    ##
    # @brief Constructor
    # @param self The object pointer
    def __init__(self):
        self.arr = []
    
    ##
    # @brief Push element into stack
    # @param self The object pointer
    # @param data Data to be pushed into stack
    def push(self, data):
        self.arr.append(data)

    ##
    # @brief Pop top element from stack. If empty - do nothing.
    # @param self The object pointer
    def pop(self):
        try:
            return self.arr.pop(-1)
        except:
            pass
    
    ##
    # @brief Pop top element from stack. If empty - do nothing.
    # @param self The object pointer
    def top(self):
        try:
            return self.arr[-1]
        except:
            pass

    ##
    # @brief Check if stack is empty
    # @param self The object pointer
    def size(self):
        return len(self.arr)
##
# @brief Expression tree class for building and evaluating postfix expression
class EqTree:
    ##
    # @brief Constructor
    # @param self The object pointer
    # @param postfix_expr The expression, to build tree from
    def __init__(self, postfix_expr):
        self.expr = postfix_expr
        self.root = None
        self.build_tree(self.expr)

    ##
    # @brief Check if element is an operand
    # @param self The object pointer
    # @param element Expression element to be checked
    def is_operator(self, element):
        opertrs = ["!", "+", "-", "*", "/", "%", "^"]
        if element in opertrs:
            return True
        return False

    ##
    # @brief Build expression tree from expression
    # @param self The object pointer
    # @param expr Postfix expression
    def build_tree(self, expr):
        tree_stack = Stack()
        self.root = EqNode(expr[-1]) 
        tree_stack.push(self.root)
        
        for i in reversed(expr[:-1]):
            logging.debug(f"Building: <{i}>")
            curr_node = tree_stack.top()
            logging.debug(f"Curr_node.data = <{curr_node.data}>")
            # Factorial problem fixes
            if curr_node.data == '!':
                temp_node = EqNode(i)
                curr_node.right = temp_node
                curr_node.left = EqNode(0)
                tree_stack.pop()
                if self.is_operator(i):
                    tree_stack.push(temp_node)
                
                logging.debug("----------Factorial logging")
                logging.debug(f"---------After building for <{i}> at current node <{curr_node.data}>")
                logging.debug(f"---------left = <{curr_node.left.data}> || right = <{curr_node.right.data}>")
                logging.debug("----------END ofFactorial logging")

                #DEBUG ONLY
                logging.debug(f"Tree after building for <{i}> at current node <{curr_node.data}>")
                # self.print_tree(self.root, 0)
                #END OF DEBUG ONLY
                continue
                
            # else:
            if curr_node.right is None:
                temp_node = EqNode(i)
                curr_node.right = temp_node
                if self.is_operator(i):
                    tree_stack.push(temp_node)
            else: 
                # while curr_node.data == '!':
                #     curr_node = tree_stack.pop()
                temp_node = EqNode(i)
                curr_node.left = temp_node
                tree_stack.pop()
                if self.is_operator(i):
                    tree_stack.push(temp_node)
            
            logging.debug(f"After building for <{i}> at current node <{curr_node.data}>")
            if curr_node.left is None and curr_node.right is None:
                logging.debug(f"left = <None> || right = <None>")
            elif curr_node.left is None:
                logging.debug(f"left = <None> || right = <{curr_node.right.data}>")    
            elif curr_node.right is None:
                logging.debug(f"left = <{curr_node.left.data}> || right = <None>")
            else: 
                logging.debug(f"left = <{curr_node.left.data}> || right = <{curr_node.right.data}>")

            #DEBUG ONLY
            logging.debug(f"Tree after building for <{i}> at current node <{curr_node.data}>")
            # self.print_tree(self.root, 0)
            #END OF DEBUG ONLY
            #******************Before fixing:***********************

            # if curr_node.right is None:
            #     temp_node = EqNode(i)
            #     curr_node.right = temp_node
            #     if self.is_operator(i):
            #         tree_stack.push(temp_node)
            # else: 
            #     while curr_node.data == '!':
            #         curr_node = tree_stack.pop()
            #     temp_node = EqNode(i)
            #     curr_node.left = temp_node
            
            #     tree_stack.pop()
            #     if self.is_operator(i):
            #         tree_stack.push(temp_node)
    

    ##
    # @brief Recursive evaluating of tree
    # @param self The object pointer
    # @param curr_node Current node to be evaluated
    # @return Value of the node (if operand is stored in the node), 0 if root is None, result of the operation (if operator is stored in the node)
    def evaluate_tree(self, curr_node):
        if curr_node is None:
            return 0

        logging.debug(f"Evaluating: <{curr_node.data}>, left = <{curr_node.left}>, right = <{curr_node.right}>")
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
            if int(right) != right:
                raise ValueError
            return math.factorial(int(right))
        elif curr_node.data == '%':
            if int(right) != right:
                print(right)
                raise ValueError
            return left % int(right)

    ##
    # @brief Recursively print the built expression tree
    # @param self The object pointer
    # @param node Current node to be printed
    # @param tab Numers of indents
    # @return Prints built binary tree
    def print_tree(self, node : EqNode, tab : int):
        if node is None:
            return 
        
        tab += 3
        self.print_tree(node.right, tab)

        
        for i in range(0, tab):
            print(end=" ")
        print(node.data)


        self.print_tree(node.left, tab)



# if __name__ == "__main__":
#    postfixExp = "ab+ef*g*-"
#    et = EqTree(postfixExp)
#    et.infixExp()
