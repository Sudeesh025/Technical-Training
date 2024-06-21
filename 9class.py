#[4,8,14,22,36,68]
#4-8 prime(7),,13,19,31,67

'''def prime(a):
    for i in range(2, a):
        if(a%i==0):
            print("not prime")
            break
        else:
            print("prime")
def addprime(a):
    for i in range(1,len(a)):
        for j in range(1,len(a)-1):
            return prime(a[i]+a[j+1])
    return a

a=[4,8,14,22,36,68]
addprime(a)'''




'''def isprime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True

def lprime(n, m):
    for i in range(m, n, -1):
        if isprime(i):
            return i
    return 0

a = [4, 8, 14, 22, 36, 68]
# a=list(map(int,input().split()))
s = 0
for i in range(len(a) - 1):
    s += lprime(a[i], a[i + 1])
print(s)'''


#4,9,8,2,14,3,5,6

#4,8,9,2,14,3,5,6
#  2,8,9,14,3,5,6
#    8,9,14,3,5,6
#       3,9,14,5,6
#          5,9,14,6
#             6,9,14

'''
#4,2,8,3,5,6,9,14    # 3 #3
a=list(map(int(input().split())))
for i in range(len(a)-2):       #slidding window to [i+2]
    if(a[i]<a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1<a[i+2]]):
        a[i+1], a[i + 2] = a[i + 1], a[i]
        if (a[i] < a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)'''


#hello:5438,car:214,book:8799,apple:2187
#oaxp   #nearest small
'''s = ''
a = input().split(',')
for i in a:
    b = i.split(":")
    l = len(b[0])
    if str(l) in b[1]:
        s = s + b[0][-1]
    else:
        for j in range(l-1, 0, -1):
            if str(j) in b[1]:
                s = s + b[0][j-1]
                break
        else:
            s = s + 'x'
print(s)'''


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

    # def lv(self,root):
    #     if(root):
    #         print(root.data,end=" ")
    #         self.lv(root.left)

    def view(self, root, c):
        if root == None:
            return
        print(root.data, c,end="")
        self.view(root.left, c + 1)
        self.view(root.right, c + 1)

    def lw(self,root,c,l):
        if(root==None):
            return
        if c not in l:
            l.append(c)
            print(root.data)

        self.lw(root.left, c + 1,l)
        self.lw(root.right, c + 1,l)

    def rv(self,root,c,l):
        if(root==None):
            return
        if c not in l:
            l.append(c)
            print(root.data)
        self.rv(root.right, c + 1, l)
        self.rv(root.left, c + 1, l)

    def top_view(self, root, c, l):
        if root is None:
            return
        if c not in l:
            l[c] = root.data  # Store the data of the node at this horizontal distance
            print(root.data)
        self.top_view(root.left, c - 1, l)
        self.top_view(root.right, c + 1, l)

    def bfs(self,root):
        if(root==None):
            return
        else:
            q = []
            d={}
            q.append((root,0))
            while(q):
                root=q[0][0]
                if(root.left!=None):
                    q.append((root.left,q[0][1]-1))
                if (root.right != None):
                    q.append((root.right,q[0][1] + 1))
                if(q[0][1] not in d):                      #
                    d[q[0][1]]=root.data
                q.pop(0)
            for i in sorted(d):
                print(d[i],end=" ")
            return d



t=tree()
t.root=Node(10)
t.create(t.root,5)
t.create(t.root,15)
t.create(t.root,2)
t.create(t.root,7)
t.create(t.root,11)
t.create(t.root,8)
t.create(t.root,9)

# t.preorder(t.root)
# t.postorder(t.root)
# t.view(t.root,0)
t.lw(t.root,0,[])
t.rv(t.root,0,[])
# t.top_view(t.root,1, [])
print("ok")
t.bfs(t.root)