# Importing the modules
import turtle
import random
import time
import pygame
from tkinter import messagebox as msg

# Some Variables
pygame.init()
enemy_x = random.randint(-230, 230)
score = -1
enemy_score = 0
difficulty = 20
sound1 = pygame.mixer.Sound("Zoop - copy.wav")
sound2 = pygame.mixer.Sound("HandClap - copy.wav")

# Making the sprites and the screen
# Making the screen
win = turtle.Screen()
win.bgpic("spaceinvaderbackground - copy.gif")
image = "spaceinvaderplayer - copy.gif"
image1 = "spaceinvaderenemy - copy.gif"
win.addshape(image1)
win.addshape(image)
win.setup(500, 500)

# Writing the score
pen = turtle.Turtle()
pen.color("white")
pen.speed(-1)
pen.penup()
pen.goto(0, 220)
pen.hideturtle()
pen.write("Your Score: 0", align="center", font="courier 20 bold")

# Writing the enemy's score
pen1 = turtle.Turtle()
pen1.color("white")
pen1.speed(-1)
pen1.penup()
pen1.goto(0, -220)
pen1.hideturtle()
pen1.write("Enemy's Score: 0", align="center", font="courier 20 bold")

# Making the player
player = turtle.Turtle()
player.shape(image)
player.penup()
player.speed(-1)
player.goto(0, -130)

# Making the shooter
B = turtle.Turtle()
B.penup()
B.speed(-1)
B.hideturtle()
B.goto(player.xcor(), player.ycor())
B.shapesize(stretch_wid=0.5, stretch_len=0.5)
B.shape("square")
B.color("red")

# Making the enemy
enemy = turtle.Turtle()
enemy.shape(image1)
enemy.penup()
enemy.speed(-1)
enemy.goto(0, 170)

# Making the enemy shooter
BE = turtle.Turtle()
BE.penup()
BE.speed(-1)
BE.hideturtle()
BE.goto(enemy.xcor(), enemy.ycor())
BE.shapesize(stretch_wid=0.5, stretch_len=0.5)
BE.shape("square")
BE.color("light green")
msg.showinfo("Instructions", "Move the player by left and right arrow keys and hit the enemy using up arrow key")
answer = msg.askquestion("Select Mode", "Do you want hard difficulty level?")
if (answer == "yes"):
    difficulty = 60
# Making the functions
def enemyShoot():
    BE.showturtle()
    global enemy_score
    BE.goto(enemy.xcor(), enemy.ycor())
    for i in range(60):
        y = BE.ycor()
        y -= 5
        BE.sety(y)
    if BE.distance(player) < difficulty:
        sound2.play()
        BE.goto(enemy.xcor(), enemy.ycor())
        enemy_score += 1
        pen1.clear()
        pen1.write("Enemy's score: {}".format(enemy_score), align="center", font="courier 20 bold")
    if (enemy_score >= 3):
        msg.showinfo("You lose", "You lose enemy won the game!!")
        quit()
    BE.hideturtle()    
    BE.goto(enemy.xcor(), enemy.ycor())
def movetheenemy():
    for i in range(250):
        x = enemy.xcor()
        x += 15
        enemy.setx(x)
        if (enemy.xcor() > 230):
            enemy.goto(0, 170)
        if (enemy.xcor() < -230):
            enemy.goto(0, 170)    
        enemyShoot()           
def Right():
    x = player.xcor()
    x += 4
    player.setx(x)
    if (player.xcor() > 240):
        player.setx(220)   
def Left():
    x = player.xcor()
    x -= 4
    player.setx(x)
    if (player.xcor() < -240):
        player.setx(-220)
def Hit():
    B.showturtle()
    global score
    global enemy_score
    sound1.play()
    B.goto(player.xcor(), player.ycor())
    B.color("red")
    for i in range(60):
        y = B.ycor()
        y += 5
        B.sety(y)
    B.color("black")
    if B.distance(enemy) < 20:
        sound2.play()
        B.goto(player.xcor(), player.ycor())
        score += 1
        pen.clear()
        pen.write("Your Score: {}".format(score), align="center", font="courier 20 bold")
        enemy_x = random.randint(-230, 230)
        enemy.goto(enemy_x, 170)
        if (score >= 10):
            msg.showinfo("You won", "You won enemy lose the game!!")
            quit()
        movetheenemy()
    B.hideturtle()    
    B.goto(player.xcor(), player.ycor())

# Calling the listen function
win.listen()
win.onkeypress(Right, "Right")
win.onkeypress(Left, "Left")
win.onkeypress(Hit, "Up")
