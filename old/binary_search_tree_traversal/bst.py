class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else: 
        node.right = insert(node.right, key)
    return node
        
    
def remove(node, key):
    if node.left is None and node.right is None:
        remove(key)
    if node.left is None:
        if node.right is not None:
            
    
    


