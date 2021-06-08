#We have learnt so much about so far. We have seen what variables are and how we can store data in them. We have seen how we can reduce the lines in our code by writing loops and automating different parts of our project. Exlored conditionals. We have even learnt how to make a game.

#Importing Libraries
import turtle
import random
from random import randint

#Screen Commands
window = turtle.Screen()
turtle.tracer(0)

#Making Variables
boundary = turtle.Turtle()
player = turtle.Turtle()
charm = turtle.Turtle()
score = turtle.Turtle()
spawnc = False
points = 0
style = ('Courier', 30, 'italic')

#Making the Boundary
boundary.speed('fastest')
boundary.hudeturtle()
boundary.goto(0,0)
for i in range(4):
  boundary.fd(250)
  boundary.rt(90)
boundary.hideturtle()

#Spawning the Player
player.shape('turtle')
player.up()
player.goto(125,-125)
player.showturtle()

#Defining Functions
def forward():
  player.fd(10)
def backward():
  player.fd(-10)
def left():
  player.lt(10)
def right():
  player.rt(10)
def spawn(spawnc, charmx, charmy, charm):
  if spawnc == False:
    charm.showturtle()
    charm.up()
    charm.goto(charmx, charmy)
    charm.color('red')
    charm.shape('circle')
    spawnc = True
def clash(player, charmx1, charmy1, charm):
  if player.distance(charmx1,charmy1) < 15:
    return False
def scorehandling(points):
  score.clear()
  score.up()
  score.hideturtle()
  score.goto(0,20)
  point = str(points)
  score.write("Score : "+ point, style)


#Game Loop
while True:
  #We're constantly updating our game window so the screen refreshes and all new changes are visible.
  window.update()

  #Adding Movements to our turtle
  window.onkey(forward, "Up")
  window.onkey(backward, "Down")
  window.onkey(left, "Left")
  window.onkey(right, "Right") 
  window.listen()

  #Making Sure the turtle stays within boundaries
  if(int(player.xcor())<= 0):
    y = int(player.ycor())
    player.goto(1,y)
  if(int(player.xcor())>= 250):
    y = int(player.ycor())
    player.goto(249,y)
  if(int(player.ycor())>= 0):
    x = int(player.xcor())
    player.goto(x,-1)
  if(int(player.ycor())<= -250):
    x = int(player.xcor())
    player.goto(x,-249)

  #Randomizing the position of the Red Dot
  charmx = randint(10,240)
  charmy = -1 * randint(10,240)

  #Saving the Position of the Red Dot
  if spawnc == False:
    charmx1 = charmx
    charmy1 = charmy

  #Spawning the Circle and Detecting CLashes
  spawn(spawnc, charmx, charmy, charm)
  spawnc = clash(player, charmx1, charmy1, charm)
  if(spawnc==False):
    points+=1
    scorehandling(points)