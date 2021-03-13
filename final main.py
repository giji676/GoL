from pynput import mouse
import random
import pygame

FPS = 60
ORIGINAL_FPS = 60
SLOW_FPS = 30
WIDTH, HEIGHT = 1600, 800
RESOLUTION = 50

GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")


def draw_grid(win, cols, rows):
    for i in range(cols):
        for j in range(rows):
            x = i * RESOLUTION
            y = j * RESOLUTION
            pygame.draw.rect(win, GRAY, (x, y, RESOLUTION, RESOLUTION), 1)


def make_2d_array(cols, rows):
    arr = []
    for i in range(cols):
        arr.append([])
        for j in range(rows):
            arr[i].append(0)

    return arr


def count_neighbours(grid, x, y):
    neighbourCount = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                neighbourCount += grid[x + i][y + j]

    return neighbourCount


def draw_squares(win, grid, cols, rows):
    nextA = make_2d_array(cols, rows)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = i * RESOLUTION
            y = j * RESOLUTION
            if grid[i][j] == 1:
                pygame.draw.rect(win, WHITE, (x, y, RESOLUTION, RESOLUTION))
            else:
                pygame.draw.rect(win, BLACK, (x, y, RESOLUTION, RESOLUTION))

    for i in range(cols):
        for j in range(rows):

            if i == 0 or i == cols-1 or j == 0 or j == rows-1:
                nextA[i][j] = grid[i][j]
            else:
                state = grid[i][j]
                neighbours = count_neighbours(grid, i, j)

                if state == 0 and neighbours == 3:
                    nextA[i][j] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    nextA[i][j] = 0
                else:
                    nextA[i][j] = state
    return nextA


def inputs(win, grid, button):
    pos = pygame.mouse.get_pos()
    x = pos[0]//RESOLUTION
    y = pos[1]//RESOLUTION

    if button == "MB1":
        if grid[x][y] == 0:
            grid[x][y] = 1
            pygame.draw.rect(win, WHITE, (x*RESOLUTION, y*RESOLUTION, RESOLUTION, RESOLUTION))

    if button == "MB2":
        if grid[x][y] == 1:
            grid[x][y] = 0
            pygame.draw.rect(win, BLACK, (x*RESOLUTION, y*RESOLUTION, RESOLUTION, RESOLUTION))
    return grid


def update_Squares(win, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = i * RESOLUTION
            y = j * RESOLUTION
            if grid[i][j] == 1:
                pygame.draw.rect(win, WHITE, (x, y, RESOLUTION, RESOLUTION))
            else:
                pygame.draw.rect(win, BLACK, (x, y, RESOLUTION, RESOLUTION))


def main():
    global FPS
    run = True
    run_generations = False
    clock = pygame.time.Clock()

    cols = int(WIDTH / RESOLUTION)
    rows = int(HEIGHT / RESOLUTION)

    grid = make_2d_array(cols, rows)

    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        mouse_events = pygame.mouse.get_pressed()

        if mouse_events[0]:
            grid = inputs(WIN, grid, "MB1")

        if mouse_events[2]:
            grid = inputs(WIN, grid, "MB2")

        if key[pygame.K_s]:
            run_generations = True
            FPS = SLOW_FPS

        if key[pygame.K_t]:
            run_generations = False
            FPS = ORIGINAL_FPS

        if key[pygame.K_c]:
            grid = make_2d_array(cols, rows)
            update_Squares(WIN, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if run_generations:
            grid = draw_squares(WIN, grid, cols, rows)
        draw_grid(WIN, cols, rows)
        pygame.display.update()

    pygame.quit()


main()
