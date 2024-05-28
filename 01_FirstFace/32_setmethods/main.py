s1 = { 1,2 ,3 ,4,5,6}
s2 = { 3,6,7}

# s1.union(s2)
# s1.update(s2)
# s1.intersection(s2)
# s1.intersection_update(s2)
print(s1,s2)

cities1 = {'Tokyo' , 'Madrid' , 'Berlin' , 'Delhi'}
cities2 = {'Tokyo' , 'Newyork' , 'Berlin' , 'Mumbai'}

# cities3 = cities1.symmetric_difference(cities2)
# cities3 = cities1.difference(cities2)

# print(cities3)

print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2))


# remove { error } / discard { no error }
# del
# clear