# ceaser cipher encription
alphabets = "abcdefghijklmnopqrstuvwxyz"
numeric = '0123456789'


encript = input('please put a text to encrypt : ')
rotatenum = int(input('number to change places with :'))


encriptedlist = []
try:
    for letters in encript:
        letterIndex = alphabets.find(letters)
        if(letters==' '):
            newcode = '#'
            encriptedlist.append(newcode)
        elif(letters in numeric):
            numericIndex = numeric.find(letters)
            if(numericIndex+rotatenum >len(numeric)-1):
                errorcontrol = ( numericIndex + rotatenum) - (len(numeric)-1)
                newcode = numeric[errorcontrol-1]
                encriptedlist.append(newcode)
            else:
                newcode= numeric[numericIndex+rotatenum]
                encriptedlist.append(newcode)

        else:

            if(letterIndex+rotatenum > len(alphabets)-1):
                errorcontrol = (letterIndex+rotatenum) - (len(alphabets)-1)
                newcode=alphabets[errorcontrol-1]
                encriptedlist.append(newcode)

            else:

                newcode = alphabets[letterIndex+rotatenum]
                encriptedlist.append(newcode)
except Exception as e:
    print(e)
print(''.join(encriptedlist))



# list_variable = ['Hello', 'World']
# str_variable = ''.join(list_variable)
# print(str_variable)  # output: "Hello World"