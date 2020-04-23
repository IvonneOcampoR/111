print('Hello World')

name = 'Ivonne'
lats_name = 'Ocampo'
age = 23
found = False
average = 21.78

print(name)
print(lats_name)
print(age)
print(found)
print(average)

print(21 + 21)
print(age - 1)
print(78 * 121)
print(123 / 32)
print(10 % 3) # % = modulus operator (returns theresidue of the division)

def test():
    print("inside the fn")
    print("this too")
    
def separator():
    print('-----------------')

test()

separator()

print(name + lats_name)
print(name + str(23)) #str converts number into a string

separator()

if(age < 90):
    print('You are young')
elif(age == 90):
    print('You are on the border of life')
else:
    print('Sorry bud, you are getting old')
