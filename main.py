from p5 import *
from star import star

stars = []

def setup():
    size(800, 800)
    for i in range(0, 100):
        stars.append(star())

def draw():
    speed = remap(mouse_x, (0, width), (0, 50))
    background(0)
    translate(width/2, height/2)
    for s in stars:
        s.update(speed)
        s.show()

run()
