#  try except 

def smoking():
    try:
        quit = input("what do u do with smoking : ")
        quit = quit.lower()
        if(quit!='quit'):
            raise ValueError(" sorry thats not the right ansewr")
        else:
            print('great')
            return 1

    except Exception as e:
        print(e)
        return 0
    finally:
        print('life is really beutyfull')
quit=smoking()
print(quit)

while(quit==0):
    print(smoking())
    smoking()
    quit=smoking()



