# #  strings
str1 = "Hello"
str2 = 'World'  
str3 = """This is a multi-line
string example."""

print(str1)
print(str2) 
print(str3)


str1 = "Hello"
str2 = "world-saloni "
print(len(str1))  # Length of the string
print(len(str2))  # Length of the string

final_string = str1 + " " + str2
print(len(final_string))  # Length after Concatenation
print(final_string)  # Concatenation




str = "HelloWorld!"
#  print(str[0])      # First character
#  print(str[5])      # Eighth character


# slicing
print(str[1:5])     # Last character
print(str[:7])      # First five characters
print(str[7:])      # Characters from index 7 to end
print(str[-5:-2])  # Negative indexing


str = "i am learning Python programming  am language."
print(str.endswith("language."))  # Check if string ends with "language."
str = str.capitalize()
print(str)  # Capitalize the first character

str = str.replace("Python", "Java")
print(str)  # Replace "Python" with "Java"

str = str.find("Java")
print(str)  # Find the index of "Java" in the updated string


str = input("Enter a string: ")
print(len(str))

str = "find $ accurance of the word $ in this $ string" 
str = str.count("$")
print(str)  # Count occurrences of "$" in the string