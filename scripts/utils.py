import pygame

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('scripts/Undertale_font.ttf', size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def draw_text2(surf, text, size, x, y):
    font = pygame.font.Font('scripts/Undertale_font.ttf', size)
    with open(text, 'r', encoding="utf-8") as file:
        txt = file.read()
    blit_text(surf, txt, (x, y), font)

def show_go_screen(screen, bg, clock):
    pygame.mixer.music.pause()
    screen.blit(bg, (0, 0))
    draw_text(screen, "Игра окончена!", 64, 1940 / 2, 1080 / 2 - 30)
    draw_text(screen, "нажмите пробел, чтобы продолжить", 44, 1940 / 2, 1080 / 2 + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                waiting = False
def pause_draw(surface, screen):
    pygame.draw.rect(surface, (0, 0, 0, 150), [0, 0, 1920, 1080])
    screen.blit(surface, (0, 0))
    draw_text(screen, 'Пауза', 64, 1940 / 2, 1080 / 2 - 30)
    pygame.display.update()
