#To get position and value simultaneously while iterating a list
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print("-" * 10)
#To iterate over multiple lists simultaneously use zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print(f"what is your {q}?. It is {a}")
print("-" * 10)

#to iterate in reverse order
for i in reversed(range(1,5)):
    print(i)
print("-" * 10)

#To eliminate duplicates and sort 
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
print("-" * 10)


