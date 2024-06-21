
'''def dis(d, n, o):
    d = {node: float('inf') for node in o}  # Initialize all distances as infinity
    d[n] = 0  # Distance of start node from itself is 0
    v = []
    q = [n]
    while q:
        m = float('inf')
        for i in q:
            if d[i] < m:
                m = d[i]
                n = i
        for i in o[n]:
            if i[0] not in v:
                q.append(i[0])
                if d[i[0]] > i[1] + d[n]:
                    d[i[0]] = i[1] + d[n]
        v.append(n)
        q.remove(n)
    print(v)

o = {5: [(3, 1), (1, 2), (6, 3)], 1: [(5, 2), (2, 1)], 4: [(7, 8), (2, 1)], 8: [(3, 4), (1, 2)], 3: [(5, 1), (7, 8)], 2: [(4, 8)]}
dis({}, 5, o)'''

def c(i,n,a):
    if(i>len(d)):
        print(a)
        return
    if(d[i]%2!=0):
        return c(i+1,0,a)
    else:
        if(n>=len(ns)):
            return c(i+1,0,a)
        if(ns[n]%2==0):
            return c(i,n+1,a)
        else:
            a.append(d[i]+ns[n])
            return c(i,n+1,a)
d=[6,3,2,9,4,7]
ns=[8,7,5,3,6,9]
c(0,0,[])
#[13,11,9,15,9,7,5,11,11,9,7,13


