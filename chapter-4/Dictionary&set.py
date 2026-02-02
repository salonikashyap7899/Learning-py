# Ḍictionsry and set in Python
# A dictionary is a collection of key-value pairs, where each key is unique.
# A set is an unordered collection of unique elements.  

# Creating a dictionary
my_dict = {
    'name': 'anu',
    'age': 20,
    'city': 'New York'
}
print("Dictionary:", my_dict)
# Accessing values in a dictionary
print("Name:", my_dict['name']) 


info = {
    "subject": ["Math", "Science", "English"],
    "topic": ("Python", "Java", "C++"),
    "name": "anu",
    "age": 20,
    "city": "New York"

}
print(info["name"])
print(info["subject"][0])  # Accessing first subject
print(info["topic"][1])    # Accessing second topic     


info["name"] = "rahul"  # Updating value
print("Updated name:", info["name"])
info["country"] = "USA"  # Adding new key-value pair
print("Added country:", info["country"])


# nested disctionary

student = {
    "name": "anu",
    "age": 20,
    "marks": {
        "math": 90,
        "science": 85,
        "english": 88
    }
}

print("Student Name:", student["name"])
print("Math Marks:", student["marks"]["math"])  # Accessing nested dictionary value 


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
# Adding an element to a set    