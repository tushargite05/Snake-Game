from random import *
from turtle import *

from base import vector

player=vector(0,0)
print(player.x)
aim=vector(2,0)

def wrap(value):

    if value==210:
        dot(20,"blue")
    return value

def draw():
    # move player and draw screen
    player.move(aim)  #(0+2,0+0)=(2,0)

    player.x=wrap(player.x)
    player.y=wrap(player.y)
    aim.move(random()-0.5)
    aim.rotate(random()*10-5)  # 0.34*10==>3.14

    clear()
    goto(player.x,player.y)
    dot(10)

    if True:
        ontimer(draw,100)



setup(420,420,370,0)

tracer(False)
up()
draw()
done()