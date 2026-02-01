# # if-else statement

# age = 13

# if(age >= 18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# light = "red"
# if light == "green":
#     print("You can go.")
# elif light == "yellow":
#     print("Get ready to stop.")
# elif light == "red":
#     print("You must stop.")
# else:
#     print("Invalid light color.")


# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A+")
# elif marks >= 80 and marks < 90:
#     print("Grade A")
# elif  marks >= 80:
#     print("Grade B")
# elif marks >= 70 and marks < 80:
#     print("Grade C")
# elif marks >= 60 and marks < 70:
#     print("Grade D")
# else:
#     print("Grade F")


#  # nested if-else
# age = 34
# if(age>= 18):
#     if(age>= 80):
#         print("you can drive")
#     else:
#         print("you cannot drive")
# else:
#     print("you cannot drive")


num = int(input("Enter a number: "))
print(num % 2 == 0 and "Even" or "Odd")  

# find the greatest 3 number enteres by User
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a > b and a > c):
    print("a is greatest number", a)
elif(b > c):
    print("b is greatest number", b)
else:
    print("c is greatest number", c)

#  check if number is a multiple of 7 or not
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is a multiple of 7.")
else:
    print(f"{num} is not a multiple of 7.")