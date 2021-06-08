import turtle


#Adjusting the Screen of the game
wn = turtle.Screen()
wn.bgcolor('black')

#Making our first turtle
t1 = turtle.Turtle()
t1.speed("fastest")
t1.color('white')
rotate=int(360)

#This function drawsCircles. It takes a turtle and size as argument.
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4

#This function uses the circle we previously made and uses it to draw multiple circles
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)

#Lets call our function and see what happens
drawSpecial(t1,100,10)

#Lets make another turtle over here and change it up a bit.
t2 = turtle.Turtle()
t2.speed(0)
t2.color('yellow')
rotate=int(90)

#We're making the draw circles function again but this time with a smaller range in our for loop and a different decrement in our size variable.
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

#Lets call the drawSpecial Function but this time for t2 instead of t1
drawSpecial(t2,100,10)

#Adding a new turtle
t3 = turtle.Turtle()
t3.speed(0)
t3.color('blue')
rotate=int(80)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(t3,100,10)

t4 = turtle.Turtle()
t4.speed(0)
t4.color('orange')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(t4,100,10)

t5 = turtle.Turtle()
t5.speed(0)
t5.color('pink')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(t5,100,10)
