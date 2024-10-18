for n in range(10):
    for x in range(2,n):
        if ((n % x) == 0):
            print (n, "is not a prime because it equals", x,"*",n // x)  #double back-slash in integer division
            break #break makes sure that else will not be executed for the inner for-loop
    else:  #Note that this else belongs to inner for-loop and not the inner if-block
        print(n," is a prime")


