import pygame

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode([800, 500])

FPSCLOCK = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    DISPLAYSURFACE.fill((200, 162, 200))
    pygame.display.set_caption("weeeeeee")

    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (300, 300), 20)
    pygame.display.update()

    FPSCLOCK.tick(30)



