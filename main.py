from config import WIDTH, HEIGHT
from case import Case

from tkinter import *
from perlin_noise import PerlinNoise

altitude_noise = PerlinNoise(octaves=5)
altitude_noise = [[altitude_noise([i / WIDTH, j / HEIGHT]) for j in range(WIDTH)] for i in
                  range(HEIGHT)]

root = Tk()
canvas = Canvas(root, bg="#dcdcdc", height=HEIGHT, width=WIDTH)
canvas.pack()

GRID = [[0 for y in range(HEIGHT)] for x in range(WIDTH)]


def fill():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if altitude_noise[i][j] <= -0.15:
                GRID[i][j] = Case(i, j, 'DEEP_WATER')
            elif altitude_noise[i][j] <= 0:
                GRID[i][j] = Case(i, j, 'WATER')
            elif altitude_noise[i][j] <= 0.1:
                GRID[i][j] = Case(i, j, 'SAND')
            elif altitude_noise[i][j] <= 0.2:
                GRID[i][j] = Case(i, j, 'GRASS')
            elif altitude_noise[i][j] <= 0.35:
                GRID[i][j] = Case(i, j, 'WOOD')
            elif altitude_noise[i][j] <= 0.45:
                GRID[i][j] = Case(i, j, 'STONE')
            else:
                GRID[i][j] = Case(i, j, 'SNOW')

            GRID[i][j].draw(canvas)


fill()

mainloop()
