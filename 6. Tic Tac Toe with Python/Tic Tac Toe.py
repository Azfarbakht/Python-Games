import turtle 

#Making Objects for Screen and Turtle
screen = turtle.Screen()
t = turtle.Turtle()

#This function will draw a line from point (x1,y1) to point (x2,y2)
def line(t, x1,y1,x2,y2):
  t.hideturtle()
  t.speed("fastest")
  t.penup()
  t.goto(x1,y1)
  t.pendown()
  t.goto(x2,y2)
  t.penup()

#This function draws a grid
def grid():
    "Draw tic-tac-toe grid."
    line(t, -67, 200, -67, -200)
    line(t, 67, 200, 67, -200)
    line(t, -200, -67, 200, -67)
    line(t, -200, 67, 200, 67)

def drawx(x, y):
    "Draw X player."
    line(t, x, y, x + 133, y + 133)
    line(t, x, y + 133, x + 133, y)

def drawo(x, y):
    "Draw O player."
    t.up()
    t.goto(x + 67, y + 5)
    t.down()
    t.circle(62)

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    screen.update()
    state['player'] = not player

screen.setup(420, 420, 370, 0)
t.hideturtle()
screen.tracer(False)
grid()
screen.update()
screen.onscreenclick(tap)