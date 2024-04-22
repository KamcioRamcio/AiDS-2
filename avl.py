def QuickSortLeftPivot(arr, start, end):
    if start < end:
        pivot_index = Partition(arr, start, end)
        QuickSortLeftPivot(arr, start, pivot_index - 1)
        QuickSortLeftPivot(arr, pivot_index + 1, end)
    return arr

def Partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[start], arr[right] = arr[right], arr[start]
    return right

def Mediana(arr):
    return arr[len(arr)//2]

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, arr):
        if len(arr) == 0:
            return None
        else:
            self.value = Mediana(arr)
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2+1:]
            if len(left) > 0:
                self.left = TreeNode()
                self.left.insert(left)
            if len(right) > 0:
                self.right = TreeNode()
                self.right.insert(right)
                
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.value)
        if self.right:
            self.right.in_order()
    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.value)
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
    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.value = self.right.smallest()
                self.right = self.right.delete(self.value)
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
    


my_array = [7, 8, 1, 2, 22, 58, 3, 47, 121]
# x = QuickSortLeftPivot(my_array, 0, len(my_array) - 1)
# tree = TreeNode()
# tree.insert(x)

