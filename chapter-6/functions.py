# fucntion 
# block if statements that perform a specific task are often repeated in a program. To avoid this repetition, we can define a function that performs the task, and then call the function whenever we need to perform that task.

def  calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum


calc_sum(5, 10)
calc_sum(20, 10)
calc_sum(30, 10)

# fucntion defination 
def calc_sum(a,b): #parameters
    return a + b

sum = calc_sum(5, 10) #function call with arguments
print(sum)


def printHello():
    print("Hello")

printHello()
printHello()    


def avg_num(a,b,c):
    return (a + b + c) / 3
print(avg_num(10, 20, 30)) 


def avg_sum(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg
result = avg_sum(10, 20, 30)
print(result)


# TYPE OF function
# 1. function with no return type and no parameters
def greet():
    print("Hello, welcome to the program!")  


# default parameter value
# if we want to assign default values to the parameters, we can do so by assigning a value to the parameter in the function definition. If the caller does not provide a value for that parameter, the default value will be used.
def def_val(a = 20, b= 20):
    sum = a + b
    print(sum)
def_val() # using default values    



cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

def print_len(cities):
    print(len(cities))

print_len(cities)    



heroes = ["Superman", "Batman", "Wonder"]

def print_heroes(heroes):
    for item in heroes:
        print(item, end=" ")  # Print each hero with a space separator

print_heroes(heroes)       



n = 5 
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(fact) 
# print(factorial(n))

factorial(4)

 

def converter(usd_val):
    inr_val = usd_val * 82.5
    print(usd_val, "USD =", inr_val, "INR")

converter(1)


def OdEvn(n):
    n = int(input("enter a number: "))
    if n % 2 == 0:
        print(n, "is even")
    else :
        print(n, "is odd")

OdEvn(5)


