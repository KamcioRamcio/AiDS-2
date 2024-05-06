
vizualization = "https://www.cs.usfca.edu/~galles/visualization/BST.html"
import random
import math
random_array = random.sample(range(1, 1001), 10)
#my_array=[7,8,1,2,22,58,3,47,121]
my_array = [1,2,3,4,5]


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
        #print(self.value)
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
            
    def right_rotate(self, node):
        #print("Rotacja w prawo wokół", node.value)
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        pivot.height = 1 + max(self.get_height(pivot.left), self.get_height(pivot.right))

        return pivot

    def left_rotate(self, node):
        #print("Rotacja w lewo wokół", node.value)
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        pivot.height = 1 + max(self.get_height(pivot.left), self.get_height(pivot.right))
        
        return pivot
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    def create_backbone(self):
        dummy = TreeNode()
        dummy.right = self
        node = dummy
        while node.right is not None:
            while node.right and node.right.left is not None:
                node.right = self.right_rotate(node.right)
            node = node.right
        return dummy.right

    def balance_backbone(self, n):
        dummy = TreeNode()
        dummy.right = self
        node = dummy
        m = 2**math.floor(math.log(n+1, 2)) - 1
        diff = n - m
        for _ in range(diff):
            if node.right and node.right.right is not None:
                node.right = self.left_rotate(node.right)
                node = node.right
        while m > 1:
            m //= 2
            node = dummy
            for _ in range(m):
                if node.right and node.right.right is not None:
                    node.right = self.left_rotate(node.right)
                    node = node.right
        return dummy.right
    def count_nodes(self):
        count = 1  # Count the current node
        if self.left is not None:
            count += self.left.count_nodes()
        if self.right is not None:
            count += self.right.count_nodes()
        return count
    
    

