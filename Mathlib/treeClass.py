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
        tree_stack.push(self.root)
        
        for i in "".join(reversed(expr[:-1])):
            curr_node = tree_stack.top()
            if not curr_node.right:
            # if right node of current node is NULL
                temp_node = EqNode(i)
                curr_node.right = temp_node
                if self.is_operator(i):
                    tree_stack.push(temp_node)
            else: # if left node of current node is NULL
                temp_node = EqNode(i)
                curr_node.left = temp_node
                # if no child node of current node is NULL
                tree_stack.pop() # pop current from stack
                if self.is_operator(i):
                    tree_stack.push(temp_node)
    
    def evaluate_tree(self, curr_node = None):
        if curr_node is None: # Initializing start of recursion 
            curr_node = self.root

        if curr_node is None: # Checking if tree is empty
            return 0
        
        if not self.is_operator(curr_node.data):
            return curr_node.data

    
    
    
    
    
    
    
    
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
    


if __name__ == "__main__":
   postfixExp = "ab+ef*g*-"
   et = EqTree(postfixExp)
   et.infixExp()