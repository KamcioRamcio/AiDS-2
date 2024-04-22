# Dałem tu Quicksort żeby posortować tablice bo do AVL trzeba posortowaną rosnoąco tablice
#masz link żeby sobie wizułalizować jak wyglada BST które wpisujesz
vizualization = "https://www.cs.usfca.edu/~galles/visualization/BST.html"

import random

random_array = random.sample(range(1, 1001), 50)

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
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# No tu sobie zrobiłem funkcje insert która dodaje węzeł do drzewa
    def insert(self,value):
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

tree = TreeNode(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(17)
tree.in_order()
tree.pre_order()
tree.post_order()


