'''def combination(l, k):
    def fun(curr, start):
        if (len(curr) == k):
            print(curr)
            return
        for i in range(start, len(l)):
            fun(curr + [l[i]], i + 1)
        return

    fun([], 0)
a = [3, 5, 1, 6]
k = 2
combination(a,k)'''



'''def fib(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return fib(x-1)+fib(x-2)
#               2-1     1
print(fib(3))'''

#
# def anagram(a,n,ls):
#     for i in range(0,len(a)):
#         ls.append(a[i:i+3])
#         if(i>=n):
#             return ls
#     print(ls)
#     def r(a):

# a="school"
# # p=input("school-??")
# n=3
# ls=[]
# print(anagram(a,n,ls))
# # print(a[::-1])

'''
a=input()
n=int(input())
str=[]
# str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str.append(a[int(b[2])])
    else:
        str.append(a[-int(b[2])])
        # str=str+a[-int(b[2])]
print(str)
# str=list(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    # t=list(a[i:n+i])
    t=sorted(list(a[i:n+i]))
    b.append(t)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no no")'''


'''def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print("yes")
        break
        '''

'''n=int(input())
for i in range(n):
    alpha=input()
    # alpha="qwryupcsfoghjkldezxvbintma"
    key=input()
    # key="ativedoc"
    for i in alpha:
        if(i in key):
            print(i,end="")
    print()'''

'''n=int(input())
while(n):
    alpha=input()
    s = ''
    key = input()
    for i in alpha:
        if(i in key):
            s=s+(i*key.count(i))
    print(s)
    n=n-1'''
#polikujmnhytgbvfredcxswqaz
#abbcdd

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if (len(l) == 2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)

l=[13,9,4,10,5,7]
print(fun(l))





