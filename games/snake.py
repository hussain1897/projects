import pygame, sys, math, random
import tkinter as tk
from tkinter import messagebox



class cube(object):
    row = 20
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, colour = (255,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes = False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event in pygame.event.Quit:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                   self.dirnx = -1
                   self.dirny = 0
                   self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i, c in enumerate(self.body): #i is the index c is cube object
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: (c.rows-1,c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0],0)
                elif c.dirny == -1 and c.pos[1] <= 0: (c.pos[0],c.rows-1)
                else:
                    c.move(c.dirnx,c.dirny)

    def reset(self, pos):
        pass
    def add_cube(self):
        pass
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
                    
def draw_grid(w, rows , surface):
    size_between = w // rows #the gap between the lines

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))  #change x, keep y at 0 vertical
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))  #keep x at 0, change y horizontal 

def redraw_window(surface):
    global rows, width, s
    s.draw(surface)
    surface.fill((0,0,0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows , s
    width = 500 #width of the screen
    height = 500
    rows = 20 #amount of rows
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                sys.exit()  
cube.rows = rows
cube.w = w
main()
