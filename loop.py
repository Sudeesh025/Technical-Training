#loops-->for,while
#while

''' hello*5
count=1
while count<=5:         #until its #true
    print("hello")
    count+=1             #count=count+1    ->1,2,3,4
print(count)          #6 stops  #false


i=1                    #iterates/iterator--> count,i,j,k,x,y
while(i<=3):            #itaration (loop)
    print("again",i)
    i+=1                    #4th stops
'''
''' //1-5
i=1
while i<=5:
    print(i)
    i+=1                #+1  1,2,3,4,5

//5-1

i=5
while i>=1:
    print(i)
    i-=1               #-1   5,4,3,2,1
'''

'''
#5*1=5,5*2=10

j=int(input("enter the number: ")) 
i=1                          #start 1     change
while(i<=10):                #stop 10      1-10
    print(j,"*",i,"=",j*i)      
    i+=1                       #5*1=5,5*2=10
'''

''' traverse
#print(list[0])-----print(list[z])

list=["shaktiman","powerrangers","Spiderman","superman","batman"]
#list=[1,4,9,16,25,36,49,64,81,100]
i=0      # i=list[0]   index
while(i<=len(list)-1):
    print(list[i])                     #print(list[0])-----print(list[z])
    i+=1
'''
'''
#search(linear aearch)
x=36
tuple=(1,4,9,16,25,36,49,64,81,100)
i=0
while(i<len(tuple)):
    # print(tuple[i])
    if(tuple[i]==x):
        print(x,"is available at index",i)
    # else:
    #     print(x,"is not available finding...")                  #checking
    i += 1
'''
'''
find="pizza"
fruits=("orange","grapes","pizza","mango","banana")
i=0      #index
while(i<len(fruits)):     #till len of fruits
    if(find==fruits[i]):      
        print(find,"is found at index",i)
    i+=1              #next
'''
'''
#break
i=1
while(i<=10):   
    if(i==5):
        break    #1>2>3>4>break
    print(i)
    i+=1'''
'''

#continue(skip)
i=1
while(i<=5):
    if(i==3):
        i += 1
        continue  #1>2> >4>5
    print(i)
    i+=1
'''
'''
#skip even num
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1 '''


#for(sequential traversal)
'''
nums=[1,2,3,4,5]
veg=("cabbage","tomato","carrot","spinach")
for val in nums:
    print(val)
for i in veg:
    print(i)'''

'''num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)'''

'''
find=25
num=(1,4,9,16,25,36,49,64,81,100)
for i in num:
    if(i==find):
        print(i,"is found")'''

'''
find=25
inx=0
num=(1,4,9,16,25,36,49,64,81,100)
for i in num:
    if(i==find):
        print(i,"is found at index",inx)
    inx+=1'''

#range(start?,stop,step?)      ?optional
'''seq=range(2,10,2)
for i in seq:
    print(i)'''
'''print("even numbers")
for i in range(2,20,2):
    print(i)'''

'''for i in range(8,0,-1):
    print(i)'''

#sum of n numbers 1+2+3+4+5
'''
n=5
sum=0
for i in range(1,n+1):
    sum+=i #sum=sum+i
    #print(sum)
print("sum of 1-",n,"numbers:",sum)'''
#using while
'''n=5
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print("sum of 1-",n,"numbers:",sum)'''

#factorial 1*2*3*4*5
'''n=5
fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print("factorial of 1-",n,"numbers:",fact)'''

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial=",fact)



#prime-> divisible by 1 and itself
n=int(input())
for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break
else:
    print("prime")

