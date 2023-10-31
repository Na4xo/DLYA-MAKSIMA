import pygame as pg

W = 800
H = 600
game_over = False 

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("DZ")


x = 0
y = 0
praviy_glaz_x = W / 4 + 17
oko_prav_y = H / 2 - 26
leviy_glaz_x = W / 4 - 78
oko_lev_y = H / 2 - 25

r = 6
COLOR_GREEN = (255, 255, 255)
COLOR_RED = (0, 0, 0)
COLOR_BLACK = (255, 0, 0)
COLOR_WHITE = ((255,100,10))

clock = pg.time.Clock()

while not game_over:
    screen.fill(COLOR_RED)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == 27 or event.type == pg.QUIT:
            game_over = True
    if x > W - 200:
        x = -200
    if praviy_glaz_x > W -20:
        praviy_glaz_x = -20
    if leviy_glaz_x > W -70:
        leviy_glaz_x = -70
             
    x += 5
    leviy_glaz_x += 5
    praviy_glaz_x += 5
        

    
    pg.draw.rect(screen, COLOR_GREEN, (x + 50, 250, 200, 200,))
    pg.draw.rect(screen, COLOR_BLACK, (x + 100,350, 150, 50,))
    pg.draw.rect(screen, COLOR_RED, (x + 150, 350, 80, 20,))
    pg.draw.rect(screen, COLOR_WHITE, (x + 150, 380, 80, 20,))
    

    pg.draw.circle(screen,(200, 12, 12), (praviy_glaz_x, oko_prav_y), r)
    pg.draw.circle(screen,(200, 12, 12), (leviy_glaz_x, oko_lev_y), r)

    

    pg.display.update()
    clock.tick(60)