# # List of student names

# # a built-in data type that stores set of value it can store elements of different data types(integer, flaot , string , etc)
marks = [93.4, 85.6, 78.2, 88.9, 91.3]
print("Marks:", marks)
print("Type of marks:", type(marks))
print("Number of marks:", len(marks))
print("First mark:", marks[0])
print("Last mark:", marks[1])

std = ["karan ", 94.5, 17, "delhi"]
print(std[0])
std[0] = "rahul"
print(std)

# # list in slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:5])  # Output: [30, 40, 50 ]
print(numbers[:4])   # Output: [10, 20, 30, 40]
print(numbers[5:])   # Output: [60, 70, 80, 90]
print(numbers[-3:])  # Output: [70, 80, 90]
print(numbers[:-4])  # Output: [10, 20, 30, 40, 50]

# list methods
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an element to the end of the list
print("Fruits after append:", fruits)
fruits.remove("banana")  # Removing an element from the list
print("Fruits after remove:", fruits)
fruits.sort()            # Sorting the list
print("Fruits after sort:", fruits)
print(fruits.sort(reverse=True))  # Sorting in descending order
fruits.reverse()         # Reversing the list
print("Fruits after reverse:", fruits)
fruits.insert(1, "kiwi") # Inserting an element at a specific position
print("Fruits after insert:", fruits)
fruits.pop()             # Removing the last element
print("Fruits after pop:", fruits)
fruits.clear()           # Clearing the list
print("Fruits after clear:", fruits)
print("Length of fruits list:", len(fruits))


char = ['a','c','r','w','b','f','g','s']
char.append('z')
char.sort()
char.sort(reverse=True)
char.reverse()
char.insert(2,'z')
char.remove('g')
char.pop(2)
print(char)
        

# # Tuple of student details
# # A  built-in data types that lets us create immutable squence of values
 
tup = (2,3,4,56,7,8,9,0,)
print("Tuple:", tup)
print("Type of tup:", type(tup))
print(tup[2])
print(tup[4])

tup = (1,) # single element tuple 
tup2 = (1) # not a tuple
print(type(tup2))  # type(int)
print(tup)
print(type(tup)) # type(tup)

# # slicing in tuple
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(numbers[2:5])  # Output: (30, 40, 50
print(numbers[:4])   # Output: (10, 20, 30, 40)
print(numbers[5:])   # Output: (60, 70, 80, 90)
print(numbers[-3:])  # Output: (70, 80, 90) 
print(numbers[:-4])  # Output: (10, 20, 30, 40, 50)
# tup[0] = 100 # this will raise an error as tuple is immutable

# # tuple methods
tup = (5, 2, 9, 1, 5, 6)
print("Count of 5 in tuple:", tup.count(5))  # Counting occurrences of an element
print("Index of 9 in tuple:", tup.index(9))    # Finding the index of an element    
 

movieList = []  # empty list
movie1 = input("Enter your first favorite movie name: ")
movie2 = input("Enter your second favorite movie name: ")
movie3 = input("Enter your third favorite movie name: ")
print("Your favorite movies are:", movie1, movie2, movie3)
movieList.append(movie1)    
movieList.append(movie2)
movieList.append(movie3)
print("Movie list:", movieList)


# check if a list contains a palindrome of elements
list = [1,2,1,3]

copy_list = list.copy()
copy_list.reverse()

if list == copy_list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")   
 


grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))  # Output: 3
grade.sort()
print(grade)             # Output: ['A', 'A', 'A', 'B', 'B', 'C', 'D']
