'''a=input()
b=int(input())
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)            #khoor->hello'''




# a = "xyzabcdefklmnopqefgh"
# for i in range(0, len(a)):
#     if i == ord(a[i]) - ord('a'):
#         print(i)




'''
a="xyzabcdefklmnopqefgh"    #7 len(a)
c=1
m=0 #slidingwindow
for i in range(len(a)-1):
    if(ord(a[i])==ord(a[i])-1):
        c=c+1
    else:
        c=c+1+m
print(c)'''


'''
n = int(input())
m = []
for i in range(n):
    m.append(input())
print(m)
s = input()
f = 0
for i in range(len(s)):
    if s[i] not in m[i%n]:  # Check if the character is not in the corresponding string
        print("no")
        f=1
        break
  # Print "yes" if all characters were found
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")'''
'''i/p=3
    "abc"  
    "ghi"
    "opo"
i/p:"ago" #one from each
o/p:yes'''

# num = int(input("Enter a number: "))
# temp = num
# rev = 0
#
# for _ in range(len(str(num))):
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10
#
# if num == rev:
#     print(num, "is a palindrome")
# else:
#     print(num, "is not a palindrome")

'''def rev(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return rev(x//10,re)
n=int(input())
if(x==1):
    print("yes")
else:
    print("no")  #recursive function parindrom or not #12321=yes'''

'''def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

print(max_profit([15,3,2,7,8,4]))  #(6)
print(max_profit([9,8,7,6,5,4]))  #(0)'''
'''
n=int(input())
k=1
for i in range(0,n):
    for j in range(0,n):
        if(i%(n-1)==0):    #if(i==0 or j==0 or i==a-1 or j==a-1):
            print("*",end=" ")
        else:
            if(j%(n-1)==0):
                print("*",end=" ")   ......
            else:
                print(k,end=" ")
                k=k+1
    print()

*****
*123*
*456*
*789*
*****'''

'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("1",end=" ")
        elif (i == 1 or j == 1 or i == n - 2 or j == n - 2):
            print("2", end=" ")
        elif (i == 2 or j == 2 or i == n - 3 or j == n - 3):
            print("3", end=" ")
        else:
            print(4,end=" ")
            # k=k+1
    print()'''

'''
--o--
-oooo-
oooooo'''

