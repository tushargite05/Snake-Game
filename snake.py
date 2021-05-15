'''Game Name:  Snake Game
            author:   @Tushar
             End
              '''
from turtle import *
from random import *
from base import vector, square

food=vector(0,0)
snake=[vector(10,0)]
speed=10
aim=vector(0,-speed)

def change(x,y):
    """change the snake direction"""
    aim.x=x
    aim.y=y

def inside(head):
    """Return True if head is inside the boundary"""
    return -200< head.x<190 and -200< head.y < 190


def move():
    """Move the snake forward"""
    head=snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        print("GAME OVER")
        update()
        return

    snake.append(head)


    if head==food:
        print("Snake point: ",len(snake))
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10

    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food.x,food.y, 9, 'black')
    update()
    ontimer(move, 100)



setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
#Event handling
onkey(lambda: change(speed, 0),'Right')
onkey(lambda: change(-speed, 0),'Left')
onkey(lambda: change(0, speed),'Up')
onkey(lambda: change(0, -speed),'Down')
move()
done()
