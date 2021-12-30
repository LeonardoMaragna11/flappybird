from time import sleep
from ursina import collider,color,text,texture, duplicate
import ursina
import random
from ursina.ursinastuff import invoke 

app = ursina.Ursina()
ursina.Sky()
bird = ursina.Animation('assets/', 
                        collider = 'box',
                        scale=(2,2,1),
                        y=5)
ursina.camera.orthographic = True
ursina.camera.fov = 20
def update():
    bird.y = bird.y - 7*ursina.time.dt
    for p in pipes:
        p.x  = p.x - 7*ursina.time.dt
    touch = bird.intersects()
    if touch.hit or bird.y < -10:
        sleep(1)
        quit()



pipes = []
pipe = ursina.Entity(model = 'quad',
                    color=color.green,
                    texture='white_cube',
                    position=(20,10),
                    scale =(3,15,1),
                    collider = 'box')
def newpipe():
    y = random.randint(4,12)
    new1 = duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y-22)
    pipes.extend((new1,new2))
    invoke(newpipe, delay=2)

def input(key):
    if key == 'space':
        bird.y  = bird.y + 4

newpipe()
app.run()