import pygame as pg
import random
import time

pg.mixer.init()

food_sound=pg.mixer.Sound('food.wav')
lvl_sound=pg.mixer.Sound('level.wav')

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

pg.init()
dis_width = 800
dis_height  = 600
dis=pg.display.set_mode((dis_width ,dis_height))
pg.display.update()
pg.display.set_caption("snake game")

font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("comicsansms", 35)

snake_block = 10


clock = pg.time.Clock()

def Your_score(score,level):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
    value_l = score_font.render("level : " + str(level), True, yellow)
    dis.blit(value_l, [0, dis_height/15])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 8
    level = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:

        while game_close == True:
                dis.fill((255,255,255))
                message("You Lost!  Press Q-Quit or C-Play Again", (255,0,0))
                Your_score(Length_of_snake - 1,level)
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
        dis.fill(blue)
        pg.draw.rect(dis, green , [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:           #if snake bites itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1,level)

        pg.display.update()

        if x1 == foodx and y1 == foody:
            food_sound.play()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if ((Length_of_snake-1)%10==0):
                snake_speed += 10
                level=(Length_of_snake-1)/10 + 1
                lvl_sound.play()



        clock.tick(snake_speed)


    pg.quit()
    quit()

gameLoop()

