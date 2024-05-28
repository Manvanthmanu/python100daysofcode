# Break statement

for i in range(12):
    print("5 X " , i+1, " = ",(i+ 1)*5)
    if(i==10):
        break

print("Loop ko Chodkar nikal gaya")

# continue 
# leaves iteration

for i in range(12):
    if(i==10):
        print('skip the iteration 10')
        continue
    print("5 X " , i , " = " , i*5)

#  do while loop emulation

i=0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break
