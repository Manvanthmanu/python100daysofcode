#  finally clause 

try:
    l = [ 1,3,4,6]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print('Some error occcured')


finally:
    print("I am always executed")