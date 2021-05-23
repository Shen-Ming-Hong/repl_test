import pygame

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Ball follow mouse example")
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
FPS = 60

pygame.mouse.set_visible(False)  # 使系統鼠標圖標不可見

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        # 如果按下滑鼠
        # get_pressed() 告訴您按下哪個鼠標按鈕
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse pressed", pygame.mouse.get_pressed())
            print(type(pygame.mouse.get_pressed()))
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            print("mouse released", pygame.mouse.get_pressed())
        # 如果鼠標在運動中
        # get_rel() - 返回自上次調用此函數以來X和Y的移動量
        if event.type == pygame.MOUSEMOTION:
            print("mouse is moving", pygame.mouse.get_rel())

    screen.fill(white)

    # 在滑鼠周圍畫一個圓
    pygame.draw.circle(screen, black, pygame.mouse.get_pos(), 10, 0)

    pygame.display.update()
