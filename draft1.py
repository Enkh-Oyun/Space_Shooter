import pygame
import sys
pygame.init()

screen_width = 800
screen_height = int(screen_width*0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption ("Santa Shooter")

#clock
clock = pygame.time.Clock()
FPS = 60

#player action
moving_left = False
moving_right = False

#define colors
BG = (144, 201, 120)


def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load("Santa.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), img.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        draw_bg()



def move(self, moving_left, moving_right):

    #reset movement variables
    dx = 0
    dy = 0

    #assign movement variables if moving left or right
    if moving_left:
        dx = - self.speed 
    if moving_right:
        dx= self.speed

    #update rect position
    self.rect.x += dx
    self.rect.y += dy


def draw(self):
    screen.blit(self.image, self.rect)
    player.add()

player = Soldier(200, 200, 3, 5)


while True:
    clock.tick(FPS)
    draw_bg()
    player.draw()
    player.move(moving_left, moving_right)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
               run = False 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False



    pygame.display.update()
pygame.display.quit()
pygame.quit()
sys.exit()
