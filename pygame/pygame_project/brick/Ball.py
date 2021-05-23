import pygame
import random
import math


# 建立球體
class Ball(pygame.sprite.Sprite):
    dx = 0  # x位移量
    dy = 0  # y位移量
    x = 0  # 球x坐標
    y = 0  # 球y坐標
    direction = 0  # 球移動方向
    speed = 0  # 球移動速度

    def __init__(self, sp, srx, sry, radium, color, screen):
        super().__init__()
        self.screen = screen
        self.speed = sp
        self.x = srx
        self.y = sry
        # 繪製球體
        self.image = pygame.Surface([radium * 2, radium * 2])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pygame.draw.circle(self.image, color, (radium, radium), radium, 0)
        self.rect = self.image.get_rect()  # 取得球體區域
        self.rect.center = (srx, sry)  # 初始位置
        self.direction = random.randint(20, 70)  # 移動角度

    # 球體移動
    def update(self):
        radian = math.radians(self.direction)  # 角度轉為弳度
        self.dx = self.speed * math.cos(radian)  # 球水平運動速度
        self.dy = -self.speed * math.sin(radian)  # 球垂直運動速度
        self.rect.move_ip(self.dx, self.dy)

        # 到達左右邊界
        if self.rect.left <= 0 or self.rect.right >= (self.screen.get_width() -
                                                      10):
            self.bouncelr()
        elif self.rect.top <= 10:  # 到達上邊界
            self.rect.top = 10
            self.bounceup()
        if self.rect.bottom >= self.screen.get_height() - 30:  # 到達下邊界出界
            return True
        else:
            return False

    def bounceup(self):  # 上邊界反彈
        self.direction = 360 - self.direction

    def bouncelr(self):  # 左右邊界反彈
        self.direction = 360 - self.direction + 180
