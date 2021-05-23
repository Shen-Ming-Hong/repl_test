import math
import random
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()  # 建立時間元件
FPS = 60  # Frames per second.

ball = pygame.Surface((70, 70))
ball.fill(WHITE)
pygame.draw.circle(ball, BLUE, (35, 35), 35, 0)
rect = ball.get_rect()
rect.center = (random.randint(100, 250), random.randint(150, 250))  # 球隨機起始位置
x, y = rect.topleft  # 球左上角坐標
direction = random.randint(20, 70)  # 起始角度
radian = math.radians(direction)  # 轉為弳度
dx = 5 * math.cos(radian)  # 球水平運動速度
dy = -5 * math.sin(radian)  # 球垂直運動速度

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    rect.move_ip(dx, dy)
    if rect.left <= 0 or rect.right >= screen.get_width():  # 到達左右邊界
        dx *= -1  # 水平速度變號
    elif rect.top <= 1 or rect.bottom >= screen.get_height() - 1:  # 到達上下邊界
        dy *= -1  # 垂直速度變號

    screen.fill(WHITE)
    screen.blit(ball, rect.topleft)
    pygame.display.update()
