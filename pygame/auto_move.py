import pygame

pygame.init()

screen = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

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

x = 50  # 先在左邊
y = 400  # 固定
dx = 1  # 每次移動2個像素
walkCount = 0  # 用於圖片動畫顯示
wave = 50

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg, (0, 0))

    if walkCount + 1 >= 27:  # 這樣是為了移動三次，才換一個造型
        walkCount = 0
    if x > screen.get_width() - wave:  # 到達右邊界
        dx = -1
    if x < wave:  # 到達左邊界
        dx = 1
    if dx == 1:  # 向右走
        screen.blit(walkRight[walkCount // 3], (x, y))
    else:  # 向左走
        screen.blit(walkLeft[walkCount // 3], (x, y))

    x += dx
    walkCount += 1
    pygame.display.update()  # Or pygame.display.flip()
