import turtle
import time
from random import randint

#Creating all the turtle Objects
name_t = turtle.Turtle()
text_t = turtle.Turtle()
draw_t = turtle.Turtle()

#Creating and Setting up the Screen
screen = turtle.Screen()
screen.setup(600,400)
screen.bgcolor("sky blue")

#Setting Up Turtles
name_t.color('white')
name_t.hideturtle()
name_t.speed("fastest")
text_t.hideturtle()
text_t.speed("fastest")

#Drawing the cut out design
draw_t.color("white", "white")
draw_t.speed(15)
draw_t.penup()
draw_t.goto(50,-200)
draw_t.pendown()
draw_t.begin_fill()
draw_t.setheading(45)
draw_t.fd(370)
draw_t.setheading(270)
draw_t.fd(300)
draw_t.end_fill()


#Creating a list to contain all our possible words. The code is generic which means you may add as many words of your choice as you like! 
words = ["secret", "sky", "commercial", "comedy", "andromeda", "antibacterial", "python"]


#Writing the Welcome Message.
name_t.penup()
name_t.goto(-250, 150)
name_t.write("What is your name?", font=("Verdana",20, "bold"))
name = input("Name? : ")
name_t.clear()
name_t.write("Hello, " + name + " Time to Word-Play!", font=("Verdana",20, "bold"))



#Using the time library to wait for few seconds
time.sleep(2)
name_t.clear()
name_t.write("Start guessing...", font=("Verdana",20, "bold"))
time.sleep(0.5)

#Here we randomly select a word from our list of words. Observe how the second argument of the randint function is len(words)-1)
word = words[randint(0,len(words)-1)]

#creates a variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

#Preparing the text_t turtle to write down our word to be guessed.
text_t.penup()
text_t.hideturtle()
text_t.goto(-250, 0)
text_t.color('white')

# Create a while loop
#check if the turns are more than zero
while turns > 0:

    text_t.goto(-250,0)
    failed = 0 
    
    #lis is a string that we will use to store our guessing progress.
    lis = ""
    text_t.clear()

    #Here we iterate our string "word" character by character. We we find a character that is also among the guessed characters, we add it to lis.
    for char in word:
        if char in guesses:
            #The process below is called string concatenation. In string concatenation, we can add one string to the end of another string. 
            lis += char+" "
        else:
            lis += "_ "
            failed += 1
    
    #Once the above loop runs, our string "lis" will contain dashes for all unguessed letters.
    text_t.write(lis,False, font=("Verdana",25, "bold"))

    if failed == 0:
        name_t.clear()
        name_t.write("You Won! :D", font=("Verdana",20, "bold"))
        break

    guess = input("Guess a character : ")

    #All of the words in our dictionary are written down in small letters. What if the player accidentally enters a capital letter? We have used the below method .lower() to transform any upper case letters to lowercase. i.e. A will become a and D will become d and so on.
    guess = guess.lower()
    guesses += guess

    if guess not in word:
        turns -= 1
        name_t.clear()
        #The method used below "format() is for inserting any number into a string. Once the string is written down, the {} will be replaced by whatever value is inserted in the paranthesis of format()"
        name_t.write("Oops! You have {}".format(turns) + " more guesses", font=("Verdana",20, "bold"))

        if turns == 0:
            name_t.clear()
            name_t.write("Better luck next time!", font=("Verdana",20, "bold"))

