class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node

    def binary_search(self, value):
        if self.root_node:
          return self.root_node._binary_search(value)
        return False

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
        
    def _binary_search(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left._binary_search(value)
        elif value > self.value and self.right:
            return self.right._binary_search(value)
        else:
            return False

bin_tree = Tree()
bin_tree.insert(12)
bin_tree.insert(3)
bin_tree.insert(6)
bin_tree.insert(4)
bin_tree.insert(7)

result = bin_tree.binary_search(7)
print(result)
      
