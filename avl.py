class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    def insert_node(self,key):
        if self.key is None:
            self.key = key
        elif key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert_node(key)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert_node(key)
                