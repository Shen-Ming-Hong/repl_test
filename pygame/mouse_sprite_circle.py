import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
FPS = 60


class Block(pygame.sprite.Sprite):
    def __init__(self, color, bg_color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        # self.image.set_alpha(100)
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        self.rect = self.image.get_rect()

        pygame.draw.circle(self.image, color, [width // 2, height // 2],
                           min(width, height) // 2, 0)


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(WHITE, BLACK, 15, 15)

    # block.rect.x = random.randrange(screen_width)
    # block.rect.y = random.randrange(screen_height)
    block.rect.center = (random.randrange(screen.get_width()),
                         random.randrange(screen.get_height()))

    block_list.add(block)
    all_sprites_list.add(block)

player = Block(RED, BLACK, 15, 15)
all_sprites_list.add(player)

score = 0

pygame.mouse.set_visible(False)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(BLACK)

    player.rect.center = pygame.mouse.get_pos()

    # 為角色與群組碰撞偵測，最後布林值為碰撞後是否從所有群組移除該角色
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    all_sprites_list.draw(screen)

    pygame.display.update()
