'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
# a=node(10)
# b=node(20)
# c=node(30)
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
# a.nxt=b
# b.nxt=c
# print(a.data,a.nxt)
# print(b.data,b.nxt)
# print(c.data,c.nxt)
print(head.data)
print(head.nxt.data)'''

class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)

    def addfront(self,x):
        t = node(x)
        t.nxt=self.head
        self.head=t

    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t = t.nxt
        print(s)

    def search(self, x):
        t = self.head
        while t != None:
            if t.data == x:
                print("got",end="")
                break
            t = t.nxt
        return t
    def rev(self):
        t=self.head



    def middle(self):
        # t=self.head
        # c=0
        # while(t!=None):
        #     c=c+1
        #     t=t.nxt
        # c=c//2
        # t=self.t
        fast = self.head
        slow = self.head
        while fast != None and fast.nxt != None:
            slow = slow.nxt
            fast = fast.nxt.nxt
        return slow.data

    def oe(self):
        fast = self.head
        while fast != None and fast.nxt != None:
            fast = fast.nxt.nxt
        if fast == None:
            return "Even"
        else:
            return "Odd"


    def sequence(self):
        t = self.head
        c = 1
        m = 0  # sliding window
        while t.nxt != None:
            if t.data == t.nxt.data - 1:
                c = c + 1
            else:
                if c > m:
                    m = c
                c = 1
            t = t.nxt
        if c > m:
            m = c
        print(m)

    def allpais(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
        while(t1!=None):
            print(t.data,t1.data)
            t1=t1.nxt
        t=t.nxt

    def bubble(self):
        T=self.head
        p=None
        c=0
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if(f==0):
                break
            p=t
            T=T.nxt
        return c





l1 = sll()
l1.head = node(10)
l1.head.nxt = node(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)

# l1.addfront(9)
l1.display()


# l2 = sll()
# l2.head = node(100)
# l2.head.nxt = node(200)
# l2.head.nxt.nxt = node(300)
# l2.display()

print(l1.search(1))
print(l1.middle())
print(l1.oe())
a=print(l1.bubble())
print(a)
print(l1.sequence())
# print(l1.allpais())








