import pygame
from random import randint
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = 350
y = 500

image_player = pygame.image.load('rocket.png').convert_alpha()
image_player2 = pygame.transform.scale(image_player, (75, 90))
mask_player = pygame.mask.from_surface(image_player2)
player_pos = [350, 500]

image_brick1 = pygame.image.load('brick.png').convert_alpha()
mask_brick = pygame.mask.from_surface(image_brick1)
brick_pos = [100, 200]

image_finish = pygame.image.load('finish.png').convert_alpha()
image_finish2 = pygame.transform.scale(image_finish, (125, 150))
mask_finish = pygame.mask.from_surface(image_finish2)
finish_pos = [325, -30]

image_background = pygame.image.load('space.png').convert_alpha()

offset1 = finish_pos[0] - player_pos[0], finish_pos[1] - player_pos[1]
offset2 = player_pos[0] - brick_pos[0], player_pos[1] - brick_pos[1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10


    if mask_player.overlap_mask(mask_brick, offset2):
            screen.blit(image_player2, (x, y))



    screen.blit(image_background, (0, 0))
    screen.blit(image_finish2, (325, -30))
    screen.blit(image_player2, (x, y))
    screen.blit(image_brick1, (100, 200))





    pygame.display.flip()
    clock.tick(60)


pygame.quit()
