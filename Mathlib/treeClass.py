class EqNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def printNode(self):
        print(self.data)





def check():
    root = EqNode(1)
    root.printNode()

check()