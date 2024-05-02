# match case statements

age = int(input("please enter your age : "))

match age:
    case 1:
        print('you just born')
    case 2:
        print('he he')
    case _:
        print(age)
