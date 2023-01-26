#Cian Hodnett - 121368013
#Pygame assignment for CA2
#Goal is to recreate Space invaders with:
# 🗸 sprites
# 🗸 a ship that moves left and right (left and right arrows on keyboard) bound by screen edge
# 🗸 enemies that move to an edge of the screen then one sprite size closer
# 🗸 projectiles (rockets on space key, one per second)
# 🗸 hit-boxes that reward points
# 🗸 keep track of score (5 points per alien shot)
# 🗸 have a game over state
# 🗸 looping music

import pygame, math
from pygame import mixer

pygame.init()
mixer.init()

# Giving the game music - credit and license below:
# Gothic Dark by PeriTune | https://peritune.com/
# Music promoted by https://www.chosic.com/free-music/all/
# Creative Commons CC BY 4.0
# https://creativecommons.org/licenses/by/4.0/

# mixer.music.load('Gothic-Dark.mp3')
# mixer.music.set_volume(0.03)
# mixer.music.play(-1)

#variables to bes used for screen dimensions, easier to change if needed.  (divisible by 13 sprite sizes right now)
size = width, height = 624, 624

#square lets me multiply by the sprite size (48px x 48px)
square = 48
stage = 1

#clock function lets me set framerate maximum to stop things from moving too fast
clock = pygame.time.Clock()
frames = 30

points = 0

enemylist =[]
bullets = []
spawn = stage * 3

#creating the window, setting its size, naming the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Intergalactic Intruders")

class Ship(object):
    def __init__(self, x, y , width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

    def draw(self, screen):
        # background from https://www.freepik.com/free-vector/wavy-clouds-starry-night-background_5376565.htm#query=space%20background&position=12&from_view=keyword
        #free to use with attribution, free license
        self.bg = pygame.image.load("bg.jpg").convert()
        # from https://www.nicepng.com/ourpic/u2q8a9y3a9r5i1r5_vector-spaces-ship-8-bit-spaceship-sprite/
        # free for personal use
        self.ship = pygame.image.load("player_ship.png").convert_alpha()
        #from https://toppng.com/free-image/starfoxx-spaceship-pixel-art-spaceship-PNG-free-PNG-Images_228534
        #free for personal use
        self.baddie = pygame.image.load("baddie.png").convert_alpha()
        self.baddieRect = self.baddie.get_rect()
        screen.blit(self.bg, (0,0))
        screen.blit(self.ship, (sprite.x, sprite.y))
        screen.blit(self.baddie, (baddie.x, baddie.y))
        
class projectile(object):
    def __init__(self, x, y) -> None:
        self.x = x +18
        self.y = y +5
        self.vel = -25
    
    def shoot(self):
        self.y += self.vel

class Enemy(object):
    def __init__(self, x, y , width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4*stage

#creates the text that will display users score
class Score(object):
    def __init__(self, points) -> None:
        self.points = points

    def printScore(self, points):
        self.font = pygame.font.init()
        self.title=pygame.font.SysFont('Impact', 30)
        self.text_surface = self.title.render(str(points), False, (255,255,255))
        screen.blit(self.text_surface, (24,12))

    def gameOverScreen(self, points) -> None:
        self.points = points
        
        self.font = pygame.font.init()
        self.title=pygame.font.SysFont('Impact', 100)
        self.text_surface = self.title.render("Game Over", False, (255,255,255))
        screen.blit(self.text_surface, (100,200))

        self.score = pygame.font.init()
        self.subtitle=pygame.font.SysFont('Impact', 75)
        self.subtext_surface = self.subtitle.render(str(points), False, (255,255,255))
        screen.blit(self.subtext_surface, (100,310))
    
    def exitGame(self):
        pygame.quit()

def drawScreen():
    sprite.draw(screen)
    g.printScore(points)

g = Score(points)

#creating instance of ship, passing in variables defined earlier
sprite = Ship(square*6, square*10, square, square)
baddie = Enemy(square,square, square, square)


# def isCollision(x1, x2, y1, y2):
#     distance = math.sqrt((math.pow(x1 -  x2,2)) +
#                          (math.pow( y1 -  y2,2)))
#     if distance < 30:
#         return True
#     else:
#         return False 

#creating game-loop
status = True
while (status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    #checks for keys being pressed
    keys = pygame.key.get_pressed()

    #moves ship based on if left or right key are being pressed.
    if keys[pygame.K_LEFT]:
        sprite.x -= sprite.vel

    if keys[pygame.K_RIGHT]:
        sprite.x += sprite.vel

    if bullets == []:
        if keys[pygame.K_SPACE]:
            p = projectile(sprite.x, sprite.y)
            bullets.append([sprite.x, sprite.y])

    #collision for ship and sides of screen
    if sprite.x<0:
        sprite.x = 0
    
    if sprite.x>576:
        sprite.x = 576


    for projectiles in bullets:    
        p.shoot()        
        if p.y < 0:
            bullets.remove(projectiles)
        if baddie.x - 5 < p.x < baddie.x + 5 + square and baddie.y < p.y < baddie.y + square :
            baddie.x = square*14
            baddie.y = square*1
            baddie.vel = 0
            points +=5
    
    for enemy in enemylist:
        pass
    
    #enemy movement
    baddie.x += baddie.vel
    if baddie.x < 0:
        baddie.vel = baddie.vel * -1
        baddie.y += square
        
    if baddie.x > 576:
        baddie.vel = baddie.vel * -1
        baddie.y += square



    pygame.time.Clock
    clock.tick(frames)

    #draws the screen (background and sprites) every loop
    drawScreen()
    if baddie.y > square*9:
        baddie.x = 900
        baddie.y = 900
        baddie.vel = 0
        g.gameOverScreen(points)

    for projectiles in bullets:
        pygame.draw.rect(screen, (0,200,255), (p.x, p.y, 10, 5))
    
    pygame.display.update()
    pygame.display.flip()
    

pygame.quit()
    
        