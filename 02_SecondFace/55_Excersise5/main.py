# snake water and gun using mathematics 

import random as rd

# 0 = snake , 1 = water , 2 = gun
AnswerMatrix = [['D','W','L'],['L','D','W'],['W','L','D']]



def userInputConvert(userInput):
    if(userInput == 's' or userInput == 'S'):
        return 0
    elif(userInput == 'w' or userInput == 'W'):
        return 1
    elif(userInput == 'g' or userInput == 'G'):
        return 2
    else:
        return 'Please input a valid option'
    
def userInputName(userInput):
    if(userInput == 's' or userInput == 'S'):
        return 'snake'
    elif(userInput == 'w' or userInput == 'W'):
        return 'water'
    elif(userInput == 'g' or userInput == 'G'):
        return 'gun'
    else:
        return 'Please input a valid option'
    
def computerAnswerConvert(cumputerAnswer):
    if(cumputerAnswer == 0):
        return 'Snake'
    elif(cumputerAnswer == 1):
        return 'Water'
    else:
        return 'Gun'

def convertMatrix(convert):
    if(convert == 'D'):
        return 0.5
    elif(convert == 'W'):
        return 1
    elif(convert == 'L'):
        return 0
    else:
        return None
    

def Mainfunction(cumputerAnswer):
    userInput = input("Snake , water , gun shoot -- s,w,g : ")
    userInput1 = userInputConvert(userInput)
    convert = AnswerMatrix[userInput1][cumputerAnswer]
    convert = convertMatrix(convert)
    print(f'The computer chooses {computerAnswerConvert(cumputerAnswer)} and you choose {userInputName(userInput)} its a {'Draw' if convert==0.5 else 'Lost' if convert==0 else 'Win' if convert==1 else 'None'}')
    print(convert)
    return convert


def looper():
    count = int(input('Please enter the times to play : '))
    score = 0
    for i in range(count):
        cumputerAnswer = rd.choice([0,1,2])
        score = score + Mainfunction(cumputerAnswer)
        print(f'your score is {score}')
    print(f'your final score is {score}')

looper()