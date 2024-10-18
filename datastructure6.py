#This is a short-hand version of datastructure5.py
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#Built-in function zip takes several iterables producing tuples with an item from each one
#* applied on a list unpacks it and converts it into a tuple
print("Is matrix a list?",isinstance(matrix,list))
print("Is matrix a tuple?",isinstance(matrix,tuple))

#Passing false for strict in zip function, allows
#creating tuple with least no. of columns among the rows
transpose = list(zip(*matrix,strict=False))

print("*matrix=",*matrix)
print(f"matrix={matrix}")
print(f"transpose={transpose}")



