#  map # filter and # reduce functions

# def cube(x):
#     return x*x*x

# print(cube(2))

# l= [1,2,3,4,5,6]

# newl =[]
# for item in l:
#     newl.append(cube(item))

# print(newl)

# # map

# newl = list(map(cube,l))
# print(newl)


# # filter

# def filter_function(a):
#     return a>4
# newnewl = list(filter(filter_function , l))
# print(newnewl)

from functools import reduce
numbers = [1,2,3,4,5,6]

sum = reduce(lambda x,y:x+y ,numbers )
print(sum)