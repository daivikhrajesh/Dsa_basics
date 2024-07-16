class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
    
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1
    
    def search(self, node, key):
        if node is None or node.val == key:
            return node
        elif key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    
    def print_height(self, key):
        node = self.search(self.root, key)
        if node is None:
            print(f"Node with value {key} not found.")
        else:
            print(f"Height of node {key}: {self.height(node)}")
    
    def print_presence(self, key):
        node = self.search(self.root, key)
        if node is not None:
            print(f"Node with key {key} is found.")
        else:
            print(f"Node with key {key} is not found.")
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    
    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val)

if __name__ == "__main__":
    bst = BinaryTree()
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        bst.root = bst.insert(bst.root, key)
    
    print("Height of the tree:", bst.height(bst.root))
    
    bst.print_presence(30)
    """ bst.print_presence(55)
    bst.print_presence(80) """

    bst.print_height(30)
    #bst.print_height(60)
    bst.print_height(90)
