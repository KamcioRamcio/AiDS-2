class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insertNode(value, self.root)
    
    def insertNode(self, value, node):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insertNode(value, node.left)
        elif value > node.value:
            node.right = self.insertNode(value, node.right)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        balance = self.get_balance(node)

        # Balansowanie drzewa po wstawieniu nowego węzła
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def build_tree(self, arr):
        arr.sort()
        self.root = self.build_avl(arr)
        return self.root
    def build_avl(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.build_avl(arr[:mid])
        root.right = self.build_avl(arr[mid+1:])
        return root
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def Biggest_Left(self, node):
        while node.right:
            node = node.right
        return node

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    
    
    
    def in_order(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.in_order(node.left)
        print(node.value)
        if node.right:
            self.in_order(node.right)
    def post_order(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node.value)
        
    def pre_order(self, node=None):
        if node is None:
            node = self.root
        print(node.value)
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    def right_rotate(self, node):
        print("Rotacja w prawo wokół", node.value)
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        pivot.height = 1 + max(self.get_height(pivot.left), self.get_height(pivot.right))

        return pivot

    def left_rotate(self, node):
        print("Rotacja w lewo wokół", node.value)
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        pivot.height = 1 + max(self.get_height(pivot.left), self.get_height(pivot.right))
        
        return pivot
    
    
    
    def find_node(self, value, node=None):
        if node is None:
            node = self.root
            
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self.find_node(value, node.left)
        else:
            return self.find_node(value, node.right)

    
    def delete(self, value, node=None):
        if node is None:
            node = self.root
        self.root = self.deleteNode(value, node)
    
    def deleteNode(self, value, node):
        if node is None:
            return None
        if value < node.value:
            node.left = self.deleteNode(value, node.left)
        elif value > node.value:
            node.right = self.deleteNode(value, node.right)
        else:
            if not node.left and not node.right:
                del node
                return None
            if not node.left:
                temp = node.right
                del node
                return temp
            if not node.right:
                temp = node.left
                del node
                return temp
            temp = self.Biggest_Left(node.left)
            node.value = temp.value
            node.left = self.deleteNode(temp.value, node.left)
        if not node:
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        #-- patrz def get_balance --#
        #-- Jeżeli jest większe niz 1 to znaczy że lewe poddrzewo jest większe --#
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        #-- Jeżeli jest mniejsze niz 1 to znaczy że prawe poddrzewo jest większe --#
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        #-- Jeżeli jest większe niz 1 to znaczy że lewe poddrzewo jest większe ale prawe poddrzewo tego poddrzewa jest większe --#
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        #-- Jeżeli jest mniejsze niz 1 to znaczy że prawe poddrzewo jest większe ale lewe poddrzewo tego poddrzewa jest większe --#
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def delete_all(self):
        self.post_order_delete(self.root)
        
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
    def smallest(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node.value
    def biggest(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node.value
    

avl = AVL()
avl.build_tree([7, 1, 2, 22, 58, 3, 47, 121, 12])
avl.in_order()
avl.delete(22)
avl.in_order()


def tikz_tree_helper(node, level=0, pos=0, positions=None):
    if positions is None:
        positions = {}
    if node is None:
        return "", pos
    while (pos, -level) in positions:
        pos += 1
    positions[(pos, -level)] = node.value
    result = "\\node at ({},{}) {{{}}};\n".format(pos, -level, node.value)
    if node.left:
        left_result, left_pos = tikz_tree_helper(node.left, level+1, pos-1, positions)
        result += left_result
        result += "\\draw ({},{}) -- ({},{});\n".format(pos, -level, left_pos, -(level+1))
    if node.right:
        right_result, right_pos = tikz_tree_helper(node.right, level+1, pos+1, positions)
        result += right_result
        result += "\\draw ({},{}) -- ({},{});\n".format(pos, -level, right_pos, -(level+1))
    return result, pos


def tikz_tree(node):
    result, _ = tikz_tree_helper(node)
    return result

def writeTikzToFile(filename, text):
    with open(filename, 'w') as file:
        file.write("\\documentclass{standalone}\n")
        file.write("\\usepackage{tikz}\n")
        file.write("\\begin{document}\n")
        file.write("\\begin{tikzpicture}[\n")
        file.write("level distance=1cm,\n")
        file.write("level 1/.style={sibling distance=3cm},\n")
        file.write("level 2/.style={sibling distance=1.5cm},\n")
        file.write("level 3/.style={sibling distance=1cm}\n")
        file.write("]\n")
    file.close()
    with open(filename, 'a') as file:
        file.write(text)
    file.close()
    with open(filename, 'a') as file:
        file.write("\\end{tikzpicture}\n")
        file.write("\\end{document}\n")
        
        

#Wygenerowanie kodu TikZ dla drzewa
#tikz_code = tikz_tree(avl.root)
#
#
## Zapisanie kodu TikZ do pliku
#writeTikzToFile("tree.tex", tikz_code)
#