#  Recursion

#  factorial(7) =7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1

#  factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))


# f0 = 0
# f1 = 1
# f2 = f1+f0
# fn = fn-1 +f(n-2)

def febinachi(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return febinachi(n-1) + febinachi(n-2)
    
print(febinachi(6))