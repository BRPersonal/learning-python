from math import pi

vec = [-4, -2, 0, 2, 4]
filtered=[x for x in vec if x >= 0]
print(filtered)

#apply a function to all the elements 
fruits=["  banana", "apple  ", " grape "]
juices=[f.strip() for f in fruits]
print(juices)

#create list of 2 tuples - number and its square
tuple=[(x,x**2) for x in range(6)]
print(tuple)

#list comprehensions can contain complex expressions
piValues=[str(round(pi,i)) for i in range(1,6)]
print(f"piValues={piValues}")