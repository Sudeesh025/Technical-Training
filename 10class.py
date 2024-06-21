def graph(n,l):                       #start=n
    l.append(n)
    for i in d[n]:
        if(i not in l):
            graph(i,l)
    return l
#pythontutorvisual
def path(n,l):
    l.append(n)
    if(n==2):
        print(l)
        return
    for i in d[n]:
        if (i not in l):
            path(i,l)
            l.pop()

def count(n,l,c):
    l.append(n)
    if (n == 2):
        print(l)
        c=c+1
        l.pop()
        return c
    for i in d[n]:
        if (i not in l):
            c=count(i,l,c)
    l.pop()
    return c

'''def wt(d,n,c):
    l.append(n)
    if (n == 2):
        print(l,c)
        c=c+1
    for i in d[n]:
        if (i[0] not in l):
            wt(d,i[0],c+i[1])
    l.pop()'''

def minwt(d,x,e,c,m,l1):
    l.append(x)
    if (x == e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if (i[0] not in l):
            m,l1=minwt(d, i[0],e, c + i[1],m,l,l1)
    l.pop()
    return m,l1

def short(n,l,c):
    l.append(n)
    if (n == 2):
        print(l)
        c=c+1
        l.pop()
        return c
    for i in d[n]:
        if (i not in l):
            c=count(i,l,c)
    l.pop()
    return c

def bfs(d,n):
    v=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if(i not in q and i not in v):
                q.append(i)
        v.append(q.pop(0))
        print(v[-1])



# v=[]
#     q=[n]
#     while(q):
#         for i in d[q[0]]:
#             if(i not in q and i not in v):
#                 q.append(i)
#         v.append(q.pop(0))
#         print(v[-1])

d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
# print(graph(5,[])
# path(5,[])
# print(count(5,[],0))
# # print(wt(d,5,0,))
# print(minwt(d,5,2,0,999,[]))               #minwt
# for i in d.keys():            #short
#     print(minwt(d,5,2,0,999,[]))

bfs(d,5)


