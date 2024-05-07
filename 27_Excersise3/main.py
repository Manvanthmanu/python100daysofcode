#  create a program capable of displaying quetions  to the user like kbc
#  use list data type to store the questions and their correct answers . 
# Display the final amount the person is taking home after playing the game. 


# kaun banega Carorepati

'''
1. Who is the Father of our Nation?
Answer: Mahatma Gandhi
2. Who was the first President of India?
Answer: Dr. Rajendra Prasad
3. Who is known as Father of Indian Constitution?
Answer: Dr. B. R. Ambedkar
4. Which is the most sensitive organ in our body?
Answer: Skin
5. Giddha is the folk dance of?
Answer: Punjab
6. Who was the first Prime Minister of India?
Answer: Jawaharlal Nehru was the first Prime Minister of India.
7. Which is the heavier metal of these two? Gold or Silver?
Answer: Gold
8. Who invented Computer?
Answer: Charles Babbage
9. 1024 Kilobytes is equal to?
Answer: 1 Megabyte (MB)
10. Brain of computer is?
Answer: CPU
11. India lies in which continent?
Answer: Asia
12. Which country are the Giza Pyramids in?
Answer: The Giza Pyramids are in Egypt.
13. What city is the statue of liberty in?
Answer: The statue of liberty is in New York City
14. How many Cricket world cups does India have?
Answer: India has two cricket world cups.
15. Martyrs’ Day is celebrated every year on?
Answer: 30th January
'''


# QuetionList = [""]
print(" There are 15 quetions , Choose A,B,C,D : each quetion increases 10% price ")
price = 1
optionList = ['A' , 'B' , 'C' , 'D' , 'a' , 'b' ,'c' ,'d']


def kbc(price):
    Answer1 = input("Who is the father of our Nation ? \nA) - Abdul kalam\nB) - Narendra Mode\nC) - Mahatma Gandhi\nD) - Javaharlaal Neharu\n Ans : ")
    if (Answer1 in optionList):
        if(Answer1 == 'C' or Answer1 == 'c'):
            price = price + ((price*10)/100)
            print(f'Correct Answer , your price amount is {price}')
        else:
            print(f'Opps wrong answer , your total win amount is : {price-1}')
    else:
        print('Please choose the right option')
        kbc(price)

kbc(price)




