import pygame

from maze import Maze

class Maze_Graphic:

    def __init__(self, canvas, maze):
        self.window = canvas
        self.data = maze

    def draw_cell(self, start, x, y, squareLength):

        if (x, y) in self.data.popped:
            top_x = start[0] + squareLength * x
            top_y = start[1] + squareLength * y
            size = squareLength + 1
            pygame.draw.rect(self.window, (150, 225, 0), (top_x, top_y, size, size))
        elif (x, y) in self.data.visited:
            top_x = start[0] + squareLength * x
            top_y = start[1] + squareLength * y
            size = squareLength + 1
            pygame.draw.rect(self.window, (150, 255, 225), (top_x, top_y, size, size))

        if self.data.cells[x][y].walls[0] == True:
            topLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
            topLineEnd = (topLineStart[0] + squareLength, topLineStart[1])
            pygame.draw.line(self.window, (0, 0, 0), topLineStart, topLineEnd, 1)

        if self.data.cells[x][y].walls[2] == True:
            bottomLineStart = (start[0] + squareLength * x, start[1] + squareLength * (y + 1))
            bottomLineEnd = (bottomLineStart[0] + squareLength, bottomLineStart[1])
            pygame.draw.line(self.window, (0, 0, 0), bottomLineStart, bottomLineEnd, 1)

        if self.data.cells[x][y].walls[3] == True:
            leftLineStart = (start[0] + squareLength * x, start[1] + squareLength * y)
            leftLineEnd = (leftLineStart[0], leftLineStart[1] + squareLength)
            pygame.draw.line(self.window, (0, 0, 0), leftLineStart, leftLineEnd, 1)

        if self.data.cells[x][y].walls[1] == True:
            rightLineStart = (start[0] + squareLength * (x + 1), start[1] + squareLength * y)
            rightLineEnd = (rightLineStart[0], rightLineStart[1] + squareLength)
            pygame.draw.line(self.window, (0, 0, 0), rightLineStart, rightLineEnd, 1)

    def draw_maze(self):
        width, height = self.window.get_size() # Update dimensions for drawing adjustments
        # Want to place maze with some padding for better appearance, so compute new inner canvas boundaries
        newWidth = width - (2 * width  * 0.1) # Add 10% padding
        newHeight = height - (2 * height * 0.1) # Add 10% padding
        start_x = width * 0.1
        start_y = height * 0.1
        # Get middle of canvas to help position the maze
        canvas_mid_x = width / 2
        canvas_mid_y = height / 2
        # Get length of each cell adjusted to screen dimensions
        squareLength = min(newWidth, newHeight) / self.data.size # Get size of square using minimal dimensions
        # Get the middle part of the maze to help place in middle of screen
        maze_mid_x = start_x + ((squareLength * self.data.size) / 2)
        maze_mid_y = start_y + ((squareLength * self.data.size) / 2)
        # Adjust maze to the middle of screen, no matter the dimensions
        start  = (start_x + (canvas_mid_x - maze_mid_x), (start_y + (canvas_mid_y - maze_mid_y))) # Padding for maze

        for y in range(0, self.data.size):
            for x in range(0, self.data.size):
                self.draw_cell(start, x, y, squareLength)
