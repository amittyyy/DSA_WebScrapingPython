myCat = {'size' : 'fat', 'color' : 'gray', 'age' : '28'}

print(myCat)
print(myCat.keys())
print(myCat.values())
print(myCat['size'])
print(list(myCat.items()))

isAvail = 'size' in myCat

if 'gender' not in myCat :
    myCat['gender'] = 'Female'

print(myCat)
print(isAvail)