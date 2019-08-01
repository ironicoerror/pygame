#!/bin/python3.5

"""Shows to balls that have a certain speed in x-direction and only the gravity in y-direction"""

import pygame as pg
import sys as sys
import os

pg.init()
size = width, height = 1500, 860
speed = [6,2] #x,y
speed_m = [6,2] #moon
black = 0, 0, 0
dt = 0
#look for a better way than loops // Singularity in the velocities or smth
loops = 10
vzwechsel = 0
vzwechselm = 0
screen = pg.display.set_mode(size)
framerate = 60 
clock = pg.time.Clock()
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    ball = pg.image.load(dir_path + "/intro_ball.gif")
    moon = pg.image.load(dir_path + "/intro_ball.gif")
except pg.error:
    print("Error: imagefile not found!")
    sys.exit()

ballrect = ball.get_rect()
moonrect = moon.get_rect()

state = False
state_m = False

while True:
    #exit loop for the pg.QUIT event
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
	
    #earth gravity ball
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        vzwechsel += 1
    if vzwechsel > loops:
        speed = [0, 0]
        status = True 
    else:
        speed[1] = speed[1] + 0.981 * dt

    #moon gravity ball
    moonrect = moonrect.move(speed_m)
    if moonrect.left < 0 or moonrect.right > width:
        speed_m[0] = -speed_m[0]
    if moonrect.top < 0 or moonrect.bottom > height:
        speed_m[1] = -speed_m[1]
        vzwechselm += 1
    if vzwechselm > loops:
        speed_m = [0, 0]
        status_m = True 
    else:
        speed_m[1] = speed_m[1] + 0.162 * dt
    dt = dt + (1/framerate)
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(moon, moonrect)
    pg.display.flip()
    clock.tick(framerate)
