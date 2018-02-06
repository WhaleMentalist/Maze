import random, sys, time

class Maze:

    def __init__(self, s = 5):
        self.size = s
        self.stack = []
        self.visited = set([]) # Keep a set of visited for generation algorithm and for drawing
        self.popped = set([]) # Keep a set of popped for drawing

        self.cells = [] # Holds maze represented as a 2D grid
        for x in range(0, self.size):
            self.cells.append([]) # Append an empty list before initializing cells in row
            for y in range(0, self.size):
                self.cells[x].append(Cell(x,y)) # Create cell with all the walls intact

    # Algorithm generates a maze using depth first search with randomization
    # for better maze
    def generate_cell(self):
        current = self.cells[0][0] # Pick top left as current cell to start
        currPopped = self.cells[0][0]
        self.visited.add((0, 0)) # Implement set to track visited cells
        self.stack.append(current) # Push current onto stack

        # While the stack has cells to backtrack, continue constructing maze
        while len(self.stack) > 0:
            current = self.stack[len(self.stack) - 1]
            neighbors = self.get_unvisited_neighbors(current.x, current.y) # Find unvisited neighbors

            # If there are no neighbors, we need to backtrack to node w/ neighbors
            if len(neighbors) == 0:
                currPopped = self.stack.pop()
                self.popped.add((currPopped.x, currPopped.y))
            else:
                neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
                self.connect_cells(current, neighbor)
                self.stack.append(neighbor)
                self.visited.add((neighbor.x, neighbor.y))
                current = neighbor

            yield self # Generate cell one at a time


    # Method will connect cells with shared wall
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

    # Method retrieves the neighbors of a given cell in maze and
    # returns it as a list of cells
    def get_unvisited_neighbors(self, x, y):
        neighbors = []

        # Check 'x' coordinates to boundry
        if x > 0 and x < self.size - 1:
            if (x - 1, y) not in self.visited:
                neighbors.append(self.cells[x - 1][y])
            if (x + 1, y) not in self.visited:
                neighbors.append(self.cells[x + 1][y])
        elif x < self.size - 1:
            if (x + 1, y) not in self.visited:
                neighbors.append(self.cells[x + 1][y])
        elif x > 0:
            if (x - 1, y) not in self.visited:
                neighbors.append(self.cells[x - 1][y])

        # Check 'y' coordinates to boundry
        if y > 0 and y < self.size - 1:
            if (x, y - 1) not in self.visited:
                neighbors.append(self.cells[x][y - 1])
            if(x, y + 1) not in self.visited:
                neighbors.append(self.cells[x][y + 1])
        elif y < self.size - 1:
            if (x, y + 1) not in self.visited:
                neighbors.append(self.cells[x][y + 1])
        elif y > 0:
            if(x, y - 1) not in self.visited:
                neighbors.append(self.cells[x][y - 1])

        return neighbors

class Cell:
    # For walls the order is N, E, S, and W
    def __init__(self, x, y):
        self.walls = [True, True, True, True] # Represents wall around cell
        self.x = x
        self.y = y
