import pygame as pg
import sys
pg.init()

#BACKGROUND = pg.image.load("starry_night.jpg").convert()
SURFACE = pg.display.set_mode((400,400))

while True:
    SURFACE.fill((0,100,100)) #you can call .fill() on the surface itself
    
    for event in pg.event.get():
        if event.type == pg.QUIT: #you have to reference event.type in this for loop
            pg.quit()
            sys.exit()