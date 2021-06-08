import turtle
from random import randint

#Making the Turtle objects
screen = turtle.Screen()  #Screen
draw_t = turtle.Turtle()  #To decorate our game background etc.
score_t = turtle.Turtle() #To Update the Score
text = turtle.Turtle()    #To display the question

#Making the needed variables to store game statistics
score = 0
bound = 2
chances = 5

#Defining Functions.
#Returns the mystery number, the upper and lower ranges as well. 
def sets(bound): 
  number = randint(0,1000)
  upper_bound = randint(number+1, number+bound)
  lower_bound = randint(number-bound, number-1)
  return number, upper_bound, lower_bound

#This function sets up our entire screen for us. This includes setting the background color as well as writing the latest score and number of chances left. It updates the question that we're asking our user 
def screen_setup(question):
  screen.bgcolor(23, 192, 235)
  score_write(score_t, score)
  question_write(text, question)
  draw(draw_t)

#This function writes down our score as well as our remaining chances. And incloses them incloses them in a mettalic black box drawing.
def score_write(t, score):
  t.speed("fastest")
  t.color(61, 61, 61)
  t.hideturtle()
  t.tracer(50)
  t.clear()
  t.penup()
  t.goto(-290, 175)
  t.pendown()
  t.write("Score : {}".format(score), font=("Verdana", 15, "normal"))
  t.penup()
  t.goto(-290, 155)
  t.write("Chances : {}".format(chances), font=("Verdana", 15, "normal"))
  t.penup()
  t.goto(-295, 200)
  t.pendown()
  t.setheading(0)
  t.fd(150)
  t.rt(90)
  t.fd(50)
  t.rt(90)
  t.fd(150)
  t.rt(90)
  t.fd(50) 

#This function writes down the question for our user. It takes a turtle object t and a string "question" as an argumtent. It then uses the turtle.write() function to display our question on the screen.
def question_write(t, question):
  t.speed("fastest")
  t.color("white")
  t.hideturtle()
  t.tracer(50)
  t.clear()
  t.penup()
  t.goto(-290, 0)
  t.pendown()
  t.write(question, font=("Verdana", 20, "bold"))

#This function is simply for the decoration of our game board.
def draw(t):
  t.speed("fastest")
  t.tracer(50)
  t.penup()
  t.goto(-300,-175)
  t.pendown()
  t.pensize(3)
  t.color(75, 75, 75)
  t.goto(300,-175)
  t.goto(-300,-175)
  i = 0
  while(i < 30):
    if (i%2==0):
      direction = -1
    else:
      direction = +1
    t.fd(0)
    t.lt(90*direction)
    t.fd(25)
    t.rt(90*direction)
    t.fd(20)
    t.rt(90*direction)
    t.fd(25)
    t.lt(90*direction)
    i+=1  
  t.hideturtle()

#Initial setup of the game. Adjusting Screen sized as well as number etc.
screen.setup(600,450)
screen_setup("")
number, upper_bound, lower_bound =  sets(bound)

#The main game loop, it will run till our player runs out of guesses.
while chances > 0:
  screen_setup("Guess a number between {} and {}".format(lower_bound, upper_bound))
  answer = int(input("You Guessed : "))
  if(answer == number):
    print("Correct!")
    score+=1
    chances += 1
    number, upper_bound, lower_bound =  sets(bound)
  elif (answer !=  number and chances>1):
    print("Wrong!")
    chances-=1
  else:
    print("Uh-oh! Out of turns. The number was {}.")
    chances-=1  