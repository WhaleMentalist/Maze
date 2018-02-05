import pygame

from maze import Maze

class Maze_Graphic:

    def __init__(self, canvas, maze):
        self.window = canvas
        self.data = maze

    def draw_cell(self, start, x, y, squareLength):
        if self.data.cells[x][y].walls[0] == True:
            topLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
            topLineEnd = (topLineStart[0] + squareLength, topLineStart[1])
            pygame.draw.line(self.window, (0, 0, 0), topLineStart, topLineEnd, 2)

        if self.data.cells[x][y].walls[2] == True:
            bottomLineStart = (start[0] + squareLength * x, start[1] + squareLength * (y + 1))
            bottomLineEnd = (bottomLineStart[0] + squareLength, bottomLineStart[1])
            pygame.draw.line(self.window, (0, 0, 0), bottomLineStart, bottomLineEnd, 2)

        if self.data.cells[x][y].walls[3] == True:
            leftLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
            leftLineEnd = (leftLineStart[0], leftLineStart[1] + squareLength)
            pygame.draw.line(self.window, (0, 0, 0), leftLineStart, leftLineEnd, 2)

        if self.data.cells[x][y].walls[1] == True:
            rightLineStart = (start[0] + squareLength * (x + 1), start[1] + squareLength * y)
            rightLineEnd = (rightLineStart[0], rightLineStart[1] + squareLength)
            pygame.draw.line(self.window, (0, 0, 0), rightLineStart, rightLineEnd, 2)

    def draw_maze(self):
        width, height = self.window.get_size()
        ratio = float(width) / height # Ratio of screen dimensions
        newWidth = width - (2 * width  * 0.1) # Add 10% padding
        newHeight = height - (2 * height * 0.1) # Add 10% padding

        start_x = width * 0.1
        end_x = width * 0.9
        start_y = height * 0.1

        squareLength = min(newWidth, newHeight) / self.data.size # Get size of square using minimal dimensions
        start  = ((end_x - (squareLength * self.data.size)) / ratio, start_y) # Padding for maze

        for y in range(0, self.data.size):
            for x in range(0, self.data.size):
                self.draw_cell(start, x, y, squareLength)
