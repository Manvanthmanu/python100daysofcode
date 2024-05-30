#  snake water gun 2 
import random as rd

dict1 = {
    's': 0,
    'w': 1,
    'g': 2
}
dict2 = {
    0:'Snake',
    1:'Water',
    2:'Gun'

}


def userValidation(userInput):
    if(userInput in dict1):
        return(dict1[userInput])
    else:
        return('please enter a valid input : ')

def Logicfunction(computerInput , userInput):
    if(userValidation(userInput)==0):
        if(computerInput == 0):
            return('Draw')
        elif(computerInput == 1):
            return('Win')
        else:
            return('Loose')
    elif(userValidation(userInput)==1):
        if(computerInput==0):
            return('Loose')
        elif(computerInput==1):
            return('Draw')
        else:
            return('Win')
    else:
        if(computerInput==0):
            return('Win')
        elif(computerInput==1):
            return('Loose')
        else:
            return('Draw')
            
def MainFunction(computerInput):
    userInput = input('choose it snake water or gun  , s,w,g : ')
    LogicFunctionOutput = Logicfunction(computerInput , userInput)
    if(LogicFunctionOutput == 'Win'):
        print(f'\nyou choose {dict2[dict1[userInput]]} and the computer choose {dict2[computerInput]} so its a {LogicFunctionOutput}')
        return 1
    elif(LogicFunctionOutput =='Loose'):
        print(f'you choose {dict2[dict1[userInput]]} and the computer choose {dict2[computerInput]} so its a {LogicFunctionOutput}')
        return 0
    else:
        print(f'you choose {dict2[dict1[userInput]]} and the computer choose {dict2[computerInput]} so its a {LogicFunctionOutput}')
        return 0.5

def Looper():
    count =int(input('Please Enter the number of times u wanna play : '))
    score = 0
    for i in range(count):
        computerInput = rd.choice([0,1,2])
        score = score + MainFunction(computerInput)
        print(f'your Score is : {score} \n\n')
    print(f'Your total score is {score}')

Looper()