#  error handling in python 

a = input("enter the number : ")

print(f"multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some imp lines of code")
print("End of program")


try:
    num = int(input("enter an integer : "))
    a = [6,3]
    print(a[num])
except ValueError:
    print('Number entered is not an integer')
except IndexError:
    print("entered index is not in list")
except Exception:
    print(Exception)