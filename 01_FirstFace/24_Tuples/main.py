tup = (1,3,5 ,"green",True,)
# tup1 = (1,)


print(type(tup) , tup)

print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])


def electro(): 
    if 3 in tup:
        return(3 in tup)
    else:
        return(3 in tup)

if(electro()==False):
    print('ha ha no')
else:
    print('no its there')