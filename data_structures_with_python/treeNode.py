class TreeNode:
    def __init__(self, x, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.item = x
        self.left = left
        self.right = right
    def __str__(self):
        return f"<{-1 if not self.left else self.left.item}({self.item}){-1 if not self.right else self.right.item}>"
    
if __name__ == '__main__':
    node = TreeNode(40)
    print(node)
    node2 = TreeNode(10, None, node)
    print(node2)
        