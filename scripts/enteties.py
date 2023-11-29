import pygame
import random


class Mob(pygame.sprite.Sprite):
    speedx = 8
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/star.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 1921
        self.rect.y = random.randrange(180, 900)
        self.speedx = Mob.speedx

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.top < -10:
            self.rect.x = 1921
            self.rect.y = random.randrange(80, 1000)

class Player(pygame.sprite.Sprite):
    speedy = 8
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_anim = [
            pygame.image.load('image/player/blackhole1.png').convert(),
            pygame.image.load('image/player/blackhole2.png').convert(),
            pygame.image.load('image/player/blackhole1.png').convert(),
            pygame.image.load('image/player/blackhole2.png').convert()
        ]
        self.image = self.player_anim[0]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.radius = 40
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.x = 500
        self.rect.y = 500
        self.speedy = 0
        self.current_image = 0
        self.gravity = False

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -Player.speedy
        if keystate[pygame.K_x]:
            self.speedy = Player.speedy
        self.rect.y += self.speedy
        if self.rect.top < 100:
            self.rect.top = 100
        if self.rect.bottom > 980:
            self.rect.bottom = 980
        self.current_image += 0.08

        if self.current_image >= len(self.player_anim):
            self.current_image = 0

        self.image = self.player_anim[int(self.current_image)]
        self.image.set_colorkey((255, 255, 255))



class Enemy(pygame.sprite.Sprite):
    speedx = 7
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hole_anim = [
            pygame.image.load('image/bigblackhole0.png').convert(),
            pygame.image.load('image/bigblackhole1.png').convert(),
            pygame.image.load('image/bigblackhole0.png').convert(),
            pygame.image.load('image/bigblackhole1.png').convert()
        ]
        self.image = pygame.image.load('image/bigblackhole0.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.radius = 150
        self.rect.x = 1921
        self.rect.y = random.randrange(2, 400)
        self.speedx = Enemy.speedx
        self.current_image = 0
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.top < -10:
            self.rect.x = 1921
            self.rect.y = random.randrange(2, 400)
        self.current_image += 0.07

        if self.current_image >= len(self.hole_anim):
            self.current_image = 0

        self.image = self.hole_anim[int(self.current_image)]
        self.image.set_colorkey((255, 255, 255))

class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path).convert
        self.hover_image = pygame.image.load(hover_image_path).convert