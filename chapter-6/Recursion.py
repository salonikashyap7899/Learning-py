# when a funtion calls itself, it is called recursion

# refucrsiive function

from operator import index


def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)   


def fact(n):
    if(n ==1 or n == 0):
        return 1
    return n * fact(n-1)
print(fact(5))


# calculate the sum of first n numbers using recursion

def sum_of_n(n):
    if(n == 0):
        return 0
    return n + sum_of_n(n-1)

print(sum_of_n(5))





def allChar(list, index):
    if index == len(list):
        return
    print(list[index])
    allChar(list, index + 1)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
allChar(fruits, 0)


# print all the even or odd number using recursion

def evnOd(a, b=10):
    a = int(input("enter a number: "))
    if a > b:
        return
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
    evnOd(a + 1, b)

evnOd(1)
   

