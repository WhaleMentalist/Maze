import sys, time, pygame

from maze import *

def draw(canvas, graphical_maze):
    canvas.fill((255, 255, 255))
    graphical_maze.draw_maze()

pygame.init()
canvas = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Create maze and display original
maze = Maze(20)
maze_cell_generator = maze.generate_single_cell()
graphical_maze = Graphical_Maze(canvas, maze)
draw(canvas, graphical_maze)
pygame.display.flip()

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
    maze = maze_cell_generator.next() # Generate next part of maze
    time.sleep(0.05)

# Quit
pygame.quit()
