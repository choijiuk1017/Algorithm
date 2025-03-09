from treeNode import TreeNode

class BST:
    def __init__(self):
        self.__root = None
    def getParent(self, node: TreeNode) -> TreeNode:
        return self.find(node.item)[1]
    def predecessor(self, node: TreeNode) -> TreeNode: # problem 1
        _, parent = self.find(node.item)
        if parent == node: # root node
            if not node.left:
                return None
            return self.rightmost(node.left, node)[0]
        if parent.item < node.item:
            return parent
        if not node.left:
            _, grandparent = self.find(parent.item)
            if grandparent is parent:
                return None
            return grandparent
        return self.rightmost(node.left, node)[0]
    def print(self):
        def _print(node):
            if not node: return
            print(node, end=' ')
            _print(node.left)
            _print(node.right)
        _print(self.__root)
        print()
    def insert(self, x):
        def _insert(node, x): # node should not be None
            if x == node.item: return
            if x < node.item:
                if not node.left:
                    node.left = TreeNode(x)
                    return
                _insert(node.left, x)
            else:
                if not node.right:
                    node.right = TreeNode(x)
                    return
                _insert(node.right, x)
        if not self.__root:
            self.__root = TreeNode(x)
            return
        _insert(self.__root, x)
        
    def insert2(self, x):
        def _insert(node, x):
            if not node: return TreeNode(x)
            if x < node.item:
                node.left = _insert(node.left, x)
            else:
                node.right = _insert(node.right, x)
            return node
        self.__root = _insert(self.__root, x)
    def rightmost(self, node, parent):
        if not node.right:
            return node, parent
        return self.rightmost(node.right, node)
    def delete(self, x):
        def _delete(node, x):
            if not node: return node
            if x == node.item:
                if not node.left and not node.right: # case (1)
                    del node
                    return None
                elif not node.right: # case (2)
                    candidate = node.left
                    del node
                    return candidate
                elif not node.left: # case (2)
                    candidate = node.right
                    del node
                    return candidate
                else: # case (3)
                    candidate, candidate_parent = self.rightmost(node.left, node)
                    candidate.item, node.item = node.item, candidate.item
                    target = _delete(candidate, x)
                    self.setParent(candidate_parent, candidate, target)
                    return node
            elif x < node.item:
                node.left = _delete(node.left, x)
            else:
                node.right = _delete(node.right, x)
            return node
        self.__root = _delete(self.__root, x)
    def setParent(self, parent, f, t):
        if parent == f:
            self.__root = t
            return
        if parent.left == f:
            parent.left = t
        elif parent.right == f:
            parent.right = t
    def search(self, x):
        def _search(node, x):
            if not node: return None
            if x == node.item: return node
            if x < node.item: return _search(node.left, x)
            return _search(node.right, x)
        return _search(self.__root, x)
    def find(self, x):
        parent = node = self.__root
        while node:
            if node.item == x:
                return node, parent
            parent = node
            node = node.left if x < node.item else node.right
        return node, parent
    def leftRotation(self, t, parent):
        if not t: return
        newRoot = t.right
        if not t.right: return
        t.right = newRoot.left
        newRoot.left = t
        self.setParent(parent, t, newRoot)
    def rightRotation(self, t, parent):
        if not t: return
        newRoot = t.left
        if not t.left: return
        t.left = newRoot.right
        newRoot.right = t
        self.setParent(parent, t, newRoot)
if __name__ == '__main__':
    bst = BST()
    for item in [40, 20, 55, 17, 37, 70, 15, 30, 38, 35]:
        bst.insert2(item)
    arr =     [40, 20, 55, 17, 37, 70, 15, 30, 38, 35]
    arr.sort()
    print(arr)
    
    bst.print()
    for item in [40, 20, 55, 17, 37, 70, 15, 30, 38, 35]:
        target, parent = bst.find(item)
        print(f'predecessor of {target} is {bst.predecessor(target)}')
    
        