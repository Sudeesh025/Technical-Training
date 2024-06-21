'''def schedule(d, n, v, i):
    if i + 1 >= len(a):
        return v
    if n >= len(a):
        if i < len(a):
            return schedule([a[i]], i + 1, v, i + 1)
    s0 = 0
    for s in range(n, len(a)):
        if not d:
            s0 = s0 + b[i]
            d.append(a[i])
        elif a[s][0] >= d[len(d) - 1][1]:
            s0 = s0 + b[s]
            d.append(a[s])
    if s == len(a) - 1:
        if s0 > v:
            v = s0
        return schedule([], n + 1, v, i)


a = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
b = [5, 6, 5, 4, 11, 2]
v = schedule([], 0, 0, 0)
print(v)'''

'''def longest_substring(s,x='',i=0):
    if i == len(s):
        return
    for j in range(i, len(s)):
        x += s[j]
        print(x,i,j)
        longest_substring(s, x, j + 1)
        x = x[:-1]
    return x
s=input('Enter string: ')
longest_substring(s)'''
'''
s1="abcd"
s2="axbd"
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s1)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
s=" "
u=len(s1)
v=len(s2)
while u>0 and v>0:
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u-1][v]):
          u=u-1
        else:
            v=v-1
print(s[::-1])'''
#tower of annoy
'''s = ""
u = len(s1)
v = len(s2)

while u > 0 and v > 0:
    if s1[u - 1] == s2[v - 1]:
        s = s1[u - 1] + s
        u -= 1
        v -= 1
    elif m[u - 1][v] > m[u][v - 1]:
        u -= 1
    else:
        v -= 1

print(s)'''#rev




'''def op(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return 0
    # Mark as visited
    a[i][j] = 2
    # Count this cell plus all connected cells
    return 1 + op(i, j-1) + op(i, j+1) + op(i-1, j) + op(i+1, j)
''''''a[i][j]=2
    op(i,j-1,c)
    op(i,j+1,c)
    op(i-1,j,c)
    op(i+1,j,c)
    return c''''''

# Grid should be mutable, so use lists instead of tuples
a = [[0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 1]]

n = len(a) # Assuming square grid
c = 0 # Number of components
m = 0 # Size of largest component

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            k = op(i,j)
            m = max(m,k)
            c += 1
print(c,m)'''

#360-d, 30-w, 6-days
#65476
#YMWD

