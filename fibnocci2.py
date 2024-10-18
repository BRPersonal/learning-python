#Ignore this file. refer fibo.py
#Note the multiple assignments
a,b= 0,1
while a < 10:
    #keyword end can be used to avoid printing a new line
    print(a,end=",")
    #Note how we avoid temp variable by smartly using multiple assignments
    #expresions in rhs are evaluated first before assignment take place
    #expressions are evaluated from left to right
    a,b = b,a+b

