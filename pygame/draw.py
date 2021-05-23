import pygame
pygame.init()  # 啟動 Pygame
screen = pygame.display.set_mode((320, 480))  # 建立繪圖視窗
pygame.display.set_caption("基本架構")  # 繪圖視窗標題
background = pygame.Surface(screen.get_size())  # 建立畫布
background = background.convert()
background.fill((255, 255, 255))  # 畫布為白色

# pygame.draw.rect(background, (255,0,0),[160, 160, 80, 50], 2)
# pygame.draw.circle(background, (0, 0, 255), (100, 100), 50, 0)
# pygame.draw.ellipse(background, (0, 255, 0), [100, 100, 120, 70], 5)
# pygame.draw.arc(background, (255,0,0), [ 100, 100, 150, 150], 0, 3.14, 5)
pygame.draw.line(background, (255, 0, 255), (100, 100), (300, 400), 3)

screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布
pygame.display.update()  # 更新繪圖視窗

running = True
while running:  # 無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False
pygame.quit()  # 關閉繪圖視窗
