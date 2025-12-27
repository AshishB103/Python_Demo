## While Loops ##

# count = 1
# while count<=5:
#     print("Hello")
#     count += 1

##print numbers from 5 to 1
# c = 5
# while c >= 1:
#     print(c)
#     c -= 1

##print numbers from 1 to 100
# x = 1
# while x <= 100:
#     print (x)
#     x += 1

##print multiplication table of any number
# n = int(input("Enter a number : "))
# y = 1
# result = n
# while y <= 10:
#     result = n * y
#     print ( n, "*" , y, "=", result)
#     y += 1

##print all the elements of a list using while loop
# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i <= (len(nums)-1):
#     print(nums[i])
#     i += 1

##Search for any number  from a tuple. Using BREAK keyword to end the loop when the number is found
# num2 = (1,4,9,16,25,36,49,64,81,100)
# idx = int(input("Enter a number: "))
# y = 0
# while y < len(num2):
#     if (num2[y] == idx):
#         print ("found at index", y)
#         break   #breaks the loop. Used to terminate the loop when encountered
#     else:
#         print("finding..")
#     y += 1
#
# print("End of Loop!")

##Print all odd numbers starting from 1 to 10
# i = 1
# while i < 10 :
#     if (i%2 == 0):
#         i += 1
#         continue #terminates execution in the current iteration & continues execution of the loop with the next iteration
#     print(i)
#     i += 1

##FOR Loop : Used for sequential traversal. For traversing list, strings, tuples etc
# str = "Thor: Ragnarock"
#
# for char in str:
#     if (char == "r"):
#         print("r found")
#         break  # break will come out of loop, and will not print else condition
#     print(char)
# else:
#     print("END")

#Print elements of the list using FOR loop
# lst = [1,4,9,16,25,36,47,64,81,100]
#
# for i in lst:
#     print(i)
# else:
#     print("END")

# #Search for a number in the list using FOR loop
# nums = [1,4,9,16,25,36,47,64,81,100]
# x = int(input("Enter a number: "))
# z = 0
# for n in nums:
#     if (x == n):
#         print ("The number is present in the list", z)
#     z += 1


#Range
# for i in range(5): #range(stop)
#     print(i)
# for i in range(2,10): #range(start,stop)
#     print(i)
# for i in range(2,10,3): #range(start,stop,step)
#     print(i)

##Print numbers from 1 to 100 using range
# for  i in range(101):
#     print(i)

##print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

##Print multiplication table of a number
# nums = int(input("Enter a number"))
# result = nums
# for i in range(1,11):
#     result = nums * i
#     print(nums,"*",i, "=",result)

#PASS statement in FOR loop
# for i in range(5):
#  pass  #used as a placeholder. prints null
# print("Some useful code")

##Print sum of 1st n numbers
# b = 5
# sum = 0
# for i in range(1, b+1):
#     sum += i
# print("The sum is ", sum)