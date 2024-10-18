def printRange(args):
    for i in range(*args):  #unpacking arguments from a list/tuple
        print(i, end=" ")
    print("")

list=[3,8,2] #range is 3 to 7 increment by 2
printRange(list)
list=[3,8]
printRange(list) #range is 3 to 7 increment by 1
    