import pygame as pg
pg.init()
dis=pg.display.set_mode((400,300))
pg.display.update()
pg.display.set_caption("snake game")
game_over=False
while not game_over:
    for event in pg.event.get():
        print(event)

pg.quit()
quit()

