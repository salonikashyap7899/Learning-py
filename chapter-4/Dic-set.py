# # # Ḍictionsry and set in Python
# # # A dictionary is a collection of key-value pairs, where each key is unique.
# # # A set is an unordered collection of unique elements.  

# # # Creating a dictionary
# # my_dict = {
# #     'name': 'anu',
# #     'age': 20,
# #     'city': 'New York'
# # }
# # print("Dictionary:", my_dict)
# # # Accessing values in a dictionary
# # print("Name:", my_dict['name']) 


# # info = {
# #     "subject": ["Math", "Science", "English"],
# #     "topic": ("Python", "Java", "C++"),
# #     "name": "anu",
# #     "age": 20,
# #     "city": "New York"

# # }
# # print(info["name"])
# # print(info["subject"][0])  # Accessing first subject
# # print(info["topic"][1])    # Accessing second topic     


# # info["name"] = "rahul"  # Updating value
# # print("Updated name:", info["name"])
# # info["country"] = "USA"  # Adding new key-value pair
# # print("Added country:", info["country"])


# # nested disctionary

# student = {
#     "name": "anu",
#     "age": 20,
#     "marks": {
#         "math": 90,
#         "science": 85,
#         "english": 88
#     }
# }

# # print(list(student.keys()))
# # print(list(student.values()))
# # print(list(student.items()))
# # pairs = list(student.items())
# # print(pairs[0])

# # print(student["name2"]) #erros
# # print(student.get("name2")) #none

# # student.update({"city": "noida"})
# # print(student)

# # print("Student Name:", student["name"])
# # print("Math Marks:", student["marks"]["math"])  # Accessing nested dictionary value 



# # Creating a set
# # Set is the collection of the unordered unique elements each element in the set must be unique & ummutable

# # collection = {1, 2,2,3,4,5, 3, 4}
# # collection = set()
# # collection.add(1)
# # collection.add(2)
# # collection.add("saloni")
# # # collection.clear()
# # collection.pop()
# # # collection.remove(2)
# # print(len(collection))


# collection = {"hellow", "apna", "world", "coding", "python "}
# print(collection.pop())



# # print(collection)
# # print(type(collection))

  
# empty_set = set()
# # empty_set = {} # This creates an empty dictionary, not a set
# # print(type(empty_set))  # Output: <class 'set'>

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
# # print(set1.intersection(set2))  # Output: {3}



# dict = {
#     "table": ["a piece of furniture with a", "flat top and one or more legs"],
#     "cat": "a small animal"
# }
# print(dict["table"])
# print(dict["cat"])



# setofstd = {"python", "java", "c++", "python", "javascript", "java", "python","java", "C", "c++"}
# print(len(setofstd))
  

SubDict = {}
# x = int(input("enter phy : "))
# y = int(input("enter chem : "))
# z = int(input("enter math : "))

# SubDict.update({"phy": x, "chem": y, "math": z})
# print(SubDict)


values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)


# values = {9, 9.0}
# print(values)