#  global and local variables . 

x = 4
print(x)


def hello():
    x = 5
    print(f'The local x is {x}')
    print('hello harry')

print(f"The global x is {x}")
hello()