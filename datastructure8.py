#Build a dictionary
tel = {'jack': 4098, 'sape': 4139}
print(tel['jack'])

#Accessing non-existing key will throw error
#print(tel['jill'])

tel['jill'] = 4127
print(tel['jill'])

#list keys
keys = list(tel)
print(f"keys={keys}")

#check for presence of key
print('jack' in tel)

#check for absence of key
print('bala' not in tel)

#dict() constructor builds dictionaries directly from sequences of key-value pairs
myDict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(myDict)

#dictionary comprehensions are also possible
myDict = {x:x**2 for x in (2,4,6)}
print(myDict)

#loop thru dictionary
for key,value in myDict.items():
    print(f"{key}={value}")

