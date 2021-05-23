import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")

from brick.Ball import Ball
from brick.Brick import Brick
from brick.Pad import Pad


# 結束程式
def gameover(message):
    # 顯示訊息
    text = ffont.render(message, 1, (255, 0, 255))
    screen.blit(text,
                (screen.get_width() / 2 - 150, screen.get_height() / 2 - 20))
    return False


pygame.init()
pygame.display.set_caption("Brick Game")
pygame.mouse.set_visible(False)
dfont = pygame.font.SysFont("Arial", 20)  # 下方訊息字體
ffont = pygame.font.SysFont("SimHei", 32)  # 結束程式訊息字體
screen = pygame.display.set_mode((600, 400))
background = pygame.Surface(screen.get_size()).convert().fill((255, 255, 255))
clock = pygame.time.Clock()

FPS = 60
score = 0  # 得分
downmsg = "Press Left Click Button to start game!"  # 起始訊息
playing = False  # 開始時球不會移動

allsprite = pygame.sprite.Group()  # 建立全部角色群組
bricks = pygame.sprite.Group()  # 建立磚塊角色群組

pad = Pad(screen)  # 建立滑板球物件
allsprite.add(pad)  # 加入全部角色群組

ball = Ball(5,
            screen.get_width() / 2, pad.rect.top - 10, 10, (255, 123, 188),
            screen)  # 建立粉球
allsprite.add(ball)  # 加入全部角色群組

# 建立磚塊
for row in range(0, 5):  # 5列方塊
    for column in range(0, 15):  # 每列15磚塊
        if row == 1 or row == 0:
            brick = Brick((153, 205, 255), column * 40 + 1,
                          row * 15 + 1)  # 位置為40*15
        if row == 2:
            brick = Brick((94, 175, 254), column * 40 + 1, row * 15 + 1)
        if row == 3 or row == 4:
            brick = Brick((52, 153, 207), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)  # 加入磚塊角色群組
        allsprite.add(brick)  # 加入全部角色群組

# 運行的程式碼
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            print(pygame.key.get_pressed().index(1))  # space = 44

    buttons = pygame.mouse.get_pressed()  # 檢查滑鼠按鈕
    if buttons[0]:  # 按滑鼠左鍵後球可移動
        playing = True

    # 遊戲進行中
    if playing == True:
        pad.update()  # 更新滑板位置

        # 檢查出界
        if ball.update():  # 移動球體:
            playing = gameover("You failed!See you next time~")

        # 檢查球和滑板碰撞
        hitpad = pygame.sprite.collide_rect(ball, pad)
        if hitpad:  # 球和滑板發生碰撞
            ball.bounceup()  # 球反彈

        # 檢查球和磚塊碰撞
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)
        if len(hitbrick) > 0:  # 球和磚塊發生碰撞
            score += len(hitbrick)  # 計算分數
            downmsg = "Score: " + str(score)
            # soundhit.play()  # 球撞磚塊聲
            ball.rect.y += 10  # 球向下移
            ball.bounceup()  # 球反彈
            if len(bricks) == 0:  # 所有磚塊消失
                playing = gameover("Congratulations!!")

    screen.blit(background, (0, 0))  # 清除繪圖視窗
    allsprite.draw(screen)  # 繪製所有角色
    message = dfont.render(downmsg, True, (255, 0, 255))  # 繪製下方訊息
    screen.blit(
        message,
        (screen.get_width() / 2 - 100, screen.get_height() - 30))  # 設定訊息位置
    pygame.display.update()
