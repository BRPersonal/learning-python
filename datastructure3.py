tuple = [(x,y) for x in (1,2,3) for y in (3,1,4) if x != y]
print(tuple)

#This is equivalent but more verbose
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)