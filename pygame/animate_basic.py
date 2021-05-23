import pygame
pygame.init()

# 設定視窗
width, height = 640, 480  # 寬、高的變數，方便後修改
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My's game")
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg, (0, 0))
    pygame.display.update()  # Or pygame.display.flip()
