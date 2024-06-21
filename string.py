'''str="ok \n ok\n"
str2="point \t ok"
print(str,str2)
print(type(str))'''

'''# indexing
str="point"
print(str[0])
# slicing[start:skip:end]
print(str[2:5])
print(str[-3:-1])#backwards ,in'''

'''
# functions
str="hello iam nawaz"
print(str.endswith("az"))#true
print(str.capitalize()) #starting letter 
# print(str.replace("a","o")) 
print(str.find("o"))#index value
print(str.count("a"))#3 times 
'''


#practice
'''
name=input("enter Your name:")
print("lenght of your name is:",len(name))'''


# conditional statements
# if, eif,else

#1
''''
age=int(input("enter your age:"))
if(age<18):
    print(age,"is minor")
elif(age>18):
    print(age,"is major")
else:
    print(age,"is equal to major,minor")'''

#2
'''light=input("signal light color")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("fast")
else:
    print("get lost")'''

'''
#3
marks=int(input("Enter your Marks: "))
if(marks>=90):
    Grade="A"
elif(marks>=80):
    Grade="B"
elif(marks>=70):
    Grade="C"
elif(marks>=60):
    Grade="D"
else:
    print("fail")
print("the grade is-->",Grade)'''

#nesting
'''
age=int(input("age:?"))
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")'''

#2
'''
#odd or even
num=int(input("enter a num: "))
if(num%2!=0):
    print("ODD")
else:
    print("EVEN")  #num%2==0 (even) num div 2 and rem 0 
    '''
'''
#largest of 3 numbers
a=int(input("num1: "))
b=int(input("num2: "))
c=int(input("num3: "))
if(a>=b and a>=c):                         #and operation
    print(a,"num1 is greater")
elif(b>=c):
    print(b,"num2 is greater")
else:
    print(c,"num3 is greater")'''
'''
#4
#mutiple of 7
num=int(input("num"))
if(num%7==0):
    print("is mutiple of 7")
else:
    print("not a multiple of 7") '''