import pygame
import random
import math

pygame.init()

# 設定視窗背景
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("mouse move ball")
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

# 藍球建立
ball = pygame.Surface((70, 70))
ball.fill((255, 255, 255))
pygame.draw.circle(ball, (0, 0, 255), (35, 35), 35, 0)
rect = ball.get_rect()
rect.center = (320, 240)
x, y = rect.topleft

clock = pygame.time.Clock()
FPS = 60

playing = False  # 開始時球不能移動
while True:
    clock.tick(FPS)  # 每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    buttons = pygame.mouse.get_pressed()
    if buttons[0]:  # 按滑鼠左鍵後球可移動
        playing = True
    elif buttons[2]:  # 按滑鼠右鍵後球不能移動
        playing = False

    if playing == True:  # 球可移動狀態
        rect.center = pygame.mouse.get_pos()  # 取得滑鼠坐標

    screen.blit(bg, (0, 0))
    screen.blit(ball, rect.topleft)
    pygame.display.update()
