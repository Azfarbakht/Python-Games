import turtle

t = turtle.Turtle()
screen = turtle.Screen()
r = 8
c = 8
arr = [[0 for i in range(c)] for j in range(r)]
#A dictionary is a collection which is unordeDarkRed, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
turns = {'DarkRed': 'DarkSlateBlue', 'DarkSlateBlue': 'DarkRed'}
state = {'player': 'DarkSlateBlue', 'rows': [0] * 8}

#Defining function to draw a line
def line(t, x1,y1,x2,y2):
  t.hideturtle()
  t.color("#2C5F2D")
  t.pensize(3)
  t.speed("fastest")
  t.penup()
  t.goto(x1,y1)
  t.pendown()
  t.goto(x2,y2)
  t.penup()

#Drawing Grid
def grid():
    "Draw Connect Four grid."
    screen.bgcolor('DarkSlateGray')

    for x in range(-150, 200, 50):
        line(t,x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            t.up()
            t.goto(x, y)
            t.dot(20, 'white')
    screen.update()

#This function is to be executed, everytime the mouse is clicked
def tap(x, y):
    "Draw DarkRed or yellow circle in tapped row."
    player = state['player']
    rows = state['rows']

    #Here we are normalizing the or "flooring" the x value recieved from the mouse to determine which row has been clicked.
    row = int((x + 200) // 50)
    count = rows[row]
    
    x = ((x + 200) // 50) * 50 - 200 + 25
    
    y = count * 50 - 200 + 25

    t.up()
    t.goto(x, y)
    t.dot(20, player)
    insert(x,y,player)
    print_array(arr)
    screen.update()

    rows[row] = count + 1
    state['player'] = turns[player]

def assign(x,y):
  x = (x+175)//50
  y = (y+175)//50
  return x,y

def insert(x,y,player):
  x,y = assign(x,y)
  if player == "DarkRed":
    arr[x][y] = "R"
  if player == "DarkSlateBlue":
    arr[x][y] = "B"

def print_array(a):
  print("Array : ")
  for i in range(8):
    for j in range(8):
      print(arr[i][j]),
    print("")

screen.setup(420, 420, 370, 0)
t.hideturtle()
grid()
screen.onscreenclick(tap)
screen.done()