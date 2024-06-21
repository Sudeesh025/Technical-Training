class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class Binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.insert1(self.root, x)

    def insert1(self, node, x):
        if x < node.data:
            if node.left is None:
                node.left = Node(x)
            else:
                self.insert1(node.left, x)
        else:
            if node.right is None:
                node.right = Node(x)
            else:
                self.insert1(node.right, x)

    def printInorder(self, node):
        if node:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)

    def printpreorder(self, node):
        if node:
            print(node.data, end=" ")
            self.printpreorder(node.left)
            self.printpreorder(node.right)

    def printpostorder(self, node):
        if node:
            self.printpostorder(node.left)
            self.printpostorder(node.right)
            print(node.data, end=" ")
    def l(self,

# Rest of your methods (tree_sum, tree_even_sum, Absolute_diff, height, Balance, etc.)

obj = Binary_tree()

s = input("Enter the sequence: ").split()
for i in s:
    obj.insert(int(i))
obj.printInorder(obj.root)

