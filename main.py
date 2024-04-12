#AVL Tree#
# Tworzenie węzła drzewa AVL
def TreeNode():
    def __init__(self,key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
#Tworzenie drzewa AVL
def AvlTree ():
    #Funkcja dodająca nowy węzeł do drzewa AVL
    def insert_node(self, root, key):
        #Sprawdzenie miejsca na umieszczenie węzła
        if not root:
            return TreeNode(key)
        elif key < root.key:
            return self.insert_node(root.left, key)
        else:
            return self.insert_node(root.right, key)
        #Aktualizacja wysokości węzła
        root_height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        #Obliczenie balansu węzła i balansowanie drzewa
        balance = self.get_balance(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        else:
            