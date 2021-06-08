import turtle
import time #this will freeze our code for a little while
from random import randint
from turtle import Turtle


t1 = turtle.Turtle('turtle')
t1.shape('turtle')
t2 = turtle.Turtle()
t2.shape('turtle')
t3 = turtle.Turtle()
t3.shape('turtle')
t4 = turtle.Turtle()
t4.shape('turtle')
t5 = turtle.Turtle()
t5.shape('turtle')


#------------------------------------------#
#Creating the racetrack
t = turtle.Turtle()
t.speed(100)
t.up()
t.goto(-150, 160)
t.write("TURTLE RACE", font = ("Arial", 30, "bold"))
colors = ["red", "blue", "green", "purple","gold"]
i = 0
while i<5:
  t.up()
  t.goto(-150,150-(100*i))
  t.setheading(0)
  t.color("black", colors[i])
  t.down()
  t.begin_fill()
  t.fd(600)
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(600)
  t.end_fill()
  i+=1
t.rt(90)
t.fd(5*100)
t.rt(90)
t.fd(100)
t.rt(90)
t.pensize(3)
t.fd(5*100)
t.hideturtle()
#------------------------------------------#


#------------------------------------------#
#Setting the initial positions of the turtles
t1.up()
t1.speed(0)
t1.color("white")
t1.goto(-150,100)
t1.write("Turtle 1", font = ("Arial", 15, "bold"))
t1.goto(-55,100)

t2.up()
t2.speed(0)
t2.color("white")
t2.goto(-150,0)
t2.write("Turtle 2", font = ("Arial", 15, "bold"))
t2.goto(-55,0)

#Do it yourself, Just like, t1 and t2, set the positions of t3,t4 and t5. You only need to subtract 100 from the y position.

#Write code here
t3.up()
t3.speed(0)
t3.color("white")
t3.goto(-150,-100)
t3.write("Turtle 3", font = ("Arial", 15, "bold"))
t3.goto(-55,-100)
t4.up()
t4.speed(0)
t4.color("white")
t4.goto(-150,-200)
t4.write("Turtle 4", font = ("Arial", 15, "bold"))
t4.goto(-55,-200)
t5.up()
t5.speed(0)
t5.color("white")
t5.goto(-150,-300)
t5.write("Turtle 5", font = ("Arial", 15, "bold"))
t5.goto(-55,-300)

#------------------------------------------#
#The count-down 
time.sleep(1) #pause the game for 1 second
t6 = turtle.Turtle()
t6.hideturtle()
t6.color("white")
t6.up()
t6.goto(130, -120)
t6.write("3", font = ("Arial", 30, "bold"))
time.sleep(1)
t6.clear()
t6.up()
t6.goto(130, -120)
t6.write("2", font = ("Arial", 30, "bold"))
time.sleep(1)
t6.clear()
t6.up()
t6.goto(130, -120)
t6.write("1", font = ("Arial", 30, "bold"))
time.sleep(1)
t6.clear()
t6.up()
t6.goto(130, -120)
t6.write("GO!", font = ("Arial", 30, "bold"))
time.sleep(1)
t6.clear()
#------------------------------------------#

winner = ""
j = 0
while j < 500:
 #Start Coding here!
 t1.fd(randint(1,7))
 t2.fd(randint(1,7))
 t3.fd(randint(1,7))
 t4.fd(randint(1,7))
 t5.fd(randint(1,7))

 #Announcing the Winner
 if (int(t1.xcor())>=440):
   winner = "Turtle 1"
   break
 elif (int(t2.xcor())>=440):
   winner = "Turtle 2"
   break
 elif (int(t3.xcor())>=440):
   winner = "Turtle 3"
   break
 elif (int(t4.xcor())>=440):
   winner = "Turtle 4"
   break
 elif (int(t5.xcor())>=440):
   winner = "Turtle 5"
   break
 else :
   winner = ""
 j = j+1

#Clearing up the screen to announce the winner
t.reset()
t.hideturtle()
t1.reset()
t1.hideturtle()
t2.reset()
t2.hideturtle()
t3.reset()
t3.hideturtle()
t4.reset()
t4.hideturtle()
t5.reset()
t5.hideturtle()
t6.reset()
t6.hideturtle()
t6.write(winner + " is the winner!", font = ("Arial", 30, "bold"))
