import turtle as t
t.position()  #initialize to co-ordinates 0,0
t.bgcolor("blue")
t.pencolor("orange")
t.pensize(8)
t.up()
#t.goto(-200,0)
t.down()

for _ in range(10):
    #with 5 strokes, angle 144 forms a star, 72 forms a pentagon
    #with 10 strokes, angle 36 forms a decagon
    for i in range(5):
        t.forward(200)
        t.right(144)
    t.right(36)

print("Diagram completed. Close the app")
t.hideturtle()
t.done()

