import pygame
pygame.init()  # 啟動 Pygame
screen = pygame.display.set_mode((320, 480))  # 建立繪圖視窗
pygame.display.set_caption("基本架構")  # 繪圖視窗標題
background = pygame.image.load("C:/Users/User/Downloads/20190911奇點創意-LOGO.png")
background = background.convert_alpha()
background = pygame.transform.smoothscale(background, (320, 320))
screen.blit(background, (12, 25))  # 在繪圖視窗繪製畫布
pygame.display.update()  # 更新繪圖視窗
running = True
while running:  # 無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False
pygame.quit()  # 關閉繪圖視窗
