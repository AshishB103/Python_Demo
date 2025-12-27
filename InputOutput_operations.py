# x = open("demo.txt","r")
# # data = x.read()
# line1 = x.readline()
# print(line1)
# line2 = x.readline()
# print(line2)
# #print(data)
# #print(type(data))
# x.close()

# f = open("demo.txt","a")
# data = f.write("\nThis is a new line")
# f.close()

##Using WITH syntax. It automatically closes the file after operation

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

## importing OS library
# import os
# os.remove("demo.txt")

## creating a new file and adding contents to it.
# with open("practice.txt","w") as f:
#     f.write("This is Python tutorial\nThis is file I/O\n")
#     f.write("Using WITH clause\nNo need to use close command")

##Replace a string in the file
# with open("practice.txt", "r") as f:
#     data = f.read()
#
# new_Data = data.replace("Python", "Java")
# print(new_Data)
#
# with open("practice.txt", "w") as f:
#     f.write(new_Data)

# ##Check if a particular string is present in the file
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find("tutorial") != -1):
#         print("Found")
#     else:
#         print("Not found")

##find the first occurrence of a word in a file. If not found print -1:
# def check_for_line():
#     word = "file"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#
#     return -1
#
# print(check_for_line())

## Check for count of even numbers from a file
# count = 0
# with open("practice2.txt", "r") as f:
#     data = f.read()
#     print(data)
#
#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
#     print(count)
