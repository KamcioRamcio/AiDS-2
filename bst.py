# Dałem tu Quicksort żeby posortować tablice bo do AVL trzeba posortowaną rosnoąco tablice
#masz link żeby sobie wizułalizować jak wyglada BST które wpisujesz
vizualization = "https://www.cs.usfca.edu/~galles/visualization/BST.html"
import random
random_array = random.sample(range(1, 1001), 10)
my_array=[7,8,1,2,22,58,3,47,121]

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

#print(QuickSortLeftPivot(random_array, 0, len(random_array) - 1))

# Ta mediana to AVL
def Mediana(arr):
    m = 0
    if len(arr) % 2 == 0:
        m = arr[len(arr) // 2]
        return m
    else:
        m = (arr[len(arr) // 2] + arr[len(arr) // 2 + 1]) / 2
        return m

#print(Mediana(random_array))

# No tu sobie zrobiłem drzewo binarne BST, masz ziutka value który ci jakby definiuje aktuanly węzeł, left i right to są dzieci

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
# No tu sobie zrobiłem funkcje insert która dodaje węzeł do drzewa
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
#Tera troche nie w kolejności ale czytam i ogladam i tak tłumaczyli to tak pisze, inna sprawa że potem po prsotu inaczej będziemy wywoływać to
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
        if node is None:
            return
        self.post_order_delete(node.left)
        self.post_order_delete(node.right)
        self.delete(node.value)
        print("Usunięto: ", node.value)
        print(self.post_order())
        return   
        


