class Node: 

    def __init__ (self, value):
        self.left = None
        self.right = None 
        self.value = value 

    
def inorder(node):
    inorder(node.left)
    print(node)
    inorder(node.right)


def post_order(node):
    post_order(node.left)
    post_order(node.right)
    print(node)


def pre_order(node):
    print(node)
    pre_order(node.left)
    pre_order(node.right)


# **TODO: Add testcases