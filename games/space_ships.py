import pygame
import os

WIDTH, HEIGHT = 900, 500 #capitals as they are constant so will not be changed
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Ships") #changing name of programme
WHITE = (255,255,255)
BLACK = (0,0,0)
BORDER = pygame.Rect(WIDTH/2-5 ,0, 10, HEIGHT)
FPS = 60 #frame rate
VEL = 5 #velocity
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55,40)


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), (90))
#.transform allows us to format the image dimention and orientation


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), (270))



def draw_window(red, yellow):
        WIN.fill(WHITE) #order we draw is important hence fill is first layer
        pygame.draw.rect(WIN, BLACK, BORDER) #border in the middle of the screen
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))#draw a surface on the screen with blit
        WIN.blit(RED_SPACESHIP, (red.x, red.y))
        pygame.display.update() #Updates display to show changes

def yellow_handle_movement(keys_pressed, yellow): # allows multiple keys to be pressed at the same time
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT -15: #down
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT -15: #down
            red.y += VEL

def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT) 
    clock = pygame.time.Clock() #clock in game 
    run = True
    while run:
        clock.tick(FPS) #fps of game
        for event in pygame.event.get(): #allows to quit using the red X button
            if event.type == pygame.QUIT:
                run = False
        draw_window(red, yellow)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

    
    pygame.quit() 

if __name__ == "__main__":
    main()


