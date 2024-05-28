#  complex case 
import random



quetionlist = ['In what year did the Great October Socialist Revolution take place?' ,
               'What is the largest lake in the world?',
               'Which planet in the solar system is known as the “Red Planet”?',
               'Who wrote the novel “War and Peace”?',
               'What is the capital of Japan?',
               'Whats my name?'
               ]

optionsList = [[1917,1923,1914,1920] , ['Caspian Sea','Baikal','Lake Superior','Ontario'] , ['Venus','Earth','Mars','Jupiter'] , ['Anton Chekhov ' , 'Fyodor Dostoevsky','Leo Tolstoy','Ivan Turgenev'] , ['Beijing','Tokyo','Seoul','Bangkok'] , ['manvanth' , 'kushi' , 'anu' , 'Aditya']]

AnswerList = ['a' , 'b' ,'c' ,'c' ,'b' ,'a']

optionchoice = ['A' , 'B' , 'C' , 'D' , 'a' , 'b' ,'c' ,'d']

randomlist = []
j = 0
for i in AnswerList:
    j = j+1
    randomlist.append(j)

# randomnum = 1
# print(randomnum)
# print(quetionlist[randomnum-1])

# j = 0
# displayoption = []
# for i in optionsList[randomnum-1]:
#     print(f"{optionList[j]}) {i}\n")
#     j = j+1



# price = 1000
# j = 0
# for i in quetionlist:
#     randomnum = random.choice(randomlist)
#     j = j+1
#     print(f'{j} ) - {quetionlist[randomnum-1]}\n')
#     k = 0
#     for i in optionsList[randomnum-1]:
#         print(f"{optionchoice[k]}) {i}")
#         k = k+1
#     answer = input('Ans : ')
#     if(answer == AnswerList[randomnum-1] or answer == AnswerList[randomnum-1].upper()):
#         price = price*10
#         print('Right Answer , congrats')
#         print(f'your price money is :{price}')
#     else:
#         if(j == 1):
#             price= price-1000
#         else:
#             price
#         print(f'\nWrong Answer!! , correct answer is {AnswerList[randomnum-1]}')
#         print(f'your price money is : {price}' )
#         break
#     randomlist.remove(randomnum)


    

        