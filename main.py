import pygame
from scripts.utils import draw_text, show_go_screen, pause_draw, draw_text2
from scripts.enteties import Mob, Player, Enemy, Button, PageType  # Player2
import sys


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.icon = pygame.image.load('image/icon.png')
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Wandering Black hole")

        self.screen = pygame.display.set_mode((1920, 1080))
        self.surface = pygame.Surface((1920, 1080), pygame.SRCALPHA)
        self.text_surface = pygame.Surface((650, 700))

        self.sound = True

        self.bg = pygame.image.load('image/backgroundfull2.png')
        self.bg2 = pygame.image.load('image/backgroundfull2.png')
        self.bg_x = 0
        self.bg_speed = 1
        self.title = pygame.image.load('image/title.png')

        self.stars = pygame.sprite.Group()
        self.holes = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        self.star_timer_tick = 3500
        self.hole_timer_tick = 18000

        self.star_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.star_timer, self.star_timer_tick)
        self.hole_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.hole_timer, self.hole_timer_tick)

        self.pages = [PageType.yellow_star.value, PageType.white_star.value, PageType.red_star.value,
                      PageType.blue_star.value, PageType.variable_star.value, PageType.neutron_star.value,
                      PageType.two_body.value, PageType.three_body.value, PageType.dyson_star.value,
                      PageType.stellar_hole.value, PageType.middle_hole.value, PageType.supermassive.value]
        self.page_num = 0

        self.score = 0

        self.gbutton = Button((1920/3), (1080/3 - 140), 200, 50, 'Начать', 'image/button.png', 'image/button (1).png')
        self.exitbutton = Button((1920/3), (1080/3 + 340), 200, 50, 'Выход', 'image/button.png', 'image/button (1).png')
        self.infobutton = Button((1920 / 3), (1080 / 3 + 100), 200, 50, 'Инфо', 'image/button.png',
                                 'image/button (1).png')
        self.backbutton = Button((1920 / 3 + 700), (1080 / 3 - 250), 200, 50, 'Назад', 'image/buttonmini.png',
                                 'image/buttonmini2.png')
        self.pastbutton = Button(200, 500, 200, 50, '', 'image/arrowleft.png', 'image/arrowleft2.png')
        self.nextbutton = Button(1600, 500, 200, 50, '', 'image/arrow button white.png',
                                 'image/arrow button black.png')
        pygame.mixer.music.load('audio/main_menu_theme.mp3')
        pygame.mixer.music.play(-1)

    def main_menu(self):
        running = True
        self.bg = pygame.image.load('image/backgroundfull2.png')
        while running:
            self.screen.blit(self.bg, (self.bg_x, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT and event.button == self.exitbutton:
                    pygame.quit()
                    sys.exit()
                self.exitbutton.handle_event(event)
                self.exitbutton.check_hover(pygame.mouse.get_pos())
                self.exitbutton.draw(self.screen)
                if event.type == pygame.USEREVENT and event.button == self.gbutton:
                    self.play()
                self.gbutton.handle_event(event)
                self.gbutton.check_hover(pygame.mouse.get_pos())
                self.gbutton.draw(self.screen)
                if event.type == pygame.USEREVENT and event.button == self.infobutton:
                    self.info(self.pages[self.page_num])
                self.infobutton.handle_event(event)
                self.infobutton.check_hover(pygame.mouse.get_pos())
                self.infobutton.draw(self.screen)
                pygame.display.update()

    def info(self, page_info):
        running = True
        self.bg = pygame.image.load('image/backgroundfull2.png')
        self.text_surface.fill((0, 0, 0))
        self.sound = False
        while running:
            self.screen.blit(self.bg, (self.bg_x, 0))
            self.screen.blit(page_info.image, page_info.rect)
            self.screen.blit(self.text_surface, (900, 300))
            draw_text(self.bg, page_info.name, page_info.size, page_info.x, 200)
            draw_text2(self.text_surface, page_info.text, 22, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT and event.button == self.backbutton:
                    self.main_menu()
                self.backbutton.handle_event(event)
                self.backbutton.check_hover(pygame.mouse.get_pos())
                self.backbutton.draw(self.screen)
                if event.type == pygame.USEREVENT and event.button == self.pastbutton:
                    if self.page_num == 0:
                        pass
                    else:
                        self.page_num -= 1
                    self.info(self.pages[self.page_num])
                self.pastbutton.handle_event(event)
                self.pastbutton.check_hover(pygame.mouse.get_pos())
                self.pastbutton.draw(self.screen)
                if event.type == pygame.USEREVENT and event.button == self.nextbutton:
                    if self.page_num == 11:
                        pass
                    else:
                        self.page_num += 1
                    self.info(self.pages[self.page_num])
                self.nextbutton.handle_event(event)
                self.nextbutton.check_hover(pygame.mouse.get_pos())
                self.nextbutton.draw(self.screen)
                pygame.display.update()
        self.clock.tick(60)

    def play(self):
        running = True
        game_over = False
        pause = False
        pygame.mixer.music.load('audio/untitled master.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while running:

            # Обнуляем все показатели для новой игры
            if game_over:
                show_go_screen(self.screen, self.bg, self.clock)
                game_over = False
                self.all_sprites = pygame.sprite.Group()
                self.stars = pygame.sprite.Group()
                self.holes = pygame.sprite.Group()
                self.player = Player()
                self.all_sprites.add(self.player)
                self.score = 0
                Mob.speedx = 8
                Mob.speedy = 0
                Player.speedy = 8
                Enemy.speedx = 7
                self.bg_speed = 1
                pygame.time.set_timer(self.star_timer, 3500)
            # пауза
            if pause:
                pause_draw(self.surface, self.screen)
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
                # for event in pygame.event.get():
                #     if event.type == pygame.KEYDOWN:
                #         if event.key == pygame.K_i:
                #             self.info(PageType.yellow_star.value)

            # вывод фонов
            self.screen.blit(self.bg, (self.bg_x, 0))
            self.screen.blit(self.bg, (self.bg_x + 1920, 0))

            # съедание черной дырой звезды
            hits = pygame.sprite.spritecollide(self.player, self.stars, True, pygame.sprite.collide_circle)
            if hits:
                self.score += 1
                if Mob.speedx <= 15:
                    Mob.speedx += 0.5
                if Player.speedy <= 15:
                    Player.speedy += 0.25
                if Enemy.speedx <= 14:
                    Enemy.speedx += 0.2
                if self.bg_speed <= 7:
                    self.bg_speed += 0.5
                if self.star_timer_tick >= 1800:
                    self.star_timer_tick -= 100
                    pygame.time.set_timer(self.star_timer, self.star_timer_tick)
            # съедание черной дыры другой дырой
            eats = pygame.sprite.spritecollide(self.player, self.holes, False, pygame.sprite.collide_circle)
            if eats:
                game_over = True
            # типа гравитация большой дыры
            gravity = pygame.sprite.spritecollide(self.player, self.holes, False, pygame.sprite.collide_circle_ratio(3))
            if gravity and not pause:
                if self.player.rect.centery > h.rect.centery:
                    self.player.rect.centery -= Player.speedy - 3
                elif self.player.rect.centery < h.rect.centery:
                    self.player.rect.centery += Player.speedy - 3
                if self.player.rect.centerx > h.rect.centerx:
                    self.player.rect.centerx -= Player.speedy - 5
                elif self.player.rect.centerx < h.rect.centerx:
                    self.player.rect.centerx += Player.speedy - 3
            elif not gravity and not pause:
                if self.player.rect.x > 500:
                    self.player.rect.x -= 8
                    if self.player.rect.x < 505:
                        self.player.rect.x = 500
                elif self.player.rect.x < 500:
                    self.player.rect.x += 8
                    if self.player.rect.x > 495:
                        self.player.rect.x = 500
            if self.player.rect.x < 200:
                self.player.rect.x = 200
            # гравитация маленькой дыры
            if self.stars:
                for mob in self.stars.sprites():
                    gravity2 = pygame.sprite.collide_circle_ratio(3)(self.player, mob)
                    if gravity2:
                        if mob.rect.centery > self.player.rect.centery:
                            mob.speedy += 3
                        elif mob.rect.centery < self.player.rect.centery:
                            mob.speedy -= 3
                        if mob.rect.centerx > self.player.rect.centerx:
                            mob.speedx += 3
                        elif mob.rect.centerx < self.player.rect.centerx:
                            mob.speedx -= 3
            if not pause:
                self.bg_x -= self.bg_speed
                if self.bg_x <= -1920:
                    self.bg_x = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if pause:
                            pause = False
                        else:
                            pause = True
                if event.type == self.star_timer and not pause:
                    m = Mob()
                    self.all_sprites.add(m)
                    self.stars.add(m)
                if event.type == self.hole_timer and not pause:
                    h = Enemy()
                    self.all_sprites.add(h)
                    self.holes.add(h)
            if not pause:
                self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            draw_text(self.screen, 'счет: ' + str(self.score), 30, 350, 150)
            pygame.display.update()
            self.clock.tick(60)


Game().main_menu()
