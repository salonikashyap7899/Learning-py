# # loops

# # loops are use to repeat instructions multiple times until a certain condition 

# # while loops


count = 1
while count <= 100 :
      print(count)
      count += 1  

count = 100
while count >= 1 :
      print(count)
      count -= 1  

# # print the multiplication table of a number n 
n = int(input("Enter a number: "))
i = 1
while i <= 10:
      print(n * i)
      i += 1

# # print the elements of the follwing list using while loop      
# # [1,4,9,16,25,36,49,64,81,100]

numbers = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(numbers):
      print(numbers[i])
      i += 1

# # search of a number x in this tuple using loop
#   [1,4,9,16,25,36,49,64,81,100]    

numbers = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0 
while i < len(numbers):
     if(numbers[i] == x):
      print("found at index ", i)
     i += 1


heroes = ["spiderman", "ironman", "thor", "hulk", "captain america"]
idx = 0 
while idx <= len(heroes):
     print(heroes[idx])
     idx += 1


# break statement and continue statement
# break: used to terminate the loop encountered
# continue: used to skip the current iteration and move to the next iteration


nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i =0 
while i  <= len(nums):
    if(nums[i] == x):
        print("found at index ", i)
        break
    else:
        print("not found at index ", i)
    i += 1 


i = 1
while i <= 10 :
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1


i = 1
while  i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1



# # for loops
veg = ["carrot", "broccoli", "spinach", "potato", "cabbage"]
for num in veg:
    print(num)


# for el in "python":
number = (1,4,9,16,25,36,49,64,81,100)
for num in number:
    print(num)
else:
    print("loop is ended")
   

str = "salonikashyap webdeveloper"
for char in str:
    if(char == 'a'):   
     print("found a in the string")
     break
    print(char)
 

num = [1,4,9,16,25,36,49,64,81,100]
for idx in num :
    print(idx)


num1 = (1,4,9,16,25,36,49,64,81,100)
x = 100
for idx in num1:
    if(idx == x):
        print("found ", x)
        break
    else:
        print("not found ", idx)


# range() function
#   range function returns a sequence of numbers , staring ffro 0 by default and increments by 1 by default and stops before a specified number


for num in range(5):
    print(num)

for i in range(2,10): #(start, stop)
    print(i)

for i in range(2, 20, 3): #(start, stop, step)
    print(i)



for i in range(2,100, 2):
    print(i)
for i in range(1,100, 2):
    print(i)


for i in range(1, 101):
   print(i)    
for i in range(100, 0, -1):
   print(i)    

n = int(input("enter a number: "))
# print the multiplication table of n
n = int(input("enter a number: "))
for i in range(1, 11):
    print(n * i)


# pass statement 
for el in range(5):
    pass
if el > 5:
    pass
print("loop ended")         
    # This loop does nothing because of the 'pass' statement, but it's syntactically valid.


# find the sum of the first n numbers. using while loops

n = 5
sum = 0 
for i in range(1, n+1):
    sum += i
    print("Sum is:", sum)

i = 1
while i <= n:
        sum += i
        i += 1
        print( sum)
      

n = 5 
fact = 1
for i in range(1, n+1):
        fact *= i 
        print("Factorial is:", fact)



n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
    

print("Factorial is:", fact)
