import pygame, random
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((255, 255, 255))
#window.blit(robot, (0, 0)) #location
width = robot.get_width()
heigh = robot.get_height()
for w in range(1000):
    window.blit(robot, (random.randint(0, 640-width), random.randint(0, 480-heigh)))

    
            
        

pygame.display.flip() # update the content

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


