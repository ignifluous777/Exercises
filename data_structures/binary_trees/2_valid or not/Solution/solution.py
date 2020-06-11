class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def valid_bst(self, root_node):
        if not root_node:
            return
        key = root_node.value 
        if root_node.left:
            left_search = root_node.left.min_bst(root_node.value, key)
        else:
            left_search = True
        if root_node.right:
            right_search = root_node.right.max_bst(root_node.value, key)
        else:
            right_search = True
        if left_search == True and right_search == True:
            return True
        else:
            return False

    def min_bst(self, curr, key):
        if self.value < curr and self.value < key:
            if self.left:
                self.left.min_bst(self.value, key)
            if self.right:
                self.right.max_bst(self.value, key)
            return True
        else:
            return False

    def max_bst(self, curr, key):
        if self.value > curr and self.value > key:
            if self.left:
                self.left.min_bst(self.value, key)
            if self.right:
                self.right.max_bst(self.value, key)
            return True
        else:   
            return False


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(4)
node.right.left = TreeNode(6)
node.right.right = TreeNode(8)

node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.right = TreeNode(3)

# valid BST
result = node.valid_bst(node)
print(result)
# Invalid BST
result2 = node2.valid_bst(node2)
print(result2)


