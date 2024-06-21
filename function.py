#function (no redunded/repeat)

#function defination
'''def cal_sum(a,b):#parameters
    sum=a+b
    print(sum)
    return sum
cal_sum(5,5)#function call;arguments

cal_sum(2,100)

#other
def cal_mul(a,b):
    return a*b
mul=cal_mul(5,10)
print(mul)'''


'''def printh():
    print("hello")
printh()
printh()'''

#avg of 3 num
'''def avg(a,b,c):
    return (a+b+c)/3
avg=avg(1,2,3)
print(avg)'''
'''def avg(a,b,c):
    sum=a+b+c
    avg=sum/3        #DLPR
    print(avg)
    return avg
avg(1,2,3)'''

'''cities=["warangal","kazipet","hanamkonda","hyderabad"]
heros=("superman","spiderman","batman","ironman","Hulk")
def lent(list):
    print(len(list))
lent(cities)
lent(heros)
'''
''' in single line
heros=("superman","spiderman","batman","ironman","Hulk")
def listt(list):
    for i in list:
        print(i,end=" ")
listt(heros)'''

# n=5
# fact=1
# for i in range(1,n+1): #1*2*3*4*5
#     fact*=i
# print(fact)

'''def print_fac(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
print_fac(5)
print_fac(4)'''


# n=5
# fact=1
# i=1
# while(i<=n):
#     fact*=i
#     i+=1
# print("factorial of 1-",n,"numbers:",fact)
'''def print_fact(n):
    i=1
    fact=1
    while(i<=n):
        fact*=i
        i+=1
    print(fact)
print_fact(5)'''

#usd-->INR  1usd->83inr,2usd->166inr
'''def converter(usd):
    inr_val=usd*83
    print(usd,"USD","->",inr_val,"INR")
n=int(input("enter the USD "))
converter(n)'''

#recursion (fun calls itself) ==loops

'''def show(n):
    if(n==0):    #base case (stop or not)
        return
    print(n)
    show(n-1)        #call itself in 
show(5)           #n=5,n-1->n=4,n-1->n=3,n-1->n=2,n-1->n=""0"" stop (return)'''

'''def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n
print(fact(5))'''

'''sum of natural numbers
def sum(n):
    if (n == 0):
        return 0
    else:
        return sum(n-1)+n
print(sum(5))'''


# def p_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     p_list(list,idx+1)
# lists=["mango","apple","mango","banana"]
# p_list(lists)




