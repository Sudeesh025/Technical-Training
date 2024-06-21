'''def Nqueen(r):
    if r == n:
        return True
    for c in range(n):
        if check(r, c):
            m[r][c] = 1
            if Nqueen(r + 1):
                return True
            m[r][c] = 0  # Backtrack
    return False

def check(i, j):
    # Check column
    for x in range(i):
        if m[x][j] == 1:
            return False
    # Check diagonal
    x, y = i, j
    while x >= 0 and y >= 0:
        if m[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x, y = i, j
    while x >= 0 and y < n:
        if m[x][y] == 1:
            return False
        x -= 1
        y += 1
    return True

n = 5
m = [[0 for _ in range(n)] for _ in range(n)]
if Nqueen(0):
    for row in m:
        print(row)
else:
    print("No solution")
'''

'''def Nqueen(r):
    if r == n:
        return True
    if r != u:
        for c in range(n):
            if check(r, c):
                m[r][c] = 1
                if Nqueen(r + 1):
                    return True
                m[r][c] = 0  # Backtrack
        return False
    else:
        return Nqueen(r + 1)

def check(i, j):
    # Check column
    for x in range(i):
        if m[x][j] == 1:
            return False
    # Check diagonal
    x, y = i, j
    while x >= 0 and y >= 0:
        if m[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x, y = i, j
    while x >= 0 and y < n:
        if m[x][y] == 1:
            return False
        x -= 1
        y += 1
    return True

n = 5
u = 1
v = 3
m = [[0 for _ in range(n)] for _ in range(n)]
if Nqueen(0):
    for row in m:
        print(row)
else:
    print("No solution")'''


'''''def mrng(l):
    for i in range(len(l)):
        for j in range(1,len(l)):
            if(l[i]>l[j]):
                l[j]=l[i]
                if(l[j]==l[i]):
                    break
        print(l[i],end="")
        
    '''''''max_val = float('-inf')
    result = []
    for i in range(len(l) - 1, -1, -1):
        if l[i] >= max_val:
            result.append(l[i])
            max_val = l[i]
    return result[::-1]''''''
def evng(l):
    for i in range(len(l)):
        for j in range(1,len(l)):
            if(l[i]>l[j]):
                l[j]=l[i]
        print(l[i],end="")
l=[ 3,5,9,6,8,10]
mrng(l)
# o=l[::-1]
# evng(o)'''



# i=[2,3,5,6]
#11

'''
s=tu5g2k1h8
t=g5g8gd6h3       output: 865312   astract number in even'''
'''s_input = input()
t_input = input()
digits = set()

for i in (s_input + t_input):
    if i.isdigit():
        digits.add(i)

sorted_digits = sorted(list(digits), reverse=True)
if int(sorted_digits[-1]) % 2 == 0:
    print("".join(sorted_digits))
else:
    for i in range(len(sorted_digits) - 2, -1, -1):
        if int(sorted_digits[i]) % 2 == 0:
            sorted_digits.append(sorted_digits.pop(i))
            print(''.join(sorted_digits))
            break
    else:
        print(-1)'''


'''a=int(input())
s=str(a)
while(s!=s[::-1]):
    a=a+1
    s=str(a)
print(a)'''

a="abdbsdabca"       #bdb
for i in a:
    for j in range(len(a)):
        if(a[i])

