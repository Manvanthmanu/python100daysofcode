#  fstring
country = "india"
name = "Manvanth"

letter = " Hey my name is {} and I am from {}"
# print(letter)
print(letter.format(name,country))

print(f'Hey my name is {name} and i am from {country}')


txt = 'For only {price:} dollars!'

print(txt.format(price= 49.09999))

# {{}} double brackets to ignore variables
