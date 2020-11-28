import pygame as pg
import random
import time

pg.init()
dis_width = 800
dis_height  = 600
dis=pg.display.set_mode((dis_width ,dis_height))
pg.display.update()
pg.display.set_caption("snake game")

snake_block = 10
clock = pg.time.Clock()
snake_speed = 30

font_style = pg.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/8, dis_height/3])

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:

        while game_close == True:
                dis.fill((255,255,255))
                message("You Lost!  Press Q-Quit or C-Play Again", (255,0,0))
                pg.display.update()

                for event in pg.event.get():

                    if event.type==pg.QUIT:
                        game_over=True
                        game_close=False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pg.K_c:
                            gameLoop()

        for event in pg.event.get():
            if event.type==pg.QUIT:
                game_over=True
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill([255,255,255])
        pg.draw.rect(dis,(0,0,0),[x1,y1,snake_block,snake_block])
        pg.draw.rect(dis, (0,0,255), [foodx, foody, snake_block, snake_block])
        pg.display.update()
        clock.tick(snake_speed)

    pg.quit()
    quit()

gameLoop()

