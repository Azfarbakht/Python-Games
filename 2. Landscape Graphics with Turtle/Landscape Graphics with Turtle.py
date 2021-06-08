import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed("fastest")

screen.setup(610,440)
screen.bgcolor("light blue")
pen.speed("fastest")


#Drawing the Sun!
pen.setheading(0)
pen.fillcolor("yellow")
pen.penup()
pen.goto(-320,130)
pen.pendown()
pen.begin_fill()
pen.circle(100)
pen.end_fill()

#Drawing the clouds
pen.setheading(90)
pen.fillcolor("white")
pen.penup()
pen.goto(250,120)
pen.pendown()
pen.begin_fill()
pen.color("white")
for x in range(10):
  pen.circle(20)
  pen.right(36)
  pen.forward(10)
pen.end_fill()
pen.setheading(90)

#Drawing the clouds again
pen.setheading(90)
pen.fillcolor("white")
pen.penup()
pen.goto(75,140)
pen.pendown()
pen.begin_fill()
pen.color("white")
for x in range(10):
  pen.circle(20)
  pen.right(36)
  pen.forward(10)
pen.end_fill()
pen.setheading(90)


#Drawing Grass
pen.setheading(90)
pen.fillcolor(5,114,3)
pen.penup()
pen.setheading(90)
pen.goto(-310,-300)
pen.begin_fill()
for x in range(2):
  pen.forward(150)
  pen.right(90)
  pen.forward(610)
  pen.right(90)
pen.end_fill()

#Drawing House
#Drawing House Outline
pen.color(0,0,0)  
pen.penup()
pen.goto(-301, -150)
pen.pendown()
pen.setheading(90)
pen.fillcolor("white")
pen.begin_fill()
pen.forward(150)
roof1=pen.position()
pen.right(90)
pen.forward(250)
roof2 = pen.position()
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.end_fill()
  
#roof
pen.penup()
pen.goto(roof1)
pen.fillcolor(244, 131, 66)
pen.begin_fill()
pen.pendown()
pen.goto(-180, 61)
pen.goto(roof2)
pen.goto(roof1)
pen.end_fill()
pen.setheading(90)

#door
pen.penup()
pen.goto(-223, -150)
pen.color("black", "red")
pen.begin_fill()
pen.setheading(90)

for x in range(2):
  pen.forward(50)
  pen.right(90)
  pen.forward(30)
  pen.right(90)

pen.end_fill()

  #handle
pen.color("black","black")
pen.penup()
pen.goto(-212, -150+20)
pen.begin_fill()
pen.circle(4)
pen.end_fill()
pen.hideturtle()

#This function will allow you to click anywhere on the screen and get the exact x and y coordinates of that position.
def tap(x,y):
  print(x,y)
screen.listen()
screen.onclick(tap)