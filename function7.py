sortOption=int(input("Enter sort by (number - 0, words - 1):"))
pairs = [(1,'one'),(3,'three'),(2,'two'),(4,'four')]
pairs.sort(key=lambda pair:pair[sortOption]) #passing a lambda expression for sort 
print(pairs)