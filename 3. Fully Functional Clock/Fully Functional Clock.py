import turtle
import time

# Here we create a screen object to setup the screen size and the background color for our clock.
screen = turtle.Screen() 

# Setting up a screen of width 700 and height 500 pixels, starting x position is 0, starting y position is 0.

screen.setup(700, 500, 0, 0)     # setup (width, height, starting x, starting y)
screen.bgcolor("orange")     # the background color of our clock is orange


# Next we are going to draw the clock's dial. We need a turtle object to draw on the screen, so we have created a turtle object and named it 'dial'

dial = turtle.Turtle()    # turtle object to draw the clock
dial.shape("circle")      # the shape of our clock is a circle.

# Here we have set the drawing speed of our turtle 'dial'. The speed can be a number from 0 to 10 or a string "fastest", "fast", "normal", "slow", "slowest". 0 is fastest, 1 is slowest, numbers 2-10 are very slow to very fast.
dial.speed(0)


# Next we draw the seconds marks on the clock's dial. We will use a for loop that will run 60 times because there are 60 seconds around the dial of the clock.

# We will also use If/Else conditionals to decide when to draw small black seconds marks and when to draw the big red seconds marks on our clock. The order in which the If/Else conditions are met makes a pattern, 0 1 2 3 4 - 0 1 2 3 4 - 0 1 2 3 4 and so on. This happens because in our for loop we are taking a mod of each number from 0 to 60 with 5. Why do we need this special pattern? Because we start drawing our clock's dial with 1 big red seconds mark followed by 4 small black seconds marks, then again 1 big red mark and then 4 small black marks and we keep doing this 60 times. 

# The If condition is met whenever i % 5 is 0. i % 5 is 0 after every four iterations of the for loop, that is whenever we get a multiple of 5 for example 0, 5, 10, 15, 20 and so on....
# i % 5 is 0   when   0 % 5 is 0,   5 % 5 is 0,   10 % 5 is 0,   15 % 5 is 0,   20 % 5 is 0 and so on.

# The Else condition is met whenever i % 5 is not 0
# i % 5 is not 0   when   1 % 5 is 1,   2 % 5 is 2,   3 % 5 is 3,   4 % 5 is 4,   6 % 5 is 1,  7 % 5 is 2,   8 % 5 is 3,   9 % 5 is 4,   11 % 5 is 1,   12 % 5 is 2,   13 % 5 is 3,   14 % 5 is 4 and so on and so forth.

# In our 0 1 2 3 4 - 0 1 2 3 4 pattern, 0 represents the red marks on the dial and 1 2 3 4 represents the black marks on the dial of the clock.


for i in range(60):   
      if i % 5 == 0:          # Drawing the "red" marks around the dial
            dial.pensize(10)
            dial.pencolor("red")
            dial.penup()
            dial.forward(200)
            dial.pendown()
            dial.forward(10)
            dial.penup()
            dial.backward(210)
      else:                   # Drawing the "black" marks around the dial.
            dial.pensize(5)
            dial.pencolor("black")
            dial.penup()
            dial.forward(200)
            dial.pendown()
            dial.forward(5)
            dial.penup()
            dial.backward(205)      
      
      dial.right(6)         # Setting the distance between each seconds mark
      # the gap we see between each second mark on the dial of the clock is created by changing the direction of the turtle by 6 degrees in the right direction.


# Next we will use a While loop and If/Else conditionals to draw the hour, minute and second hands of our clock. For this, we need to calculate the rate of change of the angle in degrees per minute. The hour hand of the clock turns 360° in 12 hours (720 minutes) or 0.5° per minute. The minute hand turns 360° in 60 minutes or 6° per minute.

# Calculate the angle of Hour hand:  (hour x 30 + minute) x 0.5
# Calculate the angle of Minute hand:  minute x 6
# Calculate the angle of Second hand:  second x 6

update = True   # if minute and hour hand should update (once every minute)
updateSecond = True   # if the second hand should update

while True: 
      currentTime = time.localtime(time.time())   # Current time in your time zone
      # Current Time is returned in the form of a time-tuple (tm_year, tm_month, tm_monthday, tm_hour, tm_min, tm_sec, tm_weekday, tm_yearday, tm_isdst(daylightsavingtime) )
      hour =  (currentTime.tm_hour) % 12      # Current Hour - We take mod of the hour by 12 to convert 24-hour time to 12-hour time. 
      minute = currentTime.tm_min           # Get the Current Minute from the current time-tuple
      second = currentTime.tm_sec           # Get the Current Second from the current time-tuple

      if update:
            # Drawing the hour hand
            hourhand = turtle.Turtle()
            hourhand.left(90)
            hourhand.speed(100)
            hourhand.pensize(10)
            hourhand.shape("blank")
            hourhand.right(hour * 30 + minute * 0.5)
            hourhand.backward(30)
            hourhand.forward(160)

            # Drawing the minute hand
            minutehand = turtle.Turtle()
            minutehand.speed(100)
            minutehand.shape("blank")
            minutehand.left(90)
            minutehand.pensize(6)
            minutehand.right(minute * 6)
            minutehand.backward(30)
            minutehand.forward(180)

            update = False
            
      if updateSecond:
            # Drawing the second hand
            secondhand = turtle.Turtle()
            secondhand.speed(100)
            secondhand.shape("blank")
            secondhand.color("red")
            secondhand.left(90)
            secondhand.pensize(3)
            secondhand.right(second * 6)
            secondhand.backward(30)
            secondhand.forward(190)
            updateSecond = False

      time.sleep(0.3)   # sleep() function suspends execution for the given number of seconds.

      currentTime = time.localtime(time.time())  
      newMinute = currentTime.tm_min
      newSecond = currentTime.tm_sec

      if newMinute != minute:
            update = True
            hourhand.clear()      # Clear out the drawing (if any)
            hourhand.reset()
            minutehand.clear()
            minutehand.reset()
      if newSecond != second:
            updateSecond = True
            secondhand.clear()
            secondhand.reset()
