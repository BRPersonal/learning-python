def fib(n):  #Print fibnocci series
    a,b=0,1
    while a < n:
        print(a, end = ' ')
        a,b = b,a+b
    print()


def fib2(n):  #create fibnocci series as list and return it
    result=[]
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

#This will be executed only if this file is executed as a script and 
#will not be executed if used as imported module. When executed as 
#imported module, __name__ will be "fibo"
#eg., command line python fibo.py 50
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))