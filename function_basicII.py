# countdown
#create a function that accpts a number as an input 
# def countdown(num): 
#     num_list=[]
#     for i in range (num,-1,-1):
#         num_list.append(i)
#     return(num_list)
# print(countdown(20))

# Print and return - 
# Create a function that will receive a list with two numbers. Print the first value and return the second. 
# def print_and_return(nums_list):
#     print(nums_list[0])
#     return nums_list[1]

# print_and_return([10,12])


# First Plus Length -- Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
# def first_list_length(num_list):
#     # first=num_list[0]
#     # length=len(num_list)
#     sum_of_first= num_list[0]+ len(num_list)
#     return (sum_of_first)

# print(first_list_length([1,4,5,6]))


# Values greater than second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list 
# def greater_than_second(originial_list):
#     new_list=[]
#     for i in range (len(originial_list)):
#         if originial_list[i] > originial_list[1]:
#             new_list.append(originial_list[i])
#     return new_list

# print(greater_than_second([1,45,7,23,54,67]))

# Write a function tthat accepts two integers as paramter : size and value 
# the function should create and return a list whose length is equal to the given size, and whose value are all the given value 
def thislength_thatvalue(size,value):
    new_list=[]
    for i in range (size):
        new_list.append(value)
    print(new_list)
    
thislength_thatvalue(3,7)
