import pygame

pygame.init()

BEIGE = (219, 203, 164)
GREY = (158, 153, 141)  # or (151, 151, 166)
BLACK = (41, 41, 59)
WHITE = (255, 253, 242)
GREEN = (61, 99, 58)
BLUE = (75, 75, 94)

DISPLAYSURFACE = pygame.display.set_mode([730, 400])
FPSCLOCK = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    DISPLAYSURFACE.fill(BLACK)
    pygame.display.set_caption("Hogwarts")

    pygame.draw.polygon(DISPLAYSURFACE, BEIGE, [(90, 260), (90, 349.5), (290, 349.5), (290, 220), (130, 220)])
    pygame.draw.lines(DISPLAYSURFACE, GREY, False, [(92, 258), (130, 220), (290, 220)], 5)  # grey line


    pygame.draw.rect(DISPLAYSURFACE, GREY, [90, 250, 10, 100])  # pillar 1
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(90, 250), (100, 250), (95, 240)])
    pygame.draw.rect(DISPLAYSURFACE, GREY, [130, 250, 10, 100])  # pillar 2
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(130, 250), (140, 250), (135, 240)])
    pygame.draw.rect(DISPLAYSURFACE, GREY, [170, 250, 10, 100])  # pillar 3
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(170, 250), (180, 250), (175, 240)])
    pygame.draw.rect(DISPLAYSURFACE, GREY, [210, 250, 10, 100])  # pillar 4
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(210, 250), (220, 250), (215, 240)])
    pygame.draw.rect(DISPLAYSURFACE, GREY, [250, 250, 10, 100])  # pillar 5
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(250, 250), (260, 250), (255, 240)])

    pygame.draw.line(DISPLAYSURFACE, GREY, (100, 260), (290, 260), 5)  # grey line
    pygame.draw.rect(DISPLAYSURFACE, BEIGE, [290, 190, 110, 160])  # main tower
    pygame.draw.line(DISPLAYSURFACE, GREY, (290, 349.5), (290, 200), 5)  # grey line
    pygame.draw.line(DISPLAYSURFACE, GREY, (400, 349.5), (400, 200), 5)
    pygame.draw.rect(DISPLAYSURFACE, BEIGE, [280, 117, 130, 80])  # main tower top
    pygame.draw.line(DISPLAYSURFACE, GREY, (280, 197), (292.5, 197), 5)  # grey line
    pygame.draw.line(DISPLAYSURFACE, GREY, (398, 197), (410, 197), 5)  # grey line
    pygame.draw.rect(DISPLAYSURFACE, BEIGE, [385, 40, 15, 50])  # main tower tiny tower
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(265, 117), (425, 117), (345, 10)])  # main tower triangle
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(383, 40), (401.5, 40), (392.25, 25)])  # tiny tower triangle
    pygame.draw.line(DISPLAYSURFACE, GREY, (277.5, 117), (277.5, 199), 5)  # grey line
    pygame.draw.line(DISPLAYSURFACE, GREY, (412.5, 117), (412.5, 199), 5)
    pygame.draw.rect(DISPLAYSURFACE, BEIGE, [400, 240, 215, 110])  # bridge
    pygame.draw.rect(DISPLAYSURFACE, BEIGE, [370, 270, 70, 80])  # other tower
    pygame.draw.polygon(DISPLAYSURFACE, GREY, [(370, 270), (440, 270), (405, 230)])  # other tower triangle
    pygame.draw.line(DISPLAYSURFACE, GREY, (373, 270), (373, 349.5), 5)  # grey line
    pygame.draw.line(DISPLAYSURFACE, GREY, (437, 270), (437, 349.5), 5)

    pygame.draw.rect(DISPLAYSURFACE, BLACK, [460, 285, 30, 80])  # bridge hole 1
    pygame.draw.circle(DISPLAYSURFACE, BLACK, [475, 285], 15)
    pygame.draw.rect(DISPLAYSURFACE, BLACK, [510, 285, 30, 80])  # bridge hole 2
    pygame.draw.circle(DISPLAYSURFACE, BLACK, [525, 285], 15)
    pygame.draw.rect(DISPLAYSURFACE, BLACK, [560, 285, 30, 80])  # bridge hole 3
    pygame.draw.circle(DISPLAYSURFACE, BLACK, [575, 285], 15)
    pygame.draw.line(DISPLAYSURFACE, GREY, (400, 240), (615, 240), 5)  # grey line
    pygame.draw.line(DISPLAYSURFACE, GREY, (615, 238.5), (615, 349.5), 5)

    pygame.draw.circle(DISPLAYSURFACE, WHITE, [50, 50], 1)  # star
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [150, 25], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [280, 45], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [200, 150], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [100, 100], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [40, 180], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [70, 280], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [500, 20], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [450, 100], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [410, 220], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [590, 150], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [700, 50], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [670, 250], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [500, 200], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [580, 300], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [520, 340], 1)
    pygame.draw.circle(DISPLAYSURFACE, WHITE, [710, 340], 1)

    pygame.draw.circle(DISPLAYSURFACE, WHITE, [600, 80], 20)  # moon
    pygame.draw.circle(DISPLAYSURFACE, BLACK, [590, 80], 20)

    #pygame.draw.ellipse(DISPLAYSURFACE, BLUE, [520, 80, 30, 10])  # cloud
    pygame.draw.rect(DISPLAYSURFACE, GREEN, [-10, 350, 750, 100], 0, 100)

    pygame.display.update()
    FPSCLOCK.tick(30)

