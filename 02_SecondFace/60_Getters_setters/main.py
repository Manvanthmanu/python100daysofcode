#  getters and setters in python

class MyClass:
    def __init__(self,value):
        self.valuename = value

    def show(self):
        print(f"Value is {self.valuename}")


    @property
    def ten_value(self):
        return 10*self.valuename
    
    @ten_value.setter
    def ten_value(self,newvalue):
        self.valuename = newvalue/10

obj = MyClass(20)
obj.ten_value = 89
# print(obj.ten_value)
obj.show()