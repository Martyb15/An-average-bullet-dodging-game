#Libraries
import os, pygame, pygame.mixer, random, time
from turtle import speed
from pygame.locals import *
import math

#Variables
black = (0,0,0)
red = (200,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

pygame.init()
running = True
type = random.randint(1,4)
WHITE = (255,255,255)
LIVES = 3
hit = -1
HEIGHT = 750 # Mayb we can work on getting a bigger window for the game....
WIDTH = 750
SPACE_HOLD = 14
SLOW = True
TOTAL_SECONDS = 0
dif_font = pygame.font.Font('Roboto-Regular.ttf', 32)


#Game Information + Images
screen_size = screen_width, screen_height = HEIGHT, HEIGHT
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pygame - A Random Bullet Dodging Game')




clock = pygame.time.Clock()
fps_limit = 60

img_path = os.path.join('player.png')
img_path2 = os.path.join('bullet.png')
img_path3 = os.path.join('Rocket.png')

animation_bar = []
baran1 = os.path.join('./bar/bar1.png')
baran2 = os.path.join('./bar/bar2.png')
baran3 = os.path.join('./bar/bar3.png')
baran4 = os.path.join('./bar/bar4.png')
baran5 = os.path.join('./bar/bar5.png')
baran6 = os.path.join('./bar/bar6.png')
baran7 = os.path.join('./bar/bar7.png')
baran8 = os.path.join('./bar/bar8.png')
baran9 = os.path.join('./bar/bar9.png')
baran10 = os.path.join('./bar/bar10.png')
baran11 = os.path.join('./bar/bar11.png')
baran12 = os.path.join('./bar/bar12.png')
baran13  = os.path.join('./bar/bar13.png')
baran14 = os.path.join('./bar/bar14.png')


animation_bar.append(baran1)
animation_bar.append(baran2)
animation_bar.append(baran3)
animation_bar.append(baran4)
animation_bar.append(baran5)
animation_bar.append(baran6)
animation_bar.append(baran7)
animation_bar.append(baran8)
animation_bar.append(baran9)
animation_bar.append(baran10)
animation_bar.append(baran11)
animation_bar.append(baran12)
animation_bar.append(baran13)
animation_bar.append(baran14)


#Creating the sprites

class Triangle(pygame.sprite.Sprite):
    active_player = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(img_path)
        self.image = pygame.image.load(img_path)
        # self.image.fill('purple')
        self.x = 256
        self.y = 256
        self.name = "PLAYER"
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        Triangle.active_player = self

    def keys(self):
        key = pygame.key.get_pressed()
        # dist = 0.125
        dist = 5
        if key[pygame.K_DOWN] or key[pygame.K_s] and self.y < HEIGHT-32: # down key
            self.y += dist # move down
        else:
            self.y =self.y 
        if key[pygame.K_UP] or key[pygame.K_w] and self.y > 0: # up key
            self.y -= dist # move up
        else:
            self.y=self.y
        if key[pygame.K_RIGHT] or key[pygame.K_d] and self.x < HEIGHT-32: # right key
            self.x += dist # move right
        else:
            self.x=self.x
        if key[pygame.K_LEFT] or key[pygame.K_a] and self.x > 0: # left key
            self.x -= dist # move left
        else:
            self.x=self.x
           
    def draw(self, surface):
        self.rect = self.image.get_rect()
        surface.blit(self.image, (self.x, self.y))

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        # print(sprite2.name) #check what player is colliding with
        if col == True:
            return True
            # bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))




class Start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('start.png')
        self.size = self.img.get_size()
        self.image = pygame.transform.scale(self.img,(int(self.size[0]* .7), int(self.size[1]*.7)))
        self.show = True
        self.x = 100
        self.y = 250
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        # self.image.fill('purple') #---------TEST

    def draw(self,surface):
        if self.show == True:
            self.rect = self.image.get_rect(topleft = (self.x,self.y))
            surface.blit(self.image,(self.x, self.y))


    def check_press(self,pos):
       
        print(self.rect.collidepoint(pos))
        if self.rect.collidepoint(pos):
            print("Hide Button")
            self.show = False

    def hover(self, check):
        if check == True:
            self.image = pygame.transform.scale(self.img,(int(self.size[0]* .8), int(self.size[1]*.8)))
        else:
            self.image = pygame.transform.scale(self.img,(int(self.size[0]* .7), int(self.size[1]*.7)))
       


class SlowBar:
    def __init__(self):
        self.img = pygame.image.load(animation_bar[0])
        self.size = self.img.get_size()
        self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        self.x = 200
        self.y = 2
        self.amount = 0
        self.available = True

    def animate(self, amount):
        self.amount = amount
        if amount >= 14:
            self.img = pygame.image.load(animation_bar[0])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 13:
            self.img = pygame.image.load(animation_bar[1])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 12:
            self.img = pygame.image.load(animation_bar[2])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 11:
            self.img = pygame.image.load(animation_bar[3])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 10:
            self.img = pygame.image.load(animation_bar[4])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 9:
            self.img = pygame.image.load(animation_bar[5])

        elif amount >= 8:
            self.img = pygame.image.load(animation_bar[6])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 7:
            self.img = pygame.image.load(animation_bar[7])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 6:
            self.img = pygame.image.load(animation_bar[8])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 5:
            self.img = pygame.image.load(animation_bar[9])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 4:
            self.img = pygame.image.load(animation_bar[10])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
        elif amount >= 3:
            self.img = pygame.image.load(animation_bar[11])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
            self.available = True 
        elif amount >= 2:
            self.img = pygame.image.load(animation_bar[12])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
            
        elif amount >= 1:
            self.img = pygame.image.load(animation_bar[13])
            self.image = pygame.transform.scale(self.img, (int(self.size[0]*.3), int(self.size[1]*.3)))
            self.available = False 
        

    def draw(self,surface, amount):
            self.rect = self.image.get_rect(topleft = (self.x,self.y))
            surface.blit(self.image,(self.x, self.y))
            self.animate(amount)

    def update(self):
        if self.amount < 0:
            self.available = True
            return self.available

        
    



class Lives(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img_path,"2")
        self.name = "LIVES"
        self.size = self.img.get_size()
        self.image = pygame.transform.scale(self.img, (int(self.size[0]*.5), int(self.size[1]*.5)))
        # self.image.fill('purple')
        self.x = 2
        self.y = 2
        self.rect = self.image.get_rect()

    def draw(self, surface):
        self.rect = self.image.get_rect()
        surface.blit(self.image, (self.x, self.y))
        #opacity
        #location = upper left


class Bullet(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path2)
        # self.image.fill('purple')
        # self.image.fill('purple')
        # self.image = surface.blit(self.img, (self.x, self.y))
        self.name = "BULLET"
        self.x = 0
        self.y = 0
        self.new = False
        self.steps = 10
        self.type = type
        self.direction = 0
        self.rect = self.image.get_rect()
        self.speed = 6
    #-----
    # def is_collided_with(self, sprite):
    #     return self.rect.colliderect(sprite.rect)
      
    def orientation(self, surface):
        self.image = pygame.image.load(img_path2)
        # self.image.fill('purple')
        # self.image.fill('purple')

        self.type = random.randint(1,4)
        
        if self.type == 1:
          self.direction = 270
          self.x = 0
        #   self.x = HEIGHT - 32
          self.y = random.randint(0,HEIGHT-32)
          # self.image = pygame.image.load(img_path2)
          self.image = pygame.transform.rotate(self.image, self.direction)

        if self.type == 2:
          self.direction = 180
          self.x = random.randint(0,HEIGHT-32)
          self.y = 0
          # self.image = pygame.image.load(img_path2)
          self.image = pygame.transform.rotate(self.image, self.direction)

        if self.type == 3:
          self.direction = 0
          self.x = random.randint(0,HEIGHT-32)
          self.y = HEIGHT-32
          # self.image = pygame.image.load(img_path2)
          self.image = pygame.transform.rotate(self.image, self.direction)

        if self.type == 4:
          self.direction = 90
          self.x = HEIGHT-32
          self.y = random.randint(0,HEIGHT-32)
          # self.image = pygame.image.load(img_path2)
          self.image = pygame.transform.rotate(self.image, self.direction)
            
    def move(self,surface):
        
        if self.type == 1:
            if self.x <= HEIGHT:
                self.x += self.speed
                self.draw(surface)
                # print(self.y, "--", self.x)
            else: 
            
                self.new = True        

        elif self.type == 4:
            if self.x >= 0:
                self.x -= self.speed
                self.draw(screen)
                # print(self.y, "--", self.x)
            else: 
              
                self.new = True

        elif self.type == 2:
            if self.y <= HEIGHT:
                self.y += self.speed
                self.draw(screen)
                # print(self.y, "y--x", self.x)
            else: 
               
                self.new = True

        elif self.type == 3:
            if self.y >= 0:
                self.y -= self.speed
                self.draw(screen)
                # print(self.y, "--", self.x)
            else: 
            
                self.new = True

        self.rect = self.image.get_rect()


    def draw(self, surface):
        self.rect = self.image.get_rect()
        surface.blit(self.image, (self.x, self.y))

    def reset_image_orientation(self):
        self.image = pygame.transform.rotate(self.image, 0 - self.direction)
        self.orientation(screen)
        
    def temp(self):
        if self.x < 5 and self.y < 5:
            print("Why am I here?", self.name)


def draw_background(color):
    screen.fill(color)    
    
                


def bullets_amount(sec):
    if sec >= 10.5 and secos < 20.5:
        return 2
    elif sec >= 20.5 and sec < 30.5:
        return 3
    elif sec >= 30.5 and sec < 40.5:
        return 4
    elif sec >= 40.5 and sec < 50.5:
        return 5
    elif sec >= 50.5 and sec < 60.5:
        return 6
    elif sec >= 60.5 and sec < 70.5:
        return 7
    elif sec >= 70.5 and sec < 80.5:
        return 8
    elif sec >= 80.5:
        return 9
    else: return 1

class Rocket(Bullet):
    def __init__(self):
        super().__init__(3)
        self.direction = 0
        self.rspeed = 3
        self.name = "ROCKET"
        self.image = pygame.image.load(img_path3)
        self.rect = self.image.get_rect()
        self.rotationAmount = 0
    
    def orientation(self, surface):
        dir_x = Triangle.active_player.x - self.x
        dir_y = Triangle.active_player.x - self.y
        movement = pygame.math.Vector2(dir_x,-1*dir_y)
        up = pygame.math.Vector2(0,1)
        center_x = Triangle.active_player.x - self.rect.center[0]
        center_y = Triangle.active_player.y - self.rect.center[1]
        mvmnt = pygame.math.Vector2(center_x, -1*center_y)
        direction = up.angle_to(mvmnt)
        # math.degrees(math.atan2(dir_x, dir_y))
        self.rotationAmount = direction
        self.image = pygame.transform.rotate(pygame.image.load(img_path3), direction)
    
    def move(self, surface):
        dir_x = Triangle.active_player.x - self.x
        dir_y = Triangle.active_player.y - self.y
        dir = pygame.math.Vector2(dir_x, dir_y)
        dir = dir.normalize()
        self.x += self.rspeed * dir.x
        self.y += self.rspeed * dir.y
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.rect.x,self.rect.y)

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def reset_image_orientation(self):
        self.x = 0
        self.y = 0



