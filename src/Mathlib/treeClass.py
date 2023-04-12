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
        try:
            return self.arr.pop(-1)
        except:
            pass
    
    def top(self):
        try:
            return self.arr[-1]
        except:
            pass

    def size(self):
        return len(self.arr)

class EqTree:
    def __init__(self, postfix_expr):
        self.expr = postfix_expr
        self.root = None
        self.build_tree(self.expr)

    def is_operator(self, element):
        opertrs = ["!", "+", "-", "*", "/", "%", "^"]
        if element in opertrs:
            return True
        return False

    def build_tree(self, expr):
        tree_stack = Stack()
        self.root = EqNode(expr[-1]) 
        # print(f"Root = <{self.root.data}>")
        tree_stack.push(self.root)
        
        # for i in "".join(reversed(expr[:-1])):
        for i in reversed(expr[:-1]):
            # print(f"Building: <{i}>")
            curr_node = tree_stack.top()
            if curr_node.right is None:
                temp_node = EqNode(i)
                curr_node.right = temp_node
                if self.is_operator(i):
                    tree_stack.push(temp_node)
            else: 
                temp_node = EqNode(i)
                curr_node.left = temp_node
                # if no child node of current node is NULL
                tree_stack.pop()
                if self.is_operator(i):
                    tree_stack.push(temp_node)
    
    def new_build_tree(self, expr):
        tree_stack = Stack()
        for i in expr:
            temp_node = EqNode(i)
            if not self.is_operator(i):
                tree_stack.push(temp_node)
            else:
                # Add !
                right_value = tree_stack.pop()
                left_value = tree_stack.pop()
                temp_node.left = left_value
                # temp




    def evaluate_tree(self, curr_node):
        if curr_node is None:
            return 0

        # if curr_node is None: # Checking if tree is empty
        #     return 0
        print(f"CN : <{curr_node.data}>")
        if curr_node.left is None and curr_node.right is None:
            return float(curr_node.data)

        # if not self.is_operator(curr_node.data):
        #     return float(curr_node.data)

        left = self.evaluate_tree(curr_node.left)
        right = self.evaluate_tree(curr_node.right)
        print(f"left = <{left}>")
        print(f"right = <{right}>")
        print(f"curr_node data = <{curr_node.data}>")
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


    def inorder(self, head):
      # inorder traversal of expression tree
      # inorder traversal = > left, root, right
        if head.left:
            self.inorder(head.left)
        print(head.data, end=" ")
        if head.right:
            self.inorder(head.right)
    

    def infixExp(self):
      # inorder traversal of expression tree give infix expression
        self.inorder(self.root)
        print()
    


# if __name__ == "__main__":
#    postfixExp = "ab+ef*g*-"
#    et = EqTree(postfixExp)
#    et.infixExp()