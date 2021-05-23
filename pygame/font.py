import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

comicsansms = pygame.font.SysFont("comicsansms", 72)
# hello = comicsansms.render("Hello, World", True, (0, 128, 0))
hello = comicsansms.render("Hello, World", True, (0, 0, 255),
                           (0, 255, 0))  #綠色底，藍色字 (R,G,B)

screen.blit(hello,
            (320 - hello.get_width() // 2, 160 - hello.get_height() // 2))
#置中
pygame.display.update()  # 更新繪圖視窗

running = True
while running:  # 無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False
pygame.quit()  # 關閉繪圖視窗
