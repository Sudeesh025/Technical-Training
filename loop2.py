#while
'''for i in range(5):
    print(i)
print("using for")
i=0
while (i<=4):
    print(i)
    i+=1'''
'''n=int(input())
while(n<=10):
    print(n)
    if(n%2==0):
        print(n,"is even")
    else:
        print("not even")
    break'''


'''fruits=["apple","mango","banana"]
n=input()
i=0
while(i<len(fruits)):
    if(n==fruits[i]):
        print("available")
        break
    i+=1
else:
    print("not")'''
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

n=int(input())
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)'''
'''sum=0
n=int(input())
for i in range(1,n+1):
    sum+=i
print(sum)'''

'''
for i in range (5,0,-1):
    print(i,end=" ")'''
'''for i in reversed(range(1,6,1)):
    print(i,end=" ")'''

#strings
'''name="john"
for i in name:
    print(i)'''

''' letters count
a="hd hu"
count=0
for i in a:
    count+=1
    print(count)'''

''' words count
a="hd hu hu"
count=0
for i in a.split():
    count+=1
    print(count)'''


'''vehicles=["car","cycle","bike"]
for vehicle in vehicles:
    print(vehicle)
    
for i in range(len(vehicles)):
    print(vehicles[i],end=" ")'''


#dictionary
'''course={"name":"Python","instructor":"koushik"}
for i in course:
    print(i,course[i])    #i-> dictionary,keys

for i in course.values():
    print(i,end=" ")    #i->values

for i in course.keys():
    print(i,end=" ")    #i-> keys,dictionary(name,instru*)

for i in course.items():
    print(i,end=" ")    #i->both key and values'''


#try
'''
i=1
while(i<=5):
    print("hi",i)
    i+=1
print("hlp",i)'''

'''i=5
while(i>=0):
    print(i)
    i-=1       '''         #rev 5-1
'''find=input()
tuple=["banana","apple","pizza"]
# for i in tuple:
#     if(find==i):
#         print("found at")

i=0
while(i<len(tuple)):
    if(find==i):
        print("found")
'''

#odd even
'''
one=int(input("press 1 for even and 2 for odd numbers:"))
for i in range(1,10):
    if(one==1) and (i%2!=0):
        print(i,end=" ")
    elif(one==2) and (i%2==0):
        print(i,end=" ")'''

# li=list(range(1,26))
# even=[]
# odd=[]
# for i in range(1,len(li)):
#     if(i%2!=0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# a=int(input())
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)
#     i=i+1

# a=int(input())
#
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         sq=i*j
#         print(sq,end=" ")
#     print('')
'''a=5
for i in range(1,a+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")'''
#right angle
'''a=5
for i in range(1,a+1):
    for j in range(1,i+1):
        sq=i*j              
        print(sq,end=" ")
    print(" ")'''

'''n=5
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(end=" ")
    for stars in range(1,i+1):
        print("*",end=" ")
    print()'''

#pascal triagle


'''def fib(n):
    a=0
    b=1
    if(n<=0):
        print("enter valid number")
    else:
        for i in range(n+1):
            print(a,end=" ")
            s=a+b
            a=b
            b=s
fib(5)
#0+1+1+2+3+5'''

'''import random
num=random.randint(1,10)
x=1
# x=int(input("enter a number"))
while(x!=num):    #(x!=5 is not accepted !=ran num as want) if not true until true enter the loop 
# for x in range(num+1):
    if(x!=num):
        print("not accepted",x)
    x = x+1
print("accepted",x)'''

'''s=input("enter a string:")
d,l,o=0,0,0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    else:
        o+=1
print("digits",d)
print("letters",l)
print("special char",o)'''





'''
#palindrome

#madam
# m              m
# a[start]   a[end]
# start+=1    end-=1

s=input("enter your string")
s=s.replace(" ","").lower()
start=0
end=len(s)-1
flag=True

while(start<end):
    if(s[start]!=s[end]):
        flag=False
    start+=1
    end-=1
if flag:
    print("is palindrom")
else:
    print("is  not palindrom")'''


'''
n = input()
s = []
f = 0
c = 0
for i in n:
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
    print("Balanced")
else:
    print("Not Balanced")'''


def num(n):
    for i in n:
        if(i%2==0):
            o=i+1
            print(o,end=",")
            print()
        else:
            e=i+1
            print(e,end=",")

    print(o-e)
n=[3,8,9,2,4,6,9]
num(n)





