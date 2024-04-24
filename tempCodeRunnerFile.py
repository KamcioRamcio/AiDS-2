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