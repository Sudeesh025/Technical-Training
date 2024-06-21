#height count occured
# a=[4,8,2,4,4,8,4]   #4
# max=0
# for i in a:
#     if(a.count(i)>max):
#         max=a.count(i)
# print(i)

# for i in a:
#     print(a.count(i))
'''
a=[1,1,2,3,1,4,1]
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)'''

'''b=[0,5,3,6,7,2,1]
n=7
sum=0
s=n*(n+1)//2
print(s)
for i in b:
    sum=sum+i
print(s-sum)'''


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

#{([

    def brace(self,i):
        t = self.head
        s = []
        f = 0
        c = 0
        while t!=0:
            if i in "({[":
                s.append(i)
            elif s:
                if (i == "}" and s[-1] == "{") or (i == ")" and s[-1] == "(") or (i == "]" and s[-1] == "["):
                    s.pop()
                else:
                    print(c)
                    f = 1
                    break
            else:
                print(c)
                f = 1
                break
        c += 1
        if f == 0 and not s:
            return -1
        else:
            return s.count(i)


#recursion

    # odd,even using recursion   #difference of even and odd
    def evod(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.nxt,es,os)

    def prime(self,t,c):
        if(t==None):
            return c
        def pnt(s,n,c1):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c=c+1
        return self.prime(t.nxt,c)

    def three(self,t,a,b,ls):
        s=""
        if(b!=None):
            s=str(t.data)+str(a.data)+str(b.data)
            ls.append(s)
            b=b.nxt
            return self.three(t,a,b,ls)
        elif(a.nxt!=None):
            a=a.nxt
            b=a.nxt
            return self.three(t,a,b,ls)
        else:
            if(t.nxt.nxt!=None):
                t=t.nxt
                a=t.nxt
                b=t.nxt.nxt
                return self.three(t,a,b,ls)
            else:
                print(ls)
                return ls
            print (ls)








    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end="->")
            t=t.nxt

l=dll()
l.addback(9)
l.addback(8)
l.addfront(6)
l.addfront(6)
l.addfront(2)
l.addfront(1)
# n=input()
# l.brace(n)
print(l.evod(l.head,0,0))
# print(l.prime(0,0))
print(l.three(l.head,l.head.nxt,l.head.nxt.nxt,[]))
l.display()
























