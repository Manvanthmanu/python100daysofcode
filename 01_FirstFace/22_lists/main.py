#  lists 

l = [3,5,6] # numbered lists
marks = [3,5,6] # numbered lists

mixedlist = [2,4,1,'hello world', True,False,]
print(l)
print(type(l))



print(mixedlist[len(mixedlist)-3])


if '3' in marks:
    print( "yess")
else:
    print(
        'no'
    )

if "ma" in "manvanth":
    print('yes')


#  list comprehension

# lis = [ i for i in range(4)]

lis = [i for i in range(20) if i%2==0]
print(lis)