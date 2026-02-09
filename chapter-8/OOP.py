# OOPs object oriented programming is a programming paradigm that uses objects and classes to structure code. It allows us to create reusable and modular code by organizing data and behavior into objects.

# to map with real world scenrio, we started using objects in code this is called object oriented programing 
# the self parameter is a reference to the current instance of the class and os used to access varibales that belongs to the class

class Student:
    #  deafult constructor
     def __init__(self, name, marks):
                pass
    #  parameterized constructor
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks
          print("This is the init`` function")

s1 = Student("anu", 95)  # creating an object of the class Student
print(s1.name, s1.marks)  # accessing the name and marks attributes of the object s1
s2 = Student("kashyap", 85)  # creating an object of the class Student
print(s2.name, s2.marks)  # accessing the name and marks attributes of the object s2






class Car:
     color = "blue"
     brand = "Toyota"
c1 = Car()  # creating an object of the class Car
print(c1.color)  # accessing the color attribute of the object c1
print(c1.brand)  # accessing the brand attribute of the object c1


# __init__ function
# All clases have a function called _init_(), which is always excetured when the class is being initated .




# Class & Instance Attributes
# Class.attr
# obj.attr

class Student:
     college_name = "ABC College"  # class attribute
     name = "anu rajput" # class attribute
     def __init__(self, name, marks):
          self.name = name #obj attribute > class attribute
          self.marks = marks
          print("This is the init`` function")

s1 = Student("saloni", 95)  # creating an object of the class Student
print(s1.name, s1.marks)  # accessing the name and marks attributes of the object s1


# methods
# Methos are functions that belongs to objects


class Student:
     college_name = "ABC College"  # class attribute
     name = "anu rajput" # class attribute
     def __init__(self, name, marks):
          self.name = name #obj attribute > class attribute
          self.marks = marks
          print("This is the init`` function")

     def welcome(self): #methods
          print("Welcome to ABC College", self.name)

     def get_marks(self):
          return self.marks

s1 = Student("saloni", 95)  # creating an object of the class Student
s1.welcome()  # calling the welcome method of the object s1
print(s1.get_marks())  # calling the get_marks method of the object s1 and printing the returned value





class Student():
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks
     @staticmethod
     def hello(): #  static methods
          print('hello')    

     def avg(self):
          sum = 0 
          for val in self.marks:
               sum += val 
          print("hi", self.name, "your avg score is : ", sum/3)    

s1 = Student("ayu", [99,98,97]) # accessing the name and marks attributes of the object s1
print(s1.avg())  # calling the avg method of the object s1 and printing the returned value





# Abstraction
# Hiding the implemetion deatails of a class and only showing the essential features to the user

class Car:
     def _init_(self):
          self.acc = False
          self.brk = False
          self.clutch = False
     def start(self):
          self.clutch = True
          self.acc = True
          print("car started")

car1 = Car()
car1.start()


# Encapusaltion
# wrapping data and fucntions into a single unit(object)

class Account:
     def __init__(self, bl, acc):
          self.balance = bl
          self.account = acc
     def debit(self, amount):
         self.balance  -= amount
         print("Rs.", amount, "was debited")
         print("total balamce  = ", self.get_balamce())
     def credit(self, amount):
         self.balance  += amount
         print("Rs.", amount, "was credited")
         print("total balamce  = ", self.get_balamce())
     def get_balamce(self):
          return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)