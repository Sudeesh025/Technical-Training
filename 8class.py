class Node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None

    def create(self,root,x):
        if(root==None):
            return Node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # def postorder(self,root):
    #     if(root):
    #         print(root.data,end=" ")
    #         self.postorder(root.left)
    #         self.postorder(root.right)

    def sum(self,root):
        if(root==None):
            return 0
        return root.data+self.sum(root.left)+self.sum(root.right)                  #preorder-traversal

    def evensum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        return self.evensum(root.left)+self.evensum(root.right)

    def oddeven(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        return self.evensum(root.left)+self.evensum(root.right)-root.data

    def htree(self, root):
        if root is None:
            return -1
        return max(self.htree(root.left), self.htree(root.right)) + 1

    def bal(self, root):
        return abs(self.htree(root.left) - self.htree(root.right)) <= 1

    def checkbal(self):
        if self.bal(self.root):
            print("Balanced")
        else:
            print("Not Balanced")

    def search(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return value,True
        if(root.data>value):
            return self.search(root.left,value)
        else:
            return self.search(root.right,value)
        # return self.search(root.left, value) or self.search(root.right, value)

    def depth(self,root,x,c):
        if(root==None):
            return -1
        if(root.data==x):
            return c
        if(root.data>x):
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)




'''             10
          5             20
    2         7
           6     8                      '''


t=tree()
t.root=Node(10)
t.create(t.root,5)
t.create(t.root,20)
t.create(t.root,2)
t.create(t.root,7)
t.create(t.root,6)
t.create(t.root,8)
# t.preorder(t.root)
# t.postorder(t.root)
print("sum",end="")
print(t.sum(t.root))
print("even",end="")
print(t.evensum(t.root))
print("odd and even",end=" ")
print(t.oddeven(t.root))
print("tree height",end=" ")
print(t.htree(t.root))
print("check balance tree or not",end=" ")
print(t.checkbal())
print("searching",end=" ")
print(t.search(t.root,20))
print("depth",end=" ")
print(t.depth(t.root,20,0))






#print(t.sum(t.root.left))         #for adding left



'''class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
               print("left")
            else:
               self.left.insert(data)
               print("Ro-Left")
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
                  print("Right")
               else:
                  self.right.insert(data)
                  print("R0-Right")
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data)
      if self.right:
         self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

# Preorder traversal
# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res

# Postorder traversal
# Left ->Right -> Root
   def PostorderTraversal(self, root):
      res = []
      if root:
         res = self.PostorderTraversal(root.left)
         res = res + self.PostorderTraversal(root.right)
         res.append(root.data)
      return res

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print("inorder L-Ro-R ")
print(root.inorderTraversal(root))
print("preorder Ro-L-R")
print(root.PreorderTraversal(root))
print("postorder-L-R-Ro")
print(root.PostorderTraversal(root))'''




