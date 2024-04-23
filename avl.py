class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, arr):
        if len(arr) == 0:
            return
        arr.sort()  # Sortujemy tablicę, aby umożliwić łatwiejsze tworzenie drzewa AVL
        self.root = self._create_balanced_avl(arr, 0, len(arr)-1)

    def _create_balanced_avl(self, arr, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = Node(arr[mid])

        root.left = self._create_balanced_avl(arr, start, mid - 1)
        if root.left:
            root.left.parent = root

        root.right = self._create_balanced_avl(arr, mid + 1, end)
        if root.right:
            root.right.parent = root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return root
    
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def in_order(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.in_order(node.left)
        print(node.value)
        if node.right:
            self.in_order(node.right)

    def right_rotation(self, node):
        print("Rotacja w prawo wokół", node.value)
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        pivot.height = 1 + max(self.getHeight(pivot.left), self.getHeight(pivot.right))

        return pivot

    def create_vine(self):
        root = self.root
        while root.left:
            self.right_rotate(root)
            root = root.parent

    def balance_from_vine(self, size):
        vine_height = int(size ** 0.5)
        remaining_nodes = size - (2 ** vine_height - 1)
        self.make_vine_balanced(vine_height)
        for _ in range(remaining_nodes):
            if self.root:
                self.left_rotate(self.root)

    def make_vine_balanced(self, size):
        compression_point = size // 2
        for _ in range(compression_point):
            self.left_rotate(self.root)

    def left_rotate(self, root):
        sub_root = root.parent
        right_child = root.right
        if right_child is None:
            return
        root.right = right_child.left
        if right_child.left:
            right_child.left.parent = root
        right_child.left = root
        root.parent = right_child
        right_child.parent = sub_root
        if sub_root is None:
            self.root = right_child
        elif sub_root.left == root:
            sub_root.left = right_child
        else:
            sub_root.right = right_child
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))
    
    def Biggest_Left(self, node):
        while node.right:
            node = node.right
        return node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    
    
    def delete(self, value , node):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete(value, node.left)
        elif value > node.value:
            node.right = self.delete(value, node.right)
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
            #-- Jeśli węzeł ma obu potomków to szukamy największego elementu w lewym poddrzewie --#
            temp = self.Biggest_Left(node.left)
            node.value = temp.value
            node.left = self.delete(temp.value, node.left)
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
	



avl = AVL()
avl.insert([7, 1, 2, 22, 58, 3, 47, 121,12])
avl.in_order()

avl.delete(22, avl.root)
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
tikz_code = tikz_tree(avl.root)


# Zapisanie kodu TikZ do pliku
writeTikzToFile("tree.tex", tikz_code)
