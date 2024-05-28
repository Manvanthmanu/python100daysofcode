# # secret code language

# #  write a python program to translate a message into secret code language. use the rules below to translate normal english into secret code language

# #  coding 

# #  if the word contains atleast 3 characters , remove the first letter and append it at the end now append three random characters at the starting and the end 
# # else 
# # simply reverse the sting 

# # decoding

# #  if the word contains less than 3 characters , revverse it 
# # else:
# #  remove 3 random characters from start and end , now remove the last letter  and append it to the beginning
import random
alphabets = 'abcdefghijklmnopqrstuvwxyz'



    

text = input('Please type the text to encode : ')

textstring = text.split(' ')
# print(textstring)




mainlist = []


for i  in textstring:
    listit = []
    for letters in i:
        listit.append(letters)
    # print(listit)

    if(len(listit) > 3):
        listit.append(listit[0])
        listit.pop(0)
        for i in range(3):
            listit.append(random.choice(alphabets))
        for i in range(3):
            listit.insert(0,random.choice(alphabets))
    else:
        listit=(listit[::-1])
        # print(listit)

    mainlist.append(''.join(listit))
# print(mainlist)
print(' '.join(mainlist))

# import random
# alphabets = 'abcdefghijklmnopqrstuvwxyz'


# def encrypt_word(word):
#   listit = list(word)
#   print(listit)
#   if len(listit) > 3:
#     listit.append(listit[0])
#     listit.pop(0)
#     for _ in range(3):
#       listit.append(random.choice(alphabets))
#     for _ in range(3):
#       listit.insert(0, random.choice(alphabets))
#   else:
#     listit.reverse()
#   return ''.join(listit)


# def encrypt_text(text):
#   textstring = text.split(' ')
#   mainlist = [encrypt_word(word) for word in textstring]
#   return ' '.join(mainlist)


# # Example usage
# text = "This is a test string"
# encrypted_text = encrypt_text(text)
# print(encrypted_text)