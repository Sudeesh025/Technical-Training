class node():
    def __init__(self,u):
        self.data = u
        self.next = None

class ll():
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end=" ")
            t=t.next
    def rev(self):
        t=self.head

        while(t!=None):
            self.head.next=self.head
            self.head=self.head.next
            return t



    # def addback(self,x):
    #     t=self.head
    #     while(t.nxt!=None):
    #         t=t.nxt
    #     t.next=node(x)
    #
    # def addfront(self,x):
    #     t=node(x)
    #     t.nxt=self.head
    #     self.head=t
class ll2():
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end=" ")
            t=t.next
l1=ll()
l1.head=node(2)
l1.head.next=node(4)
l1.head.next.next=node(3)
l2=ll2()
l2.head=node(5)
l2.head.next=node(6)
l2.head.next.next=node(4)
l1.display()
l2.display()
print(l1.rev())
'''Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''
