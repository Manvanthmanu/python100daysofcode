#  decorators in python 
#  decorators are a special type of function which take another function as an argument and returns another function as a result


def greet(fx):
    def mfx(*args,**kwargs):
        print('good morning')
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print('hello world')

@greet
def add(a,b):
    print(a+b)

hello()
add(10,20)

