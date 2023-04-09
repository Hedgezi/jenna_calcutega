class EqNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printNode(self):
        print(self.data)

class Stack():
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        if self.size() == 0:
            return "empty"
        return self.arr.pop(-1)
    
    def top(self):
        if self.size() == 0:
            return "empty"
        return self.arr[-1]

    def size(self):
        return len(self.arr)

class EqTree:
    def __init__(self, postfix_expr):
        self.expr = postfix_expr
        self.root = None
        self.buildTree(self.expr)

    def is_operator(element):
        opertrs = ["!", "+", "-", "*", "/", "%", "^"]
        if element in opertrs:
            return True
        return False

    def build_tree(self, expr):
        tree_stack = []
        self.root = EqNode(expr[-1]) 
        tree_stack.append(self.root)
        
    




def check():
    root = EqNode(1)
    root.printNode()

check()