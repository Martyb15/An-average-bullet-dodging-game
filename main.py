#Libraries
import os, pygame, pygame.mixer, random
from pygame.locals import *

#Variables
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
running = True
type = random.randint(1,4)

#Game Information + Images
screen_size = screen_width, screen_height = 512, 512
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pygame - A Random Bullet Dodging Game')

clock = pygame.time.Clock()
fps_limit = 60

img_path = os.path.join('player.png')
img_path2 = os.path.join('bullet.png')



#Creating the sprites
class Triangle(object):
    def __init__(self):
        self.image = pygame.image.load(img_path)
        self.x = 256
        self.y = 256

    def keys(self):
        key = pygame.key.get_pressed()
        dist = 0.125
        if key[pygame.K_DOWN] or key[pygame.K_s] and self.y < 512-32: # down key
            self.y += dist # move down
        elif key[pygame.K_UP] or key[pygame.K_w] and self.y > 0: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT] or key[pygame.K_d] and self.x < 512-32: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT] or key[pygame.K_a] and self.x > 0: # left key
            self.x -= dist # move left
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Bullet(object):
    def __init__(self, type):
        self.image = pygame.image.load(img_path2)
        # self.image = surface.blit(self.img, (self.x, self.y))
        self.x = 0
        self.y = 0
        self.type = type
      
    def orientation(self, surface):
        if self.type == 1:
          self.x = 0
          self.y = random.randint(0,512-32)
          # self.image = pygame.image.load(img_path2)
          self.image = pygame.transform.rotate(self.image, 90)
        if self.type == 2:
          self.x = random.randint(0,512-32)
          self.y = 0
          # self.image = pygame.image.load(img_path2)
          pygame.transform.rotate(self.image, 0)
        if self.type == 3:
          self.x = random.randint(0,512-32)
          self.y = 512-32
          # self.image = pygame.image.load(img_path2)
          pygame.transform.rotate(self.image, 180)
        if self.type == 4:
          self.x = 512-32
          self.y = random.randint(0,512-32)
          # self.image = pygame.image.load(img_path2)
          pygame.transform.rotate(self.image, 270)
            
    def move(self):
        if type == 1:
            for x in range(0, 480):
              self.x = x
              # print(self.x)

        elif type == 4:
            for x in range(480, 0, -1):
              self.x = x
              # print(self.x)

        elif type == 2:
            for y in range(0, 480):
              self.y = y
              # print(self.y)

        elif type == 3:
            for y in range(480, 0, -1):
              self.y = y
              # print(self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
      
                
            
            

player = Triangle()


while running:
    type = random.randint(1,4)
    # handle every event since the last frame.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
          
    bullet = Bullet(type)
    player.keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    player.draw(screen)
    # pygame.transform.rotozoom(bullet.image, 30.0, 60.0)

    pygame.display.update() # update the screen

# x = 0

