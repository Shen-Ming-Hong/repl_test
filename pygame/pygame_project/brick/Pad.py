import pygame


# 板子類別
class Pad(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # self.image = pygame.image.load("media\\pad.png")  # 滑板圖片
        self.image = pygame.Surface([38, 13])
        # self.image.convert()
        self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = int(
            (self.screen.get_width() - self.rect.width) / 2)  # 滑板位置
        self.rect.y = self.screen.get_height() - self.rect.height - 30

    # 板子位置隨滑鼠移動
    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]  # 滑鼠x坐標
        # 不要移出右邊界
        if self.rect.x > self.screen.get_width() - self.rect.width:
            self.rect.x = self.screen.get_width() - self.rect.width
