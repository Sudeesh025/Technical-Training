#total paths
def path(n,ls):
    ls.append(n)
    if(n == 2):
        print(ls)
        return
    for i in s[n]:
        if(i not in ls):
            path(i,ls)
            ls.pop()

def c(n, ls, cost):
    ls.append(n)
    if n == 2:
        print("Cost:", cost, "Path:", ls)
        ls.pop()
        return
    for i in s[n]:
        if i[0] not in ls:
            new_cost = cost + i[1]  # Update the cost
            c(i[0], ls, new_cost)
    ls.pop()

def fun(n,d):
    d.append(n)
    for i in s[n]:
        if(i not in d):
            fun(i,d)
    
    return d
    
s = {5:[(7,8),(3,4)],7:[(5,8),(4,2),(3,3)],3:[(5,4),(7,3),(8,1)],4:[(7,2),(8,2),(2,4)],8:[(2,4),(3,1),(4,2)],2:[(4,4),(8,4)]}
#ls = fun(5,[])
c(5,[],0)