import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500 #capitals as they are constant so will not be changed
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Ships") #changing name of programme
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

BORDER = pygame.Rect(WIDTH//2-5 ,0, 10, HEIGHT)
FPS = 60 #frame rate
VEL = 5 #velocity
BULLET_VEL = 7

MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55,40)

YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
#.transform allows us to format the image dimention and orientation


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0)) #order we draw is important hence fill is first layer
    pygame.draw.rect(WIN, BLACK, BORDER) #border in the middle of the screen
    
    red_health_text = HEALTH_FONT.render("Health:" + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health:" + str(yellow_health), 1, WHITE)

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() -1, 10))
    WIN.blit(yellow_health_text, (10,10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))#draw a surface on the screen with blit
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)


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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT) 

    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    clock = pygame.time.Clock() #clock in game 
    run = True
    while run: #game loop
        clock.tick(FPS) #fps of game
        for event in pygame.event.get(): #allows to quit using the red X button
            if event.type == pygame.QUIT:
                run = False
                pygame,quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: #yellow.x and width to put on edge of image | yellow.y and height so bullet comes from middle
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2-2, 10, 5) # (10,5) dimentions of bullet
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10,5) # (10,5) dimentions of bullet
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -=1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        
        if red_health<= 0:
            winner_text = "Yellow Wins!"
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    
    main()

if __name__ == "__main__":
    main()


