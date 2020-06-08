class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node

    def insert(self, data):
        if not self.root_node:
            self.root_node = TreeNode(data)
        else:
            self.root_node._insert(data)
            
    def visit(self):
        print(self)
        
    def __str__(self):
        root = self.root_node if self.root_node else ''
        return f'<{root}>'
  
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        left = f'{self.left}, ' if self.left else ''
        right = f', {self.right}' if self.right else ''
        return f'{left}{self.value}{right}'
        
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
bin_tree.insert(3)
bin_tree.insert(6)
bin_tree.insert(4)
bin_tree.insert(7)

bin_tree.visit()
