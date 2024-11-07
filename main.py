from turtle import Screen
import pgzrun
from random import randint

from pygame import Rect

WIDTH = 400
HEIGHT = 400

def draw():
    x = WIDTH
    y = HEIGHT-200
    for i in range(20):
        rect = Rect((0,0),(x,y))
        rect.center = 150,150
        screen.draw.rect(rect,"red")
        x += 10
        y -= 10



pgzrun.go()