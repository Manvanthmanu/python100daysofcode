#  classes and objects

class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is an {self.occupation}")


a = Person()
a.name = "Shubham"
a.occupation = "Accountant"
# print(a.name,a.occupation)


b = Person()
b.name = 'Nitika'
b.occupation = "HR"

a.info()
b.info()