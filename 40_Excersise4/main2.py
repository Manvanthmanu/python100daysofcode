#  descripting 

# text = input('Please type the text to decode : ')

# textstring = text.split(' ')

# mainlist = []

# for i  in textstring:
#     listit = []
#     for letters in i:
#         listit.append(letters)
#     if(len(listit) > 3):
#         for i in range(3):
#             listit.pop(0)
#         for i in range(3):
#             listit.pop(-1)
#         listit.insert(0,listit[-1])
#         listit.pop()
#     else:
#         listit=(listit[::-1])
#     mainlist.append(''.join(listit))

# print(' '.join(mainlist))
        


def encrypt_word(word):
  listit = list(word)
  print(listit)
  if len(listit) > 3:
    for i in range(3):
        listit.pop(0)
    for i in range(3):
        listit.pop(-1)
    listit.insert(0,listit[-1])
    listit.pop()
  else:
    listit.reverse()
  return ''.join(listit)


def encrypt_text(text):
  textstring = text.split(' ')
  mainlist = [encrypt_word(word) for word in textstring]
  return ' '.join(mainlist)


# Example usage
text = "kvzellohvus mpqherettvu sti em"
encrypted_text = encrypt_text(text)
print(encrypted_text)
