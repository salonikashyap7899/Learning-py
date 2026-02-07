# file i/o

# python can be used to perform operations on files. The most common operations are reading from a file and writing to a file.

# types of files

# text files: these are files that contain human-readable characters. They can be opened and edited using a text editor. Examples of text files include .txt, .csv, .json, etc.
# binary files: these are files that contain data in a format that is not human-readable. They can only be opened and edited using a specific program that understands the format of the file. Examples of binary files include .jpg, .png, .pdf, etc.



# Open, read, & close File

# we have to open a file before reading or writing 


# f = open('demo.txt', "r")

# data = f.read()
# print(data)
# f.close()

# f = open('demo.txt', "w")
# data = f.write("Hello, this is a demo file.")
# print(data)
# f.close()

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)


# f = open('demo.txt', "w")

# f.write("\nThis is a new line added to the demo file.")
# f.close()




# f = open('demo.txt', "r+")
# f.write("This is a new line added to the demo file.")
# print(f.read())
# f.close()

# f = open('demo.txt', "w+")
# # f.write("This is a new line added to the demo file.")
# print(f.read())
# f.write("abc")
# f.close()





# charcter and meaning of I/O

# r: read mode - opens a file for reading. If the file does not exist, it raises an error.
# w: write mode - opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# a: append mode - opens a file for writing. If the file already exists, it appends data to the end of the file. If the file does not exist, it creates a new file.
# x: exclusive creation mode - opens a file for writing. If the file already exists, it raises an error. If the file does not exist, it creates a new file.
# b: binary mode - opens a file in binary mode. This is used for reading and writing binary files.
#+: update mode - opens a file for reading and writing. If the file does not exist, it creates a new file.
# t: text mode - opens a file in text mode. This is the default mode for
# opening files. It is used for reading and writing text files.


# with synatx

# from gradio_client import file


# with open('demo.txt', "r") as f:
#     data = f.read()
#     print(data)

# with open('demo.txt', "w") as f:
#     f.write("\nThis is a new line added to the demo file.")    


# Deleting a file
# using the os module 
# module like a copy library is a file witten by another programmer that generally has a function we can use .


# import os
# os.remove('sample.txt')




# f = open('practise.txt', "w+")
# f.write("python ")
# f.close()

# with open('practise.txt', "w") as f:
#     f.write("hi everyone\n we are learning file I/O\n")
#     f.write("using java.\n I like programming. in java")


# with open('practise.txt', "r") as f:
#     data  = f.read()
#     new_data = data.replace("java", "python")
#     print(new_data)
    

# with open('practise.txt', "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "python"
#     with open('practise.txt', "r") as f:
#        data  = f.read()
#        if(data.find(word) != -1):
#         print("word found")
#        else:       
#           print("word not found")
    

# check_for_word()


# def check_for_line():
#      word = "learning"
#      data = True
#      line_no = 1
#      with open('practise.txt', "r") as f:
#         while data:
#            data = f.readline()
#            if(word in data):
#               print(line_no)
#               line_no += 1
  
# check_for_line()





count = 0
with open('practise.txt', "r") as f:
    data  = f.read()
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
print(count)