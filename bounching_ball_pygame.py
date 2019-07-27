import pygame as pg
import sys as sys

pg.init()
size = width, height = 1500, 860
speed = [2,2] #x,y
speed_m = [2,2] #moon
black = 0, 0, 0
dt = 0
vzwechsel = 0
vzwechselm = 0
screen = pg.display.set_mode(size)
framerate = 60 
clock = pg.time.Clock()

ball = pg.image.load("intro_ball.gif")
moon = pg.image.load("intro_ball.gif")

ballrect = ball.get_rect()
moonrect = moon.get_rect()

state = False
state_m = False

while True:
	#earth
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		vzwechsel += 1
	if vzwechsel > 20:
		speed = [0, 0]
		status = True 
	else:
		speed[1] = speed[1] + 0.981 * dt
	#moon
	moonrect = moonrect.move(speed_m)
	if moonrect.left < 0 or moonrect.right > width:
		speed_m[0] = -speed_m[0]
	if moonrect.top < 0 or moonrect.bottom > height:
		speed_m[1] = -speed_m[1]
		vzwechselm += 1
	if vzwechselm > 20:
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
	print(vzwechsel)
	
