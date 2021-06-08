import turtle

sid = turtle.Turtle()
sid.speed("fastest")

 
#Add a straight black line as the road
sid.color("black")
sid.forward(500)
sid.left(180)
sid.forward(90) 

#Draw the first wheel
sid.penup()
sid.setposition(80,0)
sid.pendown()
sid.right(180)
sid.circle(30)

#Draw the second wheel
sid.penup()
sid.setposition(400,0)
sid.pendown()
sid.circle(30)

#Draw the line between the wheels. i.e. the bottom of the car
sid.penup()
sid.setposition(110,30)
sid.pendown()
sid.left(360)
sid.forward(266)

#Draw the lower body of the car
sid.penup()
sid.setposition(429,40)
sid.pendown()
sid.left(45)
sid.forward(50)
sid.left(45)
sid.forward(80)
sid.left(90)
sid.forward(470)
sid.left(75)
sid.forward(130)
sid.left(105)
sid.forward(92)

#Draw the upper half of the car
sid.penup()
sid.setposition(100,155)
sid.pendown()
sid.left(45)
sid.forward(130)
sid.left(315)
sid.forward(180)
sid.left(310)
sid.forward(128)

#Draw the inner square
sid.penup()
sid.setposition(120,45)
sid.pendown()
sid.left(50)
sid.forward(240)
sid.left(45)
sid.forward(60)
sid.left(45)
sid.forward(72)
sid.left(0)
sid.forward(30)
sid.left(50)
sid.forward(70)
sid.left(40)
sid.forward(130)
sid.left(40)
sid.forward(120)
sid.left(50)
sid.forward(114)

#Draw the partition between doors and windows
sid.penup()
sid.setposition(270,235)
sid.pendown()
sid.left(-1)
sid.forward(200)

#Draw the gas tank
sid.penup()
sid.setposition(430,130)
sid.pendown()
sid.left(0)
sid.forward(20)
sid.left(90)
sid.forward(20)
sid.left(90)
sid.forward(20)
sid.left(90)
sid.forward(20)
sid.left(90)

#Draw the front light1
sid.penup()
sid.setposition(2,100)
sid.pendown()
sid.left(90)
sid.forward(40)
sid.left(90)
sid.forward(20)
sid.left(90)
sid.forward(40)
sid.left(90)
sid.forward(20)
sid.left(90)

#Draw the front light2
sid.penup()
sid.setposition(-22,90)
sid.pendown()
sid.left(0)
sid.forward(20)
sid.left(90)
sid.forward(10)
sid.left(90)
sid.forward(20)
