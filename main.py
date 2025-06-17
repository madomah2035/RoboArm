import pygame as pg
# import numpy as np
# import pygame.display

pg.init()

HEIGHT, WIDTH = 1000, 800

screen = pg.display.set_mode((HEIGHT, WIDTH))
pg.display.set_caption("RoboArm: Robotic Arm Display.")

char = pg.Rect((500, 400, 73, 37))

run = True
while run:

    screen.fill((0, 1, 0))

    pg.draw.rect(screen, (255, 255, 255), char)

    key = pg.key.get_pressed()
    if key[pg.K_DOWN]:
        char.move_ip(0, 1)
    elif key[pg.K_UP]:
        char.move_ip(0, -1)
    elif key[pg.K_LEFT]:
        char.move_ip(-1, 0)
    elif key[pg.K_RIGHT]:
        char.move_ip(1, 0)

    for action in pg.event.get():
        if action.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()
