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
    start  = (100,100) # Padding for maze
    squareLength = (900 - 200) / 50 # Get size of square and account for padding

    for y in range(0, maze.length):
        for x in range(0, maze.width):
            draw_cell(window, maze, start, x, y, squareLength)

pygame.init()
size = width, height = 900, 900
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

# Create maze
maze = Maze(50, 50)
maze.generate()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill(white)
        draw_maze(screen, maze)
        pygame.display.flip()
