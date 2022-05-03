import math
import random
from turtle import width
import pygame
import tkinter as tk
from tkinter import messagebox
import sys
pygame.init

class cube(object):
    row = 20
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, colour = (255, 0 , 0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes = False):
        pass

class snake(object):
    def __init__(self, colour, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def add_cube(self):
        pass
    def draw(self, surface):
        pass

def draw_grid(w, rows , surface):
    size_between = w // rows #the gap between the lines
    x = 0
    y= 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))  #change x, keep y at 0 vertical
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))  #keep x at 0, change y horizontal 

def redraw_window(surface):
    global rows, width
    surface.fill((0, 0, 0))
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
    s = snake((255, 0, 0), (10,10))
    clock = pygame.time.clock()
    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)
   
