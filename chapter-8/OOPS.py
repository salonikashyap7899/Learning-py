# OPPS
# del keyword
# used to delete object properties or object itself
# OOPS - del keyword & private attributes

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("saradha")
print(s1.name)

# del s1.name
# print(s1.name)   # This will raise AttributeError


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   # private attribute

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12334", "abcd")
print(acc1.acc_no)
acc1.reset_pass()


# # Private(like) attributes & methods 
# # Conceptual implementations in python
# # Private atttributes & methods to be used only within the class and are not accessible from outside the class

class Person:
    _name = 'annoymous'
 
    def _hello(self):
        print("hello person")

    def Welcome(self):
        self._hello()

p1 = Person()
print(p1.Welcome())



# Ineritance
# when one  class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    color = "balck"
    @staticmethod
    def Start():
        print("start car")

    @staticmethod
    def Stop():
        print('stop car')   

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.Start())

# types of inheritence
# Single Inheritence
# multi-lebel Inheritence
# multiple Inheritence


# # multi-lebel Inheritence
class Car:
    color = "balck"
    @staticmethod
    def Start():
        print("start car")

    @staticmethod
    def Stop():
        print('stop car')   

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        


car1 = Fortuner("diesel")
car1.Start()


class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to Class B"
class C(A,B):
     varC = "welcome to class C"

c1 = C()
print(c1.varC)         
print(c1.varA)         
print(c1.varB)         


# Super Methods
# super() method is used to access  methods of the parent class

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print('car stop')    
    def stop():
        print("car start")   

class ToyotaCar(Car):
    def __init__(self, name, type ):
        super().__init__(type)
        self.brand = name 
        super().Start()



car1 = ToyotaCar('prius', "electric")
print(car1.type)



# class methods
# A class methods is bound to the class & receives the class as an implicit first arguments 
# note - static methods can't access or modify class state & generally for utility

class Person:
    name = "annonymous"

    # def changeName(self, name):
    #     self.name = name
    #     # Person.name= name
    @classmethod
    def changeName(cls, name):
        cls.name = name
     #class method

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(p1.name)        



# property
# we use @property decoreter on any method in the class to use te method as a property

class Student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def parcentage(self):
         return  str((self.phy + self.chem + self.math) / 3)  + "%"

 
stu1 = Student(98,97,99)
print(stu1.parcentage)

stu1.phy = 86
print(stu1.parcentage)


# Polymoriphism: Operatore Pverloading

# when the same operatore is allowed to have diffrent meaning according to the context 

# a + b
# a - b
# a * b
# a / b
# a % b

class Complex:
    def __init__(self, real, img):
        self.real = real 
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j" )
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal , newImg)
num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4,6)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()



class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
         return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self, role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDeatils(self):
        print("role = ", self.role)   
        print("dept = ", self.dept)   
        print("salry = ", self.salary)  

class Engineer(Employee):
    def __init__(self, name, age):
           self.name = name
           self.age = age
           super().__init__("Enginner", "IT", "75,000")

eng1 = Engineer("Elon Mask", 40)
eng1.showDeatils()


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__ (self, odr2):
        return self.price > odr2.price
       

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)      

print(odr1 > odr2)