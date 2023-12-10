import pygame

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('scripts/Undertale_font.ttf', size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen(screen, bg, clock):
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

