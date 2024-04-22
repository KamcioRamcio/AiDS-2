
vizualization = "https://www.cs.usfca.edu/~galles/visualization/BST.html"
import random
random_array = random.sample(range(1, 1001), 10)
my_array=[7,8,1,2,22,58,3,47,121]



class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def insert(self,value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else: 
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)

#in_order ---- lewy, korzeń, prawy
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.value)
        if self.right:
            self.right.in_order()
#pre_order korzeń, lewy, prawy
    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
#post_order lewy, prawy, korzeń
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.value)
#Znajdowanie węzła
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
           return True
    def smallest(self):
        if self.left is None:
            return self.value
        else:
            return self.left.smallest()
    def largest(self):
        if self.right is None:
            return self.value
        else:
            return self.right.largest()
    #usuwanie
    def delete(self, value):
        if value not in my_array:
            print("Nie ma takiego elementu")
            return False
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self
        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self
        if not self.left:
            return self.right
        if not self.right:
            return self.left
        min_value = self.right.smallest()
        self.value = min_value
        self.right = self.right.delete(min_value)
        return self
    
    def delete_all(self):
            self.post_order_delete(self)
            
    def post_order_delete(self, node):
        if node:
            self.post_order_delete(node.left)
            self.post_order_delete(node.right)
            print("Usuwam węzeł", node.value)
            if node.left:
                node.left = None
            if node.right:
                node.right = None
            if node.value:
                node.value = None
            del node
            
    def right_rotate(self, root):
        current = root
        while current:
            if current.left:  
                pivot = current.left  
                current.left = pivot.right 
                pivot.right = current  
                return pivot 
            else:
                current = current.right  
        return root  
    
    def get_height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.get_height(root.left)  
            right_height = self.get_height(root.right)  
            return max(left_height, right_height) + 1 
        
    def left_rotate(self, root):
        current = root 
        while current:
            if current.right and self.get_height(current.left.right) % 2 != 0:
                pivot = current.left
                current.left = pivot.right
                pivot.right = current
                return pivot
            else:
                current = current.right
        return root
