import pygame
import random
from enum import Enum


class Mob(pygame.sprite.Sprite):
    speedy = 0
    speedx = 0
    weights = [0.05, 0.35, 0.35, 0.05, 0.025, 0.05, 0.05, 0.05, 0.025]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        star = random.choices(population=list(StarTypes), k=1, weights=self.weights)[0]
        self._set_view(star.value)

    def _set_view(self, star):
        self.image = pygame.image.load(star.image_png)
        self.rect = self.image.get_rect()
        self.rect.x = 1921
        self.rect.y = random.randrange(180, 900)
        self.speedx = star.speed
        self.speedy = Mob.speedy
        self.radius = 10
        pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.rect.top < -10:
            self.kill()


class Star:
    def __init__(self, name, image_png, speed):
        self.name = name
        self.image_png = image_png
        self.speed = speed


class StarTypes(Enum):
    red_star = Star("Красный гигант", 'image/red.png', 7)
    yellow_star = Star("Желтый карлик", 'image/star.png', 8)
    white_star = Star("Белый карлик", 'image/white.png', 10)
    blue_star = Star("Синий гигант", 'image/blue.png', 7)
    dyson_star = Star("Сфера дайсона", 'image/dyson.png', 5)
    neutron_star = Star("Нейтронная звезда", 'image/neutron.png', 12)
    three_body = Star("Три тела", 'image/threebody.png', 6)
    two_body = Star("Два тела", 'image/twobody.png', 6)
    variable_star = Star("Переменная звезда", 'image/variable.png', 9)


class Page:
    def __init__(self, name, text, image, rect, size, x):
        self.name = name
        self.text = text
        self.image = pygame.image.load(image)
        self.rect = rect
        self.size = size
        self.x = x


class PageType(Enum):
    red_star = Page("Красный гигант", 'info/red.txt', 'image/stars/red.png', (350, 370), 50, 590)
    yellow_star = Page("Желтый карлик", 'info/yellow.txt', 'image/stars/star.PNG', (370, 360), 50, 590)
    white_star = Page("Белый карлик", 'info/white.txt', 'image/stars/white.png', (80, 80), 50, 590)
    blue_star = Page("Голубой гигант", 'info/blue.txt', 'image/stars/blue.png', (340, 370), 50, 590)
    dyson_star = Page("Сфера Дайсона", 'info/dyson.txt', 'image/stars/dyson.png', (200, 230), 50, 590)
    neutron_star = Page("Нейтронная звезда", 'info/neutron.txt', 'image/stars/neutron.png', (40, 80), 50, 590)
    three_body = Page("Система из трех тел", 'info/threebody.txt', 'image/stars/three_body.png', (330, 370), 50, 590)
    two_body = Page("Система из двух тел", 'info/twobody.txt', 'image/stars/two_body.png', (240, 250), 50, 590)
    variable_star = Page("Переменная звезда", 'info/variable.txt', 'image/stars/variable.png', (80, 110), 50, 590)
    stellar_hole = Page("Чёрная дыра звёздной массы", 'info/stellar.txt', 'image/stars/hole.PNG', (330, 370), 50, 690)
    middle_hole = Page("Чёрная дыра средней массы", 'info/middle.txt', 'image/stars/middle.png', (330, 400), 50, 690)
    supermassive = Page("Сверхмассивная чёрная дыра", 'info/supermassive.txt', 'image/stars/supermassive.png', (100, 70), 50, 690)


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
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
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
        if keystate[pygame.K_s]:
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


class Player2(Player):
    speedx = 8
    speedy = 8

    def __init__(self):
        super().__init__()
        self.speedx = 0

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -Player2.speedy
        if keystate[pygame.K_x]:
            self.speedy = Player2.speedy
        if keystate[pygame.K_d]:
            self.speedx = Player2.speedx
        if keystate[pygame.K_a]:
            self.speedx = -Player2.speedx
        self.rect.y += self.speedy
        self.rect.x += self.speedx
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
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)

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
        self.image = pygame.image.load(image_path)
        self.hover_image = pygame.image.load(hover_image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = sound_path
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font('scripts/Undertale_font.ttf', 80)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        if self.is_hovered:
            text_surface = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

