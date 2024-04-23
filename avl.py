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
    def right_rotation(self, node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        return pivot
    def left_rotation(self, node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        return pivot
    def create_vine(self,root):
        vine_head = TreeNode()  # Tworzymy nowy węzeł, który będzie głową winorośli
        vine_tail = vine_head  # Ustawiamy ogon winorośli na głowę na początku
        current = root
        
        while current:
            if current.left:  # Jeśli bieżący węzeł ma lewe poddrzewo
                # Wykonujemy rotację w prawo i aktualizujemy bieżący węzeł
                current = self.right_rotation(current)
                vine_tail.right = current  # Podpinamy bieżący węzeł do ogona winorośli
                vine_tail = current  # Aktualizujemy ogon winorośli
                current = current.right  # Przechodzimy do prawego dziecka
            else:
                # Jeśli bieżący węzeł nie ma lewego poddrzewa, przechodzimy do prawego dziecka
                vine_tail = current
                current = current.right
                
        return vine_head.right  # Zwracamy głowę winorośli
       




def tikz_tree_helper(node, level=0, pos=0, positions=None):
    if positions is None:
        positions = {}  # Definiujemy słownik positions, jeśli nie został jeszcze zdefiniowany
    if node is None:
        return "", pos
    # Check if the position is already occupied
    while (pos, -level) in positions:
        # If it is, shift the position to the right
        pos += 1
    # Record the position of the current node
    positions[(pos, -level)] = node.value  # Poprawiamy odwołanie do wartości węzła
    result = "\\node at ({},{}) {{{}}};\n".format(pos, -level, node.value)  # Poprawiamy odwołanie do wartości węzła
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
        
#my_array = [7, 8, 1, 2, 22, 58, 3, 47, 121,12,13,1,5,999,49,53,32]
#x = QuickSortLeftPivot(my_array, 0, len(my_array) - 1)
#tree = TreeNode()
#tree.insert(x)
#tree.in_order()
#tree.create_vine(tree)
#
#root=tree
#
## Wygenerowanie kodu TikZ dla drzewa
#tikz_code = tikz_tree(root)
#
## Zapisanie kodu TikZ do pliku
#writeTikzToFile("tree.tex", tikz_code)