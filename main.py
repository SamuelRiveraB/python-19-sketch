from turtle import Turtle, Screen
import random

# tim = Turtle()
# tim.color('green')
# tim.shape('turtle')
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
#
# def left():
#     tim.left(10)
#
# def right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.up()
#     tim.home()
#     tim.down()
#
# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=left)
# screen.onkey(key='d', fun=right)
# screen.onkey(key='c', fun=clear)

screen = Screen()
screen.setup(width=530, height=300)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
race = True

x = -180
y = -100

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for i in range(0, 6):
    new = Turtle(shape='turtle')
    new.color(colors[i])
    new.up()
    new.goto(x, y)
    y += 40
    turtles.append(new)

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
        else:
            rdm = random.randint(0, 10)
            turtle.forward(rdm)

screen.exitonclick()
