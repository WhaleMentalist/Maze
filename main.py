import sys, time, pygame

from maze import Maze
from maze_graphic import Maze_Graphic

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Create maze
maze = Maze(90)
maze.generate()
running = True

while running:
    # Event checking and response
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    # Drawing
    screen.fill(white)
    maze_graphic = Maze_Graphic(screen, maze)
    maze_graphic.draw_maze()
    pygame.display.flip()

# Quit
pygame.quit()
