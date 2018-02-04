import time

from graphics import *
from maze import Maze


def draw_cell(window, maze, start, x, y, squareLength):
    if maze.cells[x][y].walls[0] == True:
        topLineStart = Point(start.x + squareLength * x, start.y + squareLength * y)
        topLineEnd = Point(topLineStart.x + squareLength, topLineStart.y)
        line = Line(topLineStart, topLineEnd)
        line.setWidth(2)
        line.draw(window)

    if maze.cells[x][y].walls[2] == True:
        bottomLineStart = Point(start.x + squareLength * x, start.y + squareLength * (y + 1))
        bottomLineEnd = Point(bottomLineStart.x + squareLength, bottomLineStart.y)
        line = Line(bottomLineStart, bottomLineEnd)
        line.setWidth(2)
        line.draw(window)

    if maze.cells[x][y].walls[3] == True:
        leftLineStart = Point(start.x + squareLength * x, start.y + squareLength * y)
        leftLineEnd = Point(leftLineStart.x, leftLineStart.y + squareLength)
        line = Line(leftLineStart, leftLineEnd)
        line.setWidth(2)
        line.draw(window)

    if maze.cells[x][y].walls[1] == True:
        rightLineStart = Point(start.x + squareLength * (x + 1), start.y + squareLength * y)
        rightLineEnd = Point(rightLineStart.x, rightLineStart.y + squareLength)
        line = Line(rightLineStart, rightLineEnd)
        line.setWidth(2)
        line.draw(window)

def draw_maze(window, maze):
    start  = Point(100,100) # Padding for maze
    squareLength = (900 - 200) / 30 # Get size of square and account for padding

    for y in range(0, maze.length):
        for x in range(0, maze.width):
            draw_cell(window, maze, start, x, y, squareLength)


maze = Maze(30,30)
maze.generate()
window = GraphWin('Maze', 900, 900)
draw_maze(window, maze)

window.getMouse()
window.close()
