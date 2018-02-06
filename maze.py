import random, pygame

class Observable:

    def __init_(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    # Notifies observers, which cell was changed and whether it was backtracked
    # or explored
    def notify_cell_changed(self, cell, state):
        [observer.on_cell_changed(cell, state) for observer in self.observers]

class Observer:

    # Handle cell change events from observable
    def on_cell_changed(self, cell, state):
        pass

class Maze(Observable):

    def __init__(self, size = 5):
        self.size = size
        self.observers = []

        self.cells = [] # Hold representation of maze as 2D grid
        for x in range(0, self.size):
            self.cells.append([]) # Append empty row to add columns to
            for y in range(0, self.size):
                self.cells[x].append(Cell(x,y))

    # Generator for dynamic drawing of maze generation on canvas.
    # Yield will maintain the previous state, much like a stack in
    # recursion
    def generate_single_cell(self):
        visited = set() # Track visited cells, useful for checking quickly for unvisited neighbors
        stack = [] # Stack to hold explored cells

        visited.add((0, 0))
        stack.append(self.cells[0][0])
        self.notify_cell_changed(self.cells[0][0], 1)

        while len(stack) > 0:
            currentCell = stack[len(stack) - 1] # Peeking at top of stack
            neighbors = self.get_unvisited_neighbors(currentCell.x, currentCell.y, visited)

            if len(neighbors) == 0:
                poppedCell = stack.pop()
                self.notify_cell_changed(poppedCell, 0) # Notify that cell backtracked
                print('Cell at (%s, %s) was backtracked' % (poppedCell.x, poppedCell.y))
            else:
                neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
                self.connect_cells(currentCell, neighbor)
                stack.append(neighbor)
                visited.add((neighbor.x, neighbor.y))
                self.notify_cell_changed(neighbor, 1)
                currentCell = neighbor

            yield self

    # Method will connect cells by their shared wall. It
    # uses the difference between position in grid to determine
    # orientation.
    def connect_cells(self, cell_one, cell_two):
        # Need to figure out how cells are orientated
        if cell_one.x - cell_two.x == -1:
            cell_one.walls[1] = False
            cell_two.walls[3] = False
        elif cell_one.x - cell_two.x == 1:
            cell_one.walls[3] = False
            cell_two.walls[1] = False
        elif cell_one.y - cell_two.y == -1:
            cell_one.walls[2] = False
            cell_two.walls[0] = False
        elif cell_one.y - cell_two.y == 1:
            cell_one.walls[0] = False
            cell_two.walls[2] = False
        else:
            print('Cells are not adjacent to each other')

    # Method retrieves unvisited neighbors of node located at
    # 'x' and 'y' position in 2D grid. It will ensure boundaries
    # allow neighbor to be possible as well.
    def get_unvisited_neighbors(self, x, y, visited):
        neighbors = []
        if x > 0 and x < self.size - 1:
            if (x - 1, y) not in visited:
                neighbors.append(self.cells[x - 1][y])
            if(x + 1, y) not in visited:
                neighbors.append(self.cells[x + 1][y])
        elif x < self.size - 1:
            if (x + 1, y) not in visited:
                neighbors.append(self.cells[x + 1][y])
        elif x > 0:
            if (x- 1, y) not in visited:
                neighbors.append(self.cells[x - 1][y])

        if y > 0 and y < self.size - 1:
            if (x, y -1) not in visited:
                neighbors.append(self.cells[x][y - 1])
            if (x, y + 1) not in visited:
                neighbors.append(self.cells[x][y + 1])
        elif y < self.size - 1:
            if (x, y + 1) not in visited:
                neighbors.append(self.cells[x][y + 1])
        elif y > 0:
            if (x, y - 1) not in visited:
                neighbors.append(self.cells[x][y - 1])
        return neighbors

class Cell:

    # Initialize cell (i.e grid) in maze with all walls present
    def __init__(self, x, y):
        self.walls = [True, True, True, True]
        self.x = x
        self.y = y

# Object allows maze to be drawn on canvas
class Graphical_Maze(Observer):

    def __init__(self, canvas, maze):
        self.canvas = canvas
        self.maze = maze
        maze.add_observer(self) # Add graphical representation as observer

        width, height = self.canvas.get_size()
        canvas_mid = (width / 2, height / 2)
        paddedWidth = width - (2 * width * 0.1) # Add 10% padding on each side
        paddedHeight = height - (2 * height * 0.1)

        self.start = (width * 0.1, height * 0.1)
        self.square_length = min(paddedWidth, paddedHeight) / self.maze.size
        maze_size = self.square_length * self.maze.size
        # Get middle point of maze, help adjust to middle of canvas
        maze_mid = (self.start[0] + (maze_size / 2), self.start[1] + (maze_size / 2))
        # Adjust maze to middle of screen
        self.start = (self.start[0] + (canvas_mid[0] - maze_mid[0]), self.start[1] + (canvas_mid[1] - maze_mid[1]))

    def draw_maze(self):
        for y in range(0, self.maze.size):
            for x in range(0, self.maze.size):
                self.draw_cell(x, y)

    def draw_cell(self, x, y, color = (255, 255, 255)):

        # Fill in cell with color
        top = (self.start[0] + self.square_length * x, self.start[1] + self.square_length * y)
        size = self.square_length + 1
        pygame.draw.rect(self.canvas, color, (top[0], top[1], size, size))

        if self.maze.cells[x][y].walls[0] == True:
            topLineStart = (self.start[0] + self.square_length * x, self.start[1] + self.square_length * y)
            topLineEnd = (topLineStart[0] + self.square_length, topLineStart[1])
            pygame.draw.line(self.canvas, (0, 0, 0), topLineStart, topLineEnd, 1)

        if self.maze.cells[x][y].walls[2] == True:
            bottomLineStart = (self.start[0] + self.square_length * x, self.start[1] + self.square_length * (y + 1))
            bottomLineEnd = (bottomLineStart[0] + self.square_length, bottomLineStart[1])
            pygame.draw.line(self.canvas, (0, 0, 0), bottomLineStart, bottomLineEnd, 1)

        if self.maze.cells[x][y].walls[3] == True:
            leftLineStart = (self.start[0] + self.square_length * x, self.start[1] + self.square_length * y)
            leftLineEnd = (leftLineStart[0], leftLineStart[1] + self.square_length)
            pygame.draw.line(self.canvas, (0, 0, 0), leftLineStart, leftLineEnd, 1)

        if self.maze.cells[x][y].walls[1] == True:
            rightLineStart = (self.start[0] + self.square_length * (x + 1), self.start[1] + self.square_length * y)
            rightLineEnd = (rightLineStart[0], rightLineStart[1] + self.square_length)
            pygame.draw.line(self.canvas, (0, 0, 0), rightLineStart, rightLineEnd, 1)

        pygame.display.update((top[0], top[1], size, size)) # Update only portion of screen

    # Method responds to cell change events from observable and
    # fills cell with color based on state.
    #
    # STATE(S):
    # 0 -> Cell was backtracked
    # 1 -> Cell was explored
    def on_cell_changed(self, cell, state):
        if state == 0:
            self.draw_cell(cell.x, cell.y, (150, 225, 0))
        elif state == 1:
            self.draw_cell(cell.x, cell.y, (150, 225, 225))
        else:
            self.draw_cell(cell.x, cell.y, (255, 255, 255))
