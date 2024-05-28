# ceaser cipher decription 

alphabets = "abcdefghijklmnopqrstuvwxyz"
numeric = '0123456789'


decript = input('please enter the decripting text : ')
rotatenum = int(input('number key to decript : '))

decrriptedList = []

for letters in decript:
        letterIndex = alphabets.find(letters)
        if(letters=='#'):
            newcode = ' '
            decrriptedList.append(newcode)

        elif(letters in numeric):
            numericIndex = numeric.find(letters)
            newcode= numeric[numericIndex-rotatenum]
            decrriptedList.append(newcode)
        
        else:
            newcode = alphabets[letterIndex-rotatenum]
            decrriptedList.append(newcode)
print(''.join(decrriptedList))