type = random.randint(1,4)

player = Triangle()
bullet = Bullet(type)

bullet2 = Bullet(type)

bullet3 = Bullet(type)

bullet4 = Bullet(type)

bullet5 = Bullet(type)

bullet6 = Bullet(type)

bullet7 = Bullet(type)

bullet8 = Bullet(type)

bullet9 = Bullet(type)

rocket = Rocket()


life1 = Lives()
life2 = Lives()
life2.x = 40
life3 = Lives()
life3.x = 20

bar = SlowBar()
start = Start()
bullet_group = pygame.sprite.Group()

secos = 1

# clicked = pygame.mouse.get_pressed() 

bullet_group.add(bullet)
bullet_group.add(rocket)


while running:

    if hit > secos:
        draw_background(red)
    else:
        draw_background(WHITE) # fill the screen with white
    # pygame.transform.rotozoom(bullet.image, 30.0, 60.0)

    for event in pygame.event.get():
        key = pygame.key.get_pressed()
 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event.pos[0],event.pos[1])
            start.check_press((event.pos[0],event.pos[1]))
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if ( x in range(116,483)) and (y in range(273,339)):
                start.hover(True)
            else:
                 start.hover(False)

    
        
        if key[pygame.K_SPACE] and bar.available == True:
          for b in bullet_group:
            b.speed = 2.5
            if SPACE_HOLD <= 0:
                SPACE_HOLD = 0
            else:
                SPACE_HOLD -= 1/15 # controls SLOW usage speed
        else: 
          for b in bullet_group:
            b.speed = 6
            if SPACE_HOLD < 14:
                SPACE_HOLD += 1/45 # Speed for regaining SLOW
            elif SPACE_HOLD > 14:
                SPACE_HOLD = 14

        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
    if start.show == True:
        #RESET
        for b in bullet_group:
            b.orientation(screen)
        screen.fill(WHITE)
        start.draw(screen)
        clock.tick(fps_limit)
        SLOW = 14
        bar.animate(SLOW)
        secos = 1
        LIVES = 3
        bullets = 1
        hit = -1
        player.y = 256
        player.x = 256
    # print(secos)
        pygame.display.update()
        continue
    # print(start.x,start.y)

    for b in bullet_group:
        b.temp()
            
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_presses = pygame.mouse.get_pressed()
        #     if mouse_presses[0]:
        #         print(20*"Left Mouse key was clicked")

   

    # print("SPACE_HOLD", SPACE_HOLD)

    
    
    

    SLOW = bar.available

    bullets = bullets_amount(secos)

    for b in bullet_group:
        if b.new == True:
            b.new = False
            b.orientation(screen)

    
    for bull in bullet_group:
        if player.checkCollision(player, bull) == True:
            bull.reset_image_orientation()
            LIVES -= 1
            hit = secos + .25
            # print(hit,"-----",secos)


    

    
    
    bar.draw(screen, SPACE_HOLD)
    start.draw(screen)
    player.draw(screen)
    text = dif_font.render(str(rocket.rotationAmount), True, (0,0,0))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    # if clicked[0]:
    #     print("Left Mouse Key is being pressed")

    bar.update()

    if bullets < 2:
       
        bullet.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        print(rocket.rect)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
       
    elif bullets == 2:
        
        bullet_group.add(bullet2)

        bullet.move(screen)
        
        bullet2.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        print(rocket.rect)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))

    elif bullets == 3:
        bullet_group.add(bullet3)
        bullet.move(screen)
        bullet2.move(screen)
        
        bullet3.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        print(rocket.rect)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))

    elif bullets == 4:
        bullet_group.add(bullet4)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
        
    elif bullets == 5:
        bullet_group.add(bullet5)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        bullet5.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        bullet5.rect = bullet5.image.get_rect(topleft = (bullet5.x, bullet5.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
  
    elif bullets == 6:
        bullet_group.add(bullet6)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        bullet5.move(screen)
        bullet6.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        bullet5.rect = bullet5.image.get_rect(topleft = (bullet5.x, bullet5.y))
        bullet6.rect = bullet6.image.get_rect(topleft = (bullet6.x, bullet6.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
    elif bullets == 7:
        bullet_group.add(bullet7)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        bullet5.move(screen)
        bullet6.move(screen)
        bullet7.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        bullet5.rect = bullet5.image.get_rect(topleft = (bullet5.x, bullet5.y))
        bullet6.rect = bullet6.image.get_rect(topleft = (bullet6.x, bullet6.y))
        bullet7.rect = bullet7.image.get_rect(topleft = (bullet7.x,  bullet7.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
    elif bullets == 8:
        bullet_group.add(bullet8)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        bullet5.move(screen)
        bullet6.move(screen)
        bullet7.move(screen)
        bullet8.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        bullet5.rect = bullet5.image.get_rect(topleft = (bullet5.x, bullet5.y))
        bullet6.rect = bullet6.image.get_rect(topleft = (bullet6.x, bullet6.y))
        bullet7.rect = bullet7.image.get_rect(topleft = (bullet7.x,  bullet7.y))
        bullet8.rect = bullet8.image.get_rect(topleft = (bullet8.x,  bullet8.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))
    elif bullets == 9:
        bullet_group.add(bullet9)
        bullet.move(screen)
        bullet2.move(screen)
        bullet3.move(screen)
        bullet4.move(screen)
        bullet5.move(screen)
        bullet6.move(screen)
        bullet7.move(screen)
        bullet8.move(screen)
        bullet9.move(screen)
        rocket.move(screen)
        rocket.orientation(screen)
        bullet.rect = bullet.image.get_rect(topleft = (bullet.x,  bullet.y))
        bullet2.rect = bullet.image.get_rect(topleft = (bullet2.x,  bullet2.y))
        bullet3.rect = bullet3.image.get_rect(topleft = (bullet3.x,  bullet3.y))
        bullet4.rect = bullet4.image.get_rect(topleft = (bullet4.x,  bullet4.y))
        bullet5.rect = bullet5.image.get_rect(topleft = (bullet5.x, bullet5.y))
        bullet6.rect = bullet6.image.get_rect(topleft = (bullet6.x, bullet6.y))
        bullet7.rect = bullet7.image.get_rect(topleft = (bullet7.x,  bullet7.y))
        bullet8.rect = bullet8.image.get_rect(topleft = (bullet8.x,  bullet8.y))
        bullet9.rect = bullet9.image.get_rect(topleft = (bullet9.x,  bullet9.y))
        #rocket.rect = rocket.image.get_rect(topleft = (rocket.x,  rocket.y))

    if LIVES == 3:
        life1.draw(screen)
        life2.draw(screen)
        life3.draw(screen)
    elif LIVES == 2:
        life1.draw(screen)
        life3.draw(screen)
    elif LIVES == 1:
        life1.draw(screen)
    elif LIVES == 0:
        start.show = True
        bullet.rect = bullet.image.get_rect(topleft = (-100,  -100))
        bullet2.rect = bullet.image.get_rect(topleft = (-100,  -100))
        bullet3.rect = bullet3.image.get_rect(topleft = (-100,  -100))
        bullet4.rect = bullet4.image.get_rect(topleft = (-100,  -100))
        bullet5.rect = bullet5.image.get_rect(topleft = (-100,  -100))
        bullet6.rect = bullet6.image.get_rect(topleft = (-100,  -100))
        bullet7.rect = bullet7.image.get_rect(topleft = (-100,  -100))
        bullet8.rect = bullet8.image.get_rect(topleft = (-100,  -100))
        bullet9.rect = bullet9.image.get_rect(topleft = (-100,  -100))
    
    
    # else: pygame.quit()


  


    # result = pygame.sprite.collide_rect(bullet, player)
        

    if player.x == bullet.x and player.y == bullet.y:
        pygame.quit()
    # time.sleep(1)
    player.keys() # handle the keys

    
    
    player.rect = player.image.get_rect(topleft = (player.x, player.y))

    
    #rocket.orientation(screen)
    clock.tick(fps_limit)
    secos += 1 / 60
    TOTAL_SECONDS += 1/60
    # print(secos)
    rocket.draw(screen)
    pygame.display.update() # update the screen
    print(rocket.rect)



# Reset the slow mo when round ends
# Figure out glitch with red screen and bullets being set around border before problem(game is infinitely reset)
# Top left corner bullet spawn
# Restart not working perfectly

# bullet orientation when initialized 
