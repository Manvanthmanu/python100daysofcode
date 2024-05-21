#  file handling in python 


#  reading a file 

# f = open('49_fileHandling/myfile2.txt', 'w')
# # print(f)
# f = open('49_fileHandling\\myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


# Writing to a file

# f = open('49_fileHandling\\myfile.txt' , 'a')
# f.write('Hello , world!')
# f.close()

with open('49_fileHandling\\myfile.txt' ,'a') as f:
    f.write("Hey I am inside with ")