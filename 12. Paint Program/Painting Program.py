
#Let us import the Turtle library once again. * here means all.
from turtle import *


#Setting up screen
screen = Screen()
screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2
screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

#Setting up turtle 
t = Turtle()
t.goto(0, 0)
t.speed(10)

# Set up event handler to have the t draw a line
# to the point that the user clicks on
def on_screen_click(x, y):  
  if y < screenMaxY - 40: # only draw if clicked below color squares
    t.goto(x, y)

#Let's call this method right now. When you click on the screen, this function is executed    
screen.onclick(on_screen_click)
  
#What we're about to make right now is a class. A class is basically a building block that leads to object oriented programming. Each class has some characteristics and some functions that it performs. Making a class for the ColorPicker will allow us to group all of its functions and attributes together.

class ColorPicker(Turtle):

  def __init__(self, color="red",num=0):
    Turtle.__init__(self)
    self.num = num
    self.color_name = color
    self.speed(0)
    self.shape("circle")
    self.color("black", color)
    self.penup()
    
    # hack to register click handler to instance method
    self.onclick(lambda x, y: self.handle_click(x, y))

  def draw(self):
    self.setx(screenMinX+110+self.num*30)
    self.sety(screenMaxY - 20)
    
  def handle_click(self, x, y):
    if self.color_name == "#F9F9F9":
      t.penup()
      t.color("black")
    else:
      t.pendown()
      t.color(self.color_name)
    
# Suppress animations while interface is being drawn
screen.tracer(0)

#This turtle creates the UI elements of our program
ui_turtle = Turtle()
ui_turtle.ht()
ui_turtle.penup()
ui_turtle.goto(screenMinX, screenMaxY - 23)
ui_turtle.write("TurtleDraw!", align="left", font=("Courier", 10, "bold"))

# Create color choosing squares at the top of screen
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "#F9F9F9"]
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
  picker.draw()

# Resume animations now that main interface has been drawn
screen.tracer(1)