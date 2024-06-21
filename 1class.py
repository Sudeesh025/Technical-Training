# # res = sum(list(map(int, str(num))))

# def add_digits(num):
#     # Convert the number to a string
#     num_str = str(num)
#
#     # Initialize the sum to 0
#     sum = 0
#
#     # Iterate over each character in the string
#     for char in num_str:
#         # Convert the character back to an integer and add it to the sum
#         sum += int(char)
#     return sum
# def prime(num):
#     for i in range(2, num):
#         if (num % i == 0):
#             return("not prime")
#         else:
#             return("prime")
# sum=add_digits(201)
# print(sum)
# print(prime(sum))
#

'''def add(n):
    sum=0
    while(n):
        sum+=1
    return sum
def prime(n):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1

n=int(input())
m=n
if(n<10):
    print(prime(n))
else:
    while(1):
        n=add(n)
        if(n<10):
            break
    print(prime(n))'''



# a=[3,8,5,4,3] #even+
# b=[5,0,9,3,2]
# op:(12,17)

# def sum(x,s1,s2):
#     if(x == len(a)):
#         return s1,s2
#     if(a[x]%2==0):
#         sum+=a[x]
#     return sum(x+1,a,sum)
# print(sum(0,0,0))
# a=[3,8,5,4,3]

'''def fa(x):
    if(x==1):
        return 1
    return x*fa(x-1) #2*2-1
print(fa(5))
#factorial'''

'''def fa(x):
    if(x==0):
        return 0
    return x+fa(x-1)
print(fa(4))  '''                #sum


'''def fa(x):
    if(x==0):
        return 0             #even nums
    return x+fa(x-2)
# print(fa(4))
n=int(input())
if(n%2==0):
    print(fa(n))
else:
    print(fa(n-1))
    '''

'''def add(a):
    if(len(a)%2==0):
        print("even")
    else:
        print("odd")
a=[1,1,1,1]
add(a)'''

'''def search(n,m,f):
    str = list(n)
    for i in n:
        if(n=="m"):
            print("0")
        elif(n>="m"):
            print(m)
        else:
            print(f)

n = input()
search(n,0,0)'''
# a="FMFMFFFFMMMMMFFFMMM"
# c=0
# for i in a:
#     if(i=="M"):
#         c=c+1
#     else:
#         c=c-1


# s="leet**cod*e"
# str=list(map(str,s))
# for i in str:
#     if(i=="*"):
#         str.pop(i)
# print(str)


'''s="leet**cod*e"
b=[]
for i in s:
    if(i!="*"):
        b.append(i)
    else:
        b.pop()
print("".join(b))'''

s="is2 sentence4 This1 a3"
n=input().split()
re=[0]*len(s)
for i in s:
    re[i]

