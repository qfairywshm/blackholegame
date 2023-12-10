import pygame
from scripts.utils import draw_text, show_go_screen
from scripts.enteties import Mob, Player, Enemy, Button
class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1920, 1080))

        pygame.display.set_caption("Wandering Black hole")

        self.bg = pygame.image.load('image/backgroundfull2.png')
        self.bg_x = 0
        self.bg_speed = 1

        self.stars = pygame.sprite.Group()
        self.holes = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        self.star_timer_tick = 3500
        self.hole_timer_tick = 15000

        self.star_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.star_timer, self.star_timer_tick)
        self.hole_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.hole_timer, self.hole_timer_tick)

        self.score = 0

        self.gbutton = Button((1920/3), (1080/3 - 40), 200, 50, 'Начать', 'image/button.png', 'image/button (1).png')
        self.exitbutton = Button((1920/3), (1080/3 + 250), 200, 50, 'Выход', 'image/button.png', 'image/button (1).png')

    def main_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.screen.blit(self.bg, (self.bg_x, 0))
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.USEREVENT and event.button == self.exitbutton:
                    pygame.quit()
                self.exitbutton.handle_event(event)
                self.exitbutton.check_hover(pygame.mouse.get_pos())
                self.exitbutton.draw(self.screen)
                if event.type == pygame.USEREVENT and event.button == self.gbutton:
                    self.play()
                self.gbutton.handle_event(event)
                self.gbutton.check_hover(pygame.mouse.get_pos())
                self.gbutton.draw(self.screen)
                pygame.display.update()
    def play(self):
        running = True
        self.game_over = False
        while running == True:
            if self.game_over:
                show_go_screen(self.screen, self.bg, self.clock)
                self.game_over = False
                self.all_sprites = pygame.sprite.Group()
                self.stars = pygame.sprite.Group()
                self.holes = pygame.sprite.Group()
                self.player = Player()
                self.all_sprites.add(self.player)
                self.score = 0
                Mob.speedx = 8
                Player.speedy = 8
                Enemy.speedx = 7
                self.bg_speed = 1
                pygame.time.set_timer(self.star_timer, 3500)

            self.screen.blit(self.bg, (self.bg_x, 0))
            self.screen.blit(self.bg, (self.bg_x + 1920, 0))

            hits = pygame.sprite.spritecollide(self.player, self.stars, True, pygame.sprite.collide_circle)
            if hits:
                self.score += 1
                if Mob.speedx <= 15:
                    Mob.speedx += 0.5
                if Player.speedy <= 15:
                    Player.speedy += 0.25
                if Enemy.speedx <= 14:
                    Enemy.speedx += 0.2
                if self.bg_speed <= 10:
                    self.bg_speed += 0.5
                if self.star_timer_tick >= 1800:
                    self.star_timer_tick -= 100
                    pygame.time.set_timer(self.star_timer, self.star_timer_tick)


            eats = pygame.sprite.spritecollide(self.player, self.holes, False, pygame.sprite.collide_circle)
            if eats:
                self.game_over = True

            gravity = pygame.sprite.spritecollide(self.player, self.holes, False, pygame.sprite.collide_circle_ratio(3))
            if gravity:
                if self.player.rect.centery > h.rect.centery:
                    self.player.rect.centery -= Player.speedy - 3
                elif self.player.rect.centery < h.rect.centery:
                    self.player.rect.centery += Player.speedy - 3
                if self.player.rect.centerx > h.rect.centerx:
                    self.player.rect.centerx -= Player.speedy - 5
                elif self.player.rect.centerx < h.rect.centerx:
                    self.player.rect.centerx += Player.speedy - 3
            else:
                if self.player.rect.x > 500:
                    self.player.rect.x -= 5
                    if self.player.rect.x < 505:
                        self.player.rect.x = 500
                elif self.player.rect.x < 500:
                    self.player.rect.x += 5
                    if self.player.rect.x > 495:
                        self.player.rect.x = 500
                #else:
                    #self.player.rect.x = 500
            #gravity2 = pygame.sprite.spritecollide(h, self.stars, True, pygame.sprite.collide_circle)



            self.bg_x -= self.bg_speed
            if self.bg_x <= -1920:
                self.bg_x = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.star_timer:
                    m = Mob()
                    self.all_sprites.add(m)
                    self.stars.add(m)
                if event.type == self.hole_timer:
                    h = Enemy()
                    self.all_sprites.add(h)
                    self.holes.add(h)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            draw_text(self.screen, 'счет: ' + str(self.score), 30, 350, 150)


            pygame.display.update()
            self.clock.tick(60)

Game().main_menu()