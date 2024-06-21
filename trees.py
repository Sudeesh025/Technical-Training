class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.i = 0

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif root.data > x:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def l(self,root,c,ls):
        if(root):
            if(c not in ls):
                ls[c] = root.data
                print(root.data,c)
            elif(c < 0 and c in ls):
                if(ls[c] < root.data):
                    ls[c] = root.data
            self.l(root.left,c + 1,ls)
            self.l(root.right,c - 1,ls)
        else:
            return
    def r(self,root,c,ls):
        if(root):
            if(c not in ls):
                ls.append(c)
                print(root.data)
                self.r(root.left,c + 1,ls)
                self.r(root.right,c + 1,ls)
        else:
            return
    def bfs(self,root):
        if(root == None):
            return
        else:
            d = []
            ns = {}
            d.append((root,0))
            while(d):
                root = d[0][0]
                if(root.left != None):
                    d.append((root.left,d[0][1] - 1))
                if(root.right != None):
                    d.append((root.right,d[0][1] + 1))
                if(d[0][1] not in ns):
                    ns[d[0][1]] = root.data
                d.pop(0)
                print("hi")
            for i in sorted(ns):
                print(ns[i],end = " ")
            return ns
    #def postorder(self, root):
    #     if root:
    #         print(root.data, end=" ")
    #         self.postorder(root.left)
    #         self.postor der(root.right)

# Rest of your methods (sum, evensum, oddeven, htree, bal, checkbal, search, depth)
{5:[7,3],7:[5,4,3],3:[8,5,7],4:[7,8,2],7:[5,4,3],8:[2,4,3],2:[8,4]

t = Tree()
t.root = Node(10)
t.create(t.root, 5)
t.create(t.root, 15)
t.create(t.root, 2)
t.create(t.root, 7)
t.create(t.root, 11)
t.create(t.root, 20)
t.create(t.root, 3)
t.create(t.root, 21)
t.create(t.root, 22)
t.create(t.root, 12)
t.create(t.root, 13)
t.create(t.root, 14)

ns = {}
ns[0] = 0
t.bfs(t.root)
