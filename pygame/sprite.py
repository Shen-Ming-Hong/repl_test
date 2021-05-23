import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500, 480))

pygame.display.set_caption("sprite 範例")

walkRight = [
    pygame.image.load('./game/R1.png'),
    pygame.image.load('./game/R2.png'),
    pygame.image.load('./game/R3.png'),
    pygame.image.load('./game/R4.png'),
    pygame.image.load('./game/R5.png'),
    pygame.image.load('./game/R6.png'),
    pygame.image.load('./game/R7.png'),
    pygame.image.load('./game/R8.png'),
    pygame.image.load('./game/R9.png')
]

walkLeft = [
    pygame.image.load('./game/L1.png'),
    pygame.image.load('./game/L2.png'),
    pygame.image.load('./game/L3.png'),
    pygame.image.load('./game/L4.png'),
    pygame.image.load('./game/L5.png'),
    pygame.image.load('./game/L6.png'),
    pygame.image.load('./game/L7.png'),
    pygame.image.load('./game/L8.png'),
    pygame.image.load('./game/L9.png')
]

bg = pygame.image.load('./game/bg.jpg')

clock = pygame.time.Clock()
FPS = 50  # Frames per second.
wave = 50


class player(pygame.sprite.Sprite):
    def __init__(self, x, dx, y):
        super().__init__()
        self.walkCount = 0
        self.image = walkRight[self.walkCount // 3]
        # 回傳位置
        self.rect = self.image.get_rect()
        # 定位
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.dx = dx

    def draw(self):
        if self.walkCount + 1 >= 27:  # 這樣是為了移動三次，才換一個造型
            self.walkCount = 0

        if self.x > screen.get_width() - wave or self.x < wave:  # 到達右邊界 或 左邊界
            self.dx *= -1  # 水平速度變號

        if self.dx > 0:  # 向右走
            self.image = walkRight[self.walkCount // 3]
        else:  # 向左走
            self.image = walkLeft[self.walkCount // 3]

        self.rect.center = (self.x, self.y)
        self.x += self.dx
        self.walkCount += 1


# 亂數建立三個在不同位子的呆子，把他們存在man中
mans = [
    player(random.randint(50, 300), 1, random.randint(200, 400)),
    player(random.randint(50, 300), -1, random.randint(200, 400)),
    player(random.randint(50, 300), 2, random.randint(200, 400))
]

# 建立角色群組
allMan = pygame.sprite.Group()
# 將他們依序加入角色群組
for man in mans:
    allMan.add(man)
    print(man)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg, (0, 0))

    # if pygame.sprite.collide_rect(mans[0], mans[1]):
    #     mans[0].dx *= -1
    #     mans[1].dx *= -1

    for man in mans:
        man.draw()

    allMan.draw(screen)
    pygame.display.update()
