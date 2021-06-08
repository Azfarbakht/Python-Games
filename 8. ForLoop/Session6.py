import turtle 
from random import randint
#Welcome to your 6th Session with Python Level 1! In this class we'll be all about For Loops. Since you have already learned While loops, this class will be a piece of cake for you. 
#Another important lesson that we want to teach today is event handling in the turtle library. In other words, how you can use your real world keyboard commands to interact with the world inside turtle.

#Lets start with the essentials! 
t = turtle.Turtle()
t.pensize(3)

#You might remember making a square back in your second session. Let's try doing that again but this time with loops! 
t.reset()
t.speed('fastest')
for i in range(4):
  t.fd(100)
  t.rt(90)


#Now lets see you make a star using loops, remember, a star has 5 sides and the turning angle is 144 degrees
#-----------------------------------#
#Enter Code Here

for i in range(5):
  t.fd(100)
  t.rt(144)
#Stop Coding Here
#-----------------------------------#



#But what if we want more than just one square? What if we want lots and lots of squares? Do you think it's possible to put a loop... inside another loop?


for j in range(25):
  for i in range(4):
    t.fd(100)
    t.rt(90)
  t.rt(15)

#What you just saw was an example of nested loops. In python we can use nested loops to get a lot of work done. Why don't you try it out and try making something on your own? Why don't you try making many stars? 
#-----------------------------------#
#Enter Code Here



#Stop Coding Now
#-----------------------------------#

#Observe the two codes written below. They are written according to while loops. Can you convert them to For Loops?

t.goto(0,0)
t.clear()
edges = int(input("How many edges do you want? : "))
loops = int(input("How many loops do you want? : "))

for j in range(loops):
  for i in range(edges):
    t.fd(100)
    t.rt(360/edges)
  t.rt(360/loops)


#Alright, this is our final shape! Let's do this!
t.goto(0,0)
t.clear()
t.hideturtle()
turtle.tracer(2)
n=0
i = 0
for i in range(100):
#while i<100:
  t.color((randint(0,255),randint(0,255),randint(0,255)))
  t.circle(5+n)
  n = n+ 2
  #i = i+ 1


#Well now that that's out of the way, we can begin our work with Event handling in Turtle! 

#What I recommend is commenting out all the previous code you have written so we can proceed without any hassle.

turt = turtle.Screen()
t.showturtle()

#What we're doing right now is called Defining a function. For now, all you need to know is that Functions allow us 

def up():
  t.forward(100)

def down():
  t.forward(-100)

def left():
  t.lt(50)

def right():
  t.rt(50)


  
#This next line of code is a turtle method that makes your program listen for events. 
turt.listen()
turt.onkey(up, "Up") 
turt.onkey(down, "Down")
turt.onkey(left, "Left")
turt.onkey(right, "Right")


#Now I'm giving you a predefined function that draws a square. Can you make it so that everytime, you press the s-key, a square is drawn?


def square():
  for i in range(4):  
    t.fd(100)
    t.lt(90)

#Write Code Here
turt.onkey(square, "s")