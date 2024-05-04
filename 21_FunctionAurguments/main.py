# #  Function Aurguments 

# def average(a,b):
#     print('The avertage is ' , (a+b)/2)

# average(4,6)

# #  4 types of aurguments 

# #   Default values
# def average(a=9,b=1):
#     print('The avertage is ' , (a+b)/2)

# # Keyword aurguments

# average(b=9,a=21)

# # Required Aurguments
# def average(a,b=1):
#     print('The avertage is ' , (a+b)/2)
# average(b=9)

# # variable length aurguments

# def average(*numbers): # for numbers
#     for i in numbers:
#         sum = sum+i
#     print('Average is: ', sum / len(numbers))

# average(4,2,54,2,4,2,4,2,3)

def name(**name):
    print(type(name))
    print('hello' , name["fname"],
          name["mname"] , name["lname"])
    
name(mname = "Buchanna", fname="manvnanth" , lname = "kush")

# Return