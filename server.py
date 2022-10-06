# Daniel Scheuermann
# CS 021
# Python script to make the color game work as intended


# imports
from flask import Flask, render_template, request
app = Flask(__name__)

import random

# global variables
chosenBox = 0
score = 0
highscoreHard = 0
highscoreEasy = 0
mode = "Hard"

# functions

# returns a random color in (x, y, z) format
# inputs: none, outputs: color
def getRandomColor():
    return "(" + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ")"

# checks to see if the guess is wrong or right or none
# inputs: guess, outputs: Whether the guess is wrong or right
def checkGuess(guess):
    global score
    global highscoreEasy
    global highscoreHard
    
    if guess == str(chosenBox):
        score += 1
        if mode == "Hard":
            if score >= highscoreHard:
                highscoreHard = score
        elif mode == "Easy":
            if score >= highscoreEasy:
                highscoreEasy = score
        return "Right!"
    elif guess == "":
        score = 0
        return ""
    else:
        score = 0
        return "Wrong!"

# main function
@app.route('/')
def index():
    # add global variables
    global chosenBox
    global score
    global highscore
    global mode

    # check if guess entered through form is correct via checkGuess function
    guess = request.args.get("guess", "0")
    if guess:
        rightOrWrong = ""
        rightOrWrong = checkGuess(guess)
    else:
        guess = ""
        rightOrWrong = ""
    
    # switch mode through switchMode function
    switch = request.args.get("mode", "")
    if switch == "Hard":
        mode = "Hard"
        rightOrWrong = ""
    elif switch == "Easy":
        mode = "Easy"
        rightOrWrong = ""

    # assign a variable to each box
    box1 = getRandomColor()
    box2 = getRandomColor()
    box3 = getRandomColor()
    box4 = getRandomColor()
    box5 = getRandomColor()
    box6 = getRandomColor()

    # assign a random box as 'chosen' and give it the chosen color
    boxes = []
    chosenColor = ""
    chosenBox = 0

    if mode == "Hard":
        boxes = [box1, box2, box3, box4, box5, box6,]
        chosenColor = getRandomColor()
        chosenBox = random.randint(0, 5)
        boxes[chosenBox] = chosenColor
    else:
        boxes = [box1, box2, box3,]
        chosenColor = getRandomColor()
        chosenBox = random.randint(0, 2)
        boxes[chosenBox] = chosenColor

    # Change chosenBox to its number + 1 because arrays start at 0 while boxes start at 1
    chosenBox += 1

    # renews html file with variables needed
    if mode == "Hard":
        return render_template("index.html", 
                                chosenColor = chosenColor,

                                box1 = boxes[0],
                                box2 = boxes[1],
                                box3 = boxes[2],
                                box4 = boxes[3],
                                box5 = boxes[4],
                                box6 = boxes[5],

                                rightOrWrong = rightOrWrong,

                                switchTo = "Easy",
                                difficulty = "Hard",
                                score = score,
                                highscore = highscoreHard,
                                visibility = ""
                                )
    else:
        return render_template("index.html", 
                                chosenColor = chosenColor,

                                box1 = boxes[0],
                                box2 = boxes[1],
                                box3 = boxes[2],
                                box4 = "",
                                box5 = "",
                                box6 = "",

                                rightOrWrong = rightOrWrong,

                                switchTo = "Hard",
                                difficulty = "Easy",
                                score = score,
                                highscore = highscoreEasy,
                                visibility = "hidden"
                                )


# debugger
if __name__ == '__main__':
    app.run(debug=True)
