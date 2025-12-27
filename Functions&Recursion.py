
#Function definition
# def calc_sum(a, b):  #parameters
#     return  a + b
# sum = calc_sum(1,2)   #function call, arguments
# print(sum)

# def print_Hello():
#     print("Hello")
#
# print_Hello()

#average of 3 numbers:
# def avg_num(a,b,c):
#     return (a + b + c)/3
#
# avg = avg_num(1,2,3)
# print(avg)

# function to return the len of list
# Cities = ["delhi", "gurgaon", "noida","pune","mumbai"]
# Heroes = ["thor", "ironman", "captain america","superman",]
# def list_len(list):
#     print(len(list))
# list_len(Cities)
# list_len(Heroes)

#function to print all elements of a list in a single line
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
#
# print_list(Heroes)

#Function to calculate factorial of a number;

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#          fact *= i
#     print(fact)
#
# cal_fact(5)


##function to convert USD to INR
# def converter(usd_val):
#     conv = usd_val * 91
#     print(usd_val,"dollar/s","=", conv, "rupee/s")
#
# converter(2)

# #function to find if the number is ODD or even
# def odd_even(n):
#     if n%2 == 0:
#         print("EVEN NUMBER")
#     else:
#         print("ODD NUMBER")
#
# odd_even(742)

##Recursive function
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)

##recursive function - factorial example
def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1) * n

print(fact(5))