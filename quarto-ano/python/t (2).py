from turtle import *
from time import sleep
from random import choice


colors = ('red', 'green', 'blue', 'magenta', 'cyan', 'yellow')


while True:
    color(choice(colors))
    begin_fill()
    forward(100)
    sleep(1)
    
    for _ in range(3):
        left(90)
        forward(100)
        sleep(1)
    end_fill()

