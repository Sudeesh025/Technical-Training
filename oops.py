#oops
#class
'''class Student:
    name = "shah"     #same name for name

#object (instance)

s1=Student()
print(s1)       #address
print(s1.name)
'''

'''class Car:
    color="red"
    brand="suzuki"
vehicle=Car()
print(vehicle.brand)'''


'''class Student:
    college="abc College"                       #class attribute
    def __init__(self,name,marks):             #constructor   self--> pointing object
        self.name =name                      #variable assign
        self.marks=marks
        print("add db...")                     #constructr
    # name = "shah"

s1=Student("shah",23)   #fullname address                # s1=Student()
print(s1.name,s1.marks)                                                 # print(s1)

s2=Student("nawaz",56)
print(s2.name,s2.marks)             #object attributes
print(s1.college)
print(student.college)               #class attribute
'''


'''class Car:
    def __init__(self,brand,color,cost):
        self.brand=brand
        self.color=color
        self.cost=cost
        print("car details")

car1=Car("suzuki","red",99)
print(car1.brand,car1.color,car1.cost)'''


#methods
'''
class Student:
    college="abc College"
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
        print("add db...")

    def get_marks(self):
        return (s1.marks)              #method
    def example(self):
        print("method example")

#object
s1=Student("shah",23)
print(s1.get_marks())                  #
s1.example()'''


'''class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def avg(self):
        return (self.sub1+self.sub2+self.sub3)/3

s1=Student("shah",99,100,100)
print(s1.name,s1.sub1,s1.sub2,s1.sub3)
print(s1.avg())'''


'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod             # static method-->decorator
    def hello():
        print("hello")
    def avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi!",self.name,"your avg marks are:",sum/3)

s1=Student("shah",[99,100,100])
print(s1.name,s1.marks)
# print(s1.avg())
s1.avg()
s1.hello()'''


class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    def debit(self,amount):
        self.balance-=amount
        print("Debited rupess:",amount)
        print("total balance=",self.total())
    def credit(self,amount):
        self.balance+=amount
        print("Credited rupess:",amount)
        print("total balance=", self.total())
    def total(self):
        return self.balance

acc1=Account(1000,786)
acc1.debit(500)
acc1.credit(400)
acc1.debit(100)
acc1.credit(200)
#print(bank.balance,bank.acc_no)