import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((255, 255, 255))
#window.blit(robot, (0, 0)) #location
width = robot.get_width()
height = robot.get_height()
for h in range(10):
    for w in range(10):
        window.blit(robot, (width+45*w+10*h, height+30*h))
            
        

pygame.display.flip() # update the content

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


