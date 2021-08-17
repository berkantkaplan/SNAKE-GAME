import turtle
import time
import random


speedd = 0.15
window = turtle.Screen()
window.title('SNAKE GAME')
window.bgcolor('lightblue')
window.setup(width=700, height=700)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('purple')
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(0,100)
food.shapesize(0.75, 0.75)

queues = []
score = 0

write = turtle.Turtle()
write.speed(0)
write.shape('square')
write.color('white')
write.penup()
write.goto(0,300)
write.hideturtle()
write.write("Score: {}".format(score), align = "center", font = ("Courier", 24, "normal"))


def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

window.listen()
window.onkey(goUp, "Up")
window.onkey(goDown, "Down")
window.onkey(goRight, "Right")
window.onkey(goLeft, "Left")

        

while True:

    window.update()
    time.sleep(speedd)

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for queue in queues:
            queue.goto(1000,1000)

        queues = []
        
        score = 0

        write.clear()
        
        write.write("Score: {}".format(score), align = "center", font = ("Courier", 24, "normal"))
        
        speedd = 0.15

            
    if head.distance(food) < 20:
        x = random.randint(-15 , 15)*20
        y = random.randint(-15 , 15)*20

        food.goto(x,y)

        score = score + 10
        write.clear()
        write.write("Score: {}".format(score), align = "center", font = ("Courier", 24, "normal"))


        speedd = speedd - 0.001

        newQueue = turtle.Turtle()
        newQueue.speed(0)
        newQueue.shape("square")
        newQueue.color("pink")
        newQueue.penup()
        queues.append(newQueue)

    for i in range(len(queues) -1, 0, -1):
        x = queues[i - 1].xcor()
        y = queues[i - 1].ycor()
        queues[i].goto(x,y)

    if len(queues) > 0:
        x = head.xcor()
        y = head.ycor()
        
        queues[0].goto(x,y)
        



    move()



        
