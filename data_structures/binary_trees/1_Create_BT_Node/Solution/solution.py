class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node

    def insert(self, data):
        if not self.root_node:
            self.root_node = TreeNode(data)
        else:
            self.root_node._insert(data)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def _insert(self, data):
        if data < self.value:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left._insert(data)
        elif data > self.value:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right._insert(data)


bin_tree = Tree()
bin_tree.insert(12)
