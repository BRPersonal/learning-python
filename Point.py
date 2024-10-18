def where_is(point):
    match point:
        case (0,0):
            print("Origin")
        case (0,y):
            print(f"Y={y}")
        case (x,0):
            print(f"X={x}")
        case (x,y):
            print(f"X={x}, Y={y}")  #'f' before string will replace placeholders with values
        case _:  #defalt fallback
            raise ValueError("Not a Point") #throw exception 
        
myTuple=(4,0)
where_is(myTuple)
