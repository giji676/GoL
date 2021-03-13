from pynput import mouse
import random
import pygame

FPS = 500
WIDTH, HEIGHT = 1640, 1000
SQUARE_WIDTH = 40

GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GoL")

def get_neighbours(x, y, alive):
    alive_neighbours = 0
    neighbours = []
    #0 0 0
    #0 1 0
    #0 0 0
    """
    x0y0 = [x-40, y-40]
    x1y0 = [x, y-40]
    x2y0 = [x+40, y-40]

    x0y1 = [x - 40, y]
    x2y1 = [x + 40, y + 40]

    x0y2 = [x - 40, y + 40]
    x1y2 = [x, y + 40]
    x2y2 = [x + 40, y + 40]
    """

    neighbours.append([x-40, y-40]) ## y0
    neighbours.append([x, y-40])
    neighbours.append([x+40, y-40])
    neighbours.append([x-40, y])    ## y1
    neighbours.append([x+40, y+40])
    neighbours.append([x-40, y+40]) ## y2
    neighbours.append([x, y+40])
    neighbours.append([x+40, y+40])

    for i in neighbours:
        for j in alive:
            if i[0] == j[0] and i[1] == j[1]:
                alive_neighbours += 1

    return alive_neighbours

def rule_1(x, y, alive):
    for pos in alive:
        if pos[0] == x and pos[1] == y:
            neighbours = get_neighbours(x,y, alive)
            if neighbours <= 1:
                print(pos)
                alive.remove(pos)


def rule_2():
    pass

def rule_3():
    pass

def rule_4():
    pass


def game_logic(win, alive):
    for y in range(HEIGHT//SQUARE_WIDTH):
        for x in range(WIDTH//SQUARE_WIDTH):
            rule_1(x, y, alive)
            #print(x,y,alive)
            rule_2()
            rule_3()
            rule_4()


def draw_grid(win):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if x*SQUARE_WIDTH >= WIDTH:
                break
            rect = pygame.Rect(x*SQUARE_WIDTH, y*SQUARE_WIDTH, SQUARE_WIDTH, SQUARE_WIDTH)
            pygame.draw.rect(win, GRAY, rect, 1)


def draw_squares(win, alive):
    """for i in alive:
        pygame.draw.rect(win, WHITE, (i[0], i[1], SQUARE_WIDTH, SQUARE_WIDTH))"""
    pygame.draw.rect(win, WHITE, (alive[-0][0], alive[-0][1], SQUARE_WIDTH, SQUARE_WIDTH))


def inputs(win, pos, alive):
    small_posX = pos[0]//SQUARE_WIDTH
    small_posY = pos[1]//SQUARE_WIDTH

    if len(alive) == 0:
        alive.append([small_posX*SQUARE_WIDTH, small_posY*SQUARE_WIDTH])
    else:
        for block in alive:
            if block[0] == small_posX*SQUARE_WIDTH and block[1] == small_posY*SQUARE_WIDTH:
                return
        alive.append([small_posX*SQUARE_WIDTH, small_posY*SQUARE_WIDTH])


    # fri 1900
    # sun


def main():
    alive = []
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        mouse_events = pygame.mouse.get_pressed()
        if mouse_events[0]:
            inputs(WIN, pygame.mouse.get_pos(), alive)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_squares(WIN, alive)
        game_logic(WIN, alive)
        draw_grid(WIN)

        pygame.display.update()

    pygame.quit()


main()
