name = "saloni"

namseshort = name[0:3] # slicing
print(namseshort)
charcter1 = name[0]
print(charcter1)

# sl
name1 = "anu"
print(name1) # repetition


a = 10
b = 20 

print(a+b) # addition



# relational operators with strings

a = 50
b = 20

print(a == b)
print(a != b)
print(a > b)    
print(a >= b) 
print(a < b)
print(a <= b)




# Assignment operators with strings

num = 10
num += 10  # equivalent to num = num + 10
num *= 2   # equivalent to num = num * 2
num -= 5   # equivalent to num = num - 5
num /= 5   # equivalent to num = num / 5
num %= 3   # equivalent to num = num % 3

print(num)

# Logical operators with strings
str1 = "hello"
str2 = "world"
print(str1 and str2)  # returns str2 because both are non-empty
print(str1 or str2)   # returns str1 because it's the first non-empty string
print(not str1)       # returns False because str1 is non-empty
print(not "")         # returns True because the string is empty
# Bitwise operators with strings (not applicable, will raise error if used)

a = 50 
b = 30

print ("AND operation:", (a == b ) and (a > b))  # Bitwise AND
print("OR operation:", (a == b ) or (a > b))  # Bitwise OR


# Type conversion

a = 2
b = 4.25

sum = a + b

print(sum)

#  type Casting

a = float("100")
b = 4.25

print(type(a))
print(a + b)



a = 3.14
b = str(a)
print(type(b))


input("Enter your name: ")
print("Welcome to Python programming!")

val = input("Enter some value: ")
print("The type of the input value is:", type(val))


int = ("4")
val = float(input("Enter a float value: "))
print(type(val), val)

name = input("Enter your name: ")
age = input("Enter your age: ")
marks = input("Enter your marks: ")

print("Name:", name)
print("Age:", age)
print("Marks:", marks)