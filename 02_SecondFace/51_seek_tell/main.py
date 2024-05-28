#  seek and tell 

# with open('51_seek_tell/text.txt' , 'r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.read(3))

with open('51_seek_tell/text3.txt' , 'w') as f:
    print(type(f))
    f.write('hello this is new')
    f.truncate(10)
    s =open('51_seek_tell/text3.txt' , 'r')
    
    print(s.read())