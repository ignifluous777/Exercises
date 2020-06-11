class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

bin_tree = TreeNode(27)
bin_tree.insert(14)
bin_tree.insert(35)
bin_tree.insert(10)
bin_tree.insert(19)
bin_tree.insert(31)
bin_tree.insert(42)


bin_tree.inorder(bin_tree)
