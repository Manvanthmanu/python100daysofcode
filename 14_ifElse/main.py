# a=int(input('enter your age'))
# print('your age is ', a)


# conditional operators
# > , < , >= ,<= ,== , ! =


# ifelse

# if(a>18):
#     print('you can drive')
# else:
#     print('you cannot drive')

# if else if 
# budget = 200
# applePrice = 200

# if( budget - applePrice >0):
#     print(" Number is positive ")
# elif(budget - applePrice < 0):
#     print("number is negative ")
# else:
#     print('just buy')

# nested if else

num = 18 
if(num<0):
    print('number is negative')
elif(num>0):
    if(num<=10):
        print('number is between 1-10')
    elif(num>10 and num<=20):
        print('number is between 11 - 20')
    else:
        print('number is greater than 20')
else:
    print('number is zero')

