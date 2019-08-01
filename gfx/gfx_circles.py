#init
import pygame as pg
from pygame import gfxdraw
from sys import exit

pg.init()

#screen
size = width, height = 1500, 860
screen = pg.display.set_mode(size)
framerate = 60
clock = pg.time.Clock()

#circle
x0 = 0
y0 = 0
r  = 2
black = 0, 0, 0

white = 255, 255, 255

#items on the screen
surf = pg.Surface(size)
col = 250, 235, 215
surf.fill(col)

ball = pg.gfxdraw.circle(surf, x0, y0, r, col)

while True:
	#exit condition
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
	### code here ###
	

	# appendix
	surf.fill(black)
	#screen.blit(surf)
	pg.display.flip()
	clock.tick(framerate)
