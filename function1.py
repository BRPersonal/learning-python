def fibnocci(n:int):
    #This is a docString - like a comment that explains what the function is 
    #doing. It is a good practise to include this in every function
    """Print a fibnocci series up to n"""
    
    a,b = 0,1
    while (a < n):
        print(a, end=" ")
        a,b = b,a+b
    print()

#call fibnocci function
fibnocci(2000)

