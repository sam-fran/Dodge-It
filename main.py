import pygame
import random

SCREEN_W, SCREEN_H = 1000, 400
SPAWN_THRESHOLD = 1 - 1 / 40
MAX_ENEMIES = 14
ENEMY_SPEED = 160

pygame.init()
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Dodge It! (W/S to move)")
clock = pygame.time.Clock()

player_position = 0
enemies = []
score = 0

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, ENEMY_SPEED)

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_position > 0:
                player_position -= 1
            elif event.key == pygame.K_s and player_position < 7:
                player_position += 1

        elif event.type == MOVE_EVENT:
            for i in enemies[:]:
                if i[0] <= 0:
                    enemies.remove(i)
                    score = score + 1
                    pygame.display.set_caption(f"Dodge It! Score: {score}")
                elif i[0] == 50 and i[1]/50 == player_position:
                    pygame.display.set_caption("GAME OVER!")
                    pygame.time.set_timer(MOVE_EVENT, 0)
                else:
                    i[0] -= 50

    if random.random() > SPAWN_THRESHOLD and len(enemies) < MAX_ENEMIES and not game_over:
        enemies += [[950, random.randint(0, 7) * 50]]

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255, 255, 255), [50, player_position * 50, 50, 50], 0)

    for i in enemies:
        pygame.draw.rect(window, (255, 0, 100), [i[0], i[1], 50, 50], 0)

    pygame.display.update()
    clock.tick(60)

pygame.quit()