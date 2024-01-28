import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Game")
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Robot
robot_image = pygame.image.load("robot.png")
robot_rect = robot_image.get_rect()
robot_rect.centerx = WIDTH // 2
robot_rect.bottom = HEIGHT - 10
# Coins and Monsters
coin_image = pygame.image.load("coin.png")
monster_image = pygame.image.load("monster.png")
coins = []
monsters = []
# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game variables
score = 0
game_over = False

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def spawn_coin():
    coin_rect = coin_image.get_rect()
    coin_rect.x = random.randint(0, WIDTH - coin_rect.width)
    coin_rect.y = -coin_rect.height
    coins.append(coin_rect)

def spawn_monster():
    monster_rect = monster_image.get_rect()
    monster_rect.x = random.randint(0, WIDTH - monster_rect.width)
    monster_rect.y = -monster_rect.height
    monsters.append(monster_rect)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and robot_rect.left > 0:
        robot_rect.x -= 10
    if keys[pygame.K_RIGHT] and robot_rect.right < WIDTH:
        robot_rect.x += 10

    # Update game elements
    for coin_rect in coins:
        coin_rect.y += 5
        if coin_rect.colliderect(robot_rect):
            coins.remove(coin_rect)
            score += 1

    for monster_rect in monsters:
        monster_rect.y += 5
        if monster_rect.colliderect(robot_rect):
            game_over = True

    # Spawn new coins and monsters
    if random.randint(0, 100) < 5:
        spawn_coin()

    if random.randint(0, 100) < 2:
        spawn_monster()

    # Draw background
    screen.fill(WHITE)

    # Draw robot
    screen.blit(robot_image, robot_rect)

    # Draw coins
    for coin_rect in coins:
        screen.blit(coin_image, coin_rect)

    # Draw monsters
    for monster_rect in monsters:
        screen.blit(monster_image, monster_rect)
    
    draw_text(f"Score: {score}", 10, 10, RED) # Draw score

    pygame.display.flip() # Update display
    clock.tick(60) # Set the frames per second

pygame.quit() # Quit Pygame
sys.exit()






