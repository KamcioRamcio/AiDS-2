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




class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Wysokość węzła (początkowo 1)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Aktualizacja wysokości węzła
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Zrównoważenie drzewa
        balance = self._get_balance(node)

        # Przypadki rotacji
        # LL Rotation
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        # RR Rotation
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        # LR Rotation
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # RL Rotation
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Rotacja
        y.right = z
        z.left = T3

        # Aktualizacja wysokości
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Rotacja
        y.left = z
        z.right = T2

        # Aktualizacja wysokości
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)


# Przykładowe użycie
avl_tree = AVLTree()
values = [10, 5, 15, 3, 7, 12, 17]

for value in values:
    avl_tree.insert(value)

print("Pre-order traversal:")
avl_tree.pre_order()
