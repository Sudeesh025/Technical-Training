class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev = None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt

    def addfront(self,x):
        if (self.tail == None):
            self.tail = node(x)
            self.head = self.tail

        else:
            t = node(x)
            t.nxt = self.head
            self.head= t.nxt
            self.head = t

    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if t.data==x or t1.data==x:
                print()
                return x,"found"

            t=t.nxt
            t1=t1.prev
        if(t.data==x):
            return "found"
        else:
            return "not found"

    def oe(self):
        # t=self.head
        # while(t!=None):
        #     if(t.data%2==0):
        #         print(t.data,"even")
        #     else:
        #         print("no")
        #     t=t.nxt

        if self.head is None:
            return "Even"
        t = self.head
        t1 = self.tail
        while t != t1 and t != t1.nxt:
            t = t.nxt
            t1 = t1.prev
        if t == t1:
            return "Odd"
        else:
            return "Even"

    def palindrom(self):
        t = self.head
        t1 = self.tail
        while t != t1 and t != t1.nxt:
            if(t.data!=t1.data):
                return "not palindrom"
            t = t.nxt
            t1 = t1.prev
        return "yes palindrom"

    def midswap(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.nxt.nxt != None:
            slow = slow.nxt
            fast = fast.nxt.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=self.prev
        t1.nxt=None
        self.prev=None
        self.head=slow
        self.tail=t1
        # mid = slow.nxt
        # slow.nxt = None
        # mid.prev = None
        # self.tail.nxt = self.head
        # self.head.prev = self.tail
        # self.head = mid

    #swap

    #gretest

# 578214
# ts
# 752841
#
    def linky(self):
        t=self.head
        t1=self.nxt
        t3=None
        while(t.nxt!=None):
            t.nxt=t1.nxt
            t1.nxt=t
            t1.prev=t3
            t3.nxt=t1
            t,t1=t1,t
            t3=t1
        print()

    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end="->")
            t=t.nxt
    def rev_display(self):
        t=self.tail
        while (t!=None):
            print(t.data,end="->")
            t=t.prev
        print()

l=dll()
l.addback(30)
l.addback(40)
l.addfront(20)
l.addfront(10)
l.display()

# print(l.linky())

# l.oe()
# print(l.search(20))
# print(l.palindrom())
# a=4,8,2,4,4,8,4
# l.occ(a)

# print(l.midswap())
# l.rev_display()










