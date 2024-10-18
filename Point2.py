#define a class
class Point:
    #constructor definition . first argument must be self - like this pointer
    __match_args__ = ('x', 'y')  #This line is important. Otherwise we get compilation error
    def __init__(self,x,y):
        self.x:int = x
        self.y:int = y

#Note how we explicitly specify argument type here. I prefer this 
#I dont like the idea of dynamic type inference. It is bullshit to me
#When you code , you exactly know the datatype and you code for that datatype only
#Then why the hell we should burden runtime to figure out the type?. 
def where_is(point:Point):
    match point:
        case Point(x,y) if ((x == y) and (x != 0)):  #You can add an if guard . if it is false match goes onto try next case block
            print("point is on the diagonal")
        case Point(x=0,y=0):
            print("Origin")
        case Point(x=0,y=y): #we match any point with x as 0 and y as any non-zero value
            print(f"Y={y}")
        case Point(x=x,y=0): #we match any point with x as any non-zero value and y as 0
            print(f"X={x}")
        case Point(x=x,y=y):
            print(f"X={x},Y={y}")
        case _:
            print("Not a point")

where_is(Point(1,5))
where_is(Point(0,0))
where_is((Point)(0,5))  #typecast
where_is((Point)(4,0))  #typecast
where_is((Point)("a","a")) #typecast
where_is(3)



    
