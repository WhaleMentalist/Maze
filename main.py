import sys, time, pygame

from maze import Maze

def draw_cell(window, maze, start, x, y, squareLength):
    if maze.cells[x][y].walls[0] == True:
        topLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
        topLineEnd = (topLineStart[0] + squareLength, topLineStart[1])
        pygame.draw.line(window, (0, 0, 0), topLineStart, topLineEnd, 2)

    if maze.cells[x][y].walls[2] == True:
        bottomLineStart = (start[0] + squareLength * x, start[1] + squareLength * (y + 1))
        bottomLineEnd = (bottomLineStart[0] + squareLength, bottomLineStart[1])
        pygame.draw.line(window, (0, 0, 0), bottomLineStart, bottomLineEnd, 2)

    if maze.cells[x][y].walls[3] == True:
        leftLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
        leftLineEnd = (leftLineStart[0], leftLineStart[1] + squareLength)
        pygame.draw.line(window, (0, 0, 0), leftLineStart, leftLineEnd, 2)

    if maze.cells[x][y].walls[1] == True:
        rightLineStart = (start[0] + squareLength * (x + 1), start[1] + squareLength * y)
        rightLineEnd = (rightLineStart[0], rightLineStart[1] + squareLength)
        pygame.draw.line(window, (0, 0, 0), rightLineStart, rightLineEnd, 2)

def draw_maze(window, maze):
    width, height = window.get_size()
    ratio = float(width) / height # Ratio of screen dimensions
    newWidth = width - (2 * width  * 0.1) # Add 10% padding
    newHeight = height - (2 * height * 0.1) # Add 10% padding

    start_x = width * 0.1
    end_x = width * 0.9
    start_y = height * 0.1

    squareLength = min(newWidth, newHeight) / maze.size # Get size of square using minimal dimensions
    start  = ((end_x - (squareLength * maze.size)) / ratio, start_y) # Padding for maze

    for y in range(0, maze.size):
        for x in range(0, maze.size):
            draw_cell(window, maze, start, x, y, squareLength)

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Create maze
maze = Maze(30)
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
    draw_maze(screen, maze)
    pygame.display.flip()

# Quit
pygame.quit()
