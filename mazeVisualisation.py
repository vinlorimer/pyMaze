import pygame


class mazeVisualiser:
    """
    Class to visualise mazes using the library pyGame.
    """
    def __init__(self, maze, windowWidth: int=800, windowHeight: int=800, margin: int=20):
        """
        A method to construct the mazeVisualiser class.

        Parameters
        ---
        maze: Maze | takes a maze to visualise
        windowWidth: int | the width of the display window, default 800
        windowHeight: int | the height of the display window default 800
        margin: int | the margin around the maze inside of the window, default being 20

        Attributes
        ---
        screen | the display window used to draw the maze
        clock | a pygame clock used to control the speed of event loops
        backgroundColour | the colour of the background in RGB (white)
        wallColour | the colour of walls within the maze in RGB (black)
        startCellColour | the colour of the starting cell in RGB (green)
        endCellColour | the colour of the ending cell in RGB (red)
        pathCellColour | the colour of the path taken by any given solver in RGB (blue) 
        font | the font for the text to be used in displaying length of solutions
        cellSize | the size of each cell in pixels, the largest value that lets all cells fit inside the window
        offsetX | the x axis offset used to centre the maze
        offsetY | the y axis offset used to centre the maze
        """
        self.maze = maze
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.margin = margin

        pygame.init()
        self.screen = pygame.display.set_mode((windowWidth, windowHeight))
        pygame.display.set_caption("pyMaze")
        self.clock = pygame.time.Clock()

        self.backgroundColour = (255,255,255)
        self.wallColour = (0,0,0)
        self.startCellColour = (0,200,0)
        self.endCellColour = (200,0,0)
        self.pathCellsColour = (0,0,200)
        self.font = pygame.font.SysFont(None, 30)

        self.cellSize = min((self.windowWidth - self.margin) // self.maze.columns, (self.windowHeight - self.margin) // self.maze.rows)
        self.offsetX = (self.windowWidth - self.maze.columns * self.cellSize) // 2
        self.offsetY = (self.windowHeight - self.maze.rows * self.cellSize) // 2

    def getCellRect(self, cell):
        """
        A method to get a rectangle representing any given cell.

        Parameters
        ---
        cell: Cell | the given cell

        Returns
        ---
        A pygame rectangle in the position of given cell & correct size of the cell
        """
        x = self.offsetX + cell.column * self.cellSize
        y = self.offsetY + cell.row * self.cellSize
        return pygame.Rect(x, y, self.cellSize, self.cellSize)

    def drawMaze(self, path=None):
        """
        A method to draw the maze. It does this by creating a window and filling it with the background colour, then if there is 
        a path, add each cells coordinates to the path coordinates set. Then, go through each row in the maze and then each cell in 
        the row and create a rectangle for that cell, then just a few conditional checks if its a path, start or end cell, if it is 
        none of these then it must be an unused cell, so check for its walls and draw them.

        Parameters
        ---
        path: list | A list of cells that solve the maze, by default path is none.
        """
        self.screen.fill(self.backgroundColour)
        pathCoordinates = set()
        if path is not None:
            for cell in path:
                pathCoordinates.add((cell.row, cell.column))

        for row in self.maze.grid:
            for cell in row:
                rect = self.getCellRect(cell)

                if (cell.row, cell.column) in pathCoordinates:
                    pygame.draw.rect(self.screen, self.pathCellsColour, rect)

                if cell == self.maze.startCell:
                    pygame.draw.rect(self.screen, self.startCellColour, rect)

                if cell == self.maze.endCell:
                    pygame.draw.rect(self.screen, self.endCellColour, rect)

                if cell.NWall:
                    pygame.draw.line(self.screen, self.wallColour, (rect.x, rect.y), (rect.x + self.cellSize, rect.y), 2)
                if cell.EWall:
                    pygame.draw.line(self.screen, self.wallColour, (rect.x + self.cellSize, rect.y), (rect.x + self.cellSize, rect.y + self.cellSize), 2)
                if cell.SWall:
                    pygame.draw.line(self.screen, self.wallColour, (rect.x, rect.y + self.cellSize), (rect.x + self.cellSize, rect.y + self.cellSize), 2)
                if cell.WWall:
                    pygame.draw.line(self.screen, self.wallColour, (rect.x, rect.y), (rect.x, rect.y + self.cellSize), 2)

        pygame.display.flip()

    def visualise(self, path=None):
        """
        A method to draw the maze, if there is a solution path then work out the length of that path and put display that onto the
        window. Otherwise loop waiting for the user to either close the window or do any keyboard input.

        Paramters
        ---
        path: list | A list of cells that solve the maze, by default path is none.
        """
        self.drawMaze(path)
        if path is not None:    
            pathLength = len(path) - 1
            text = self.font.render(f"Path length: {pathLength}", True, (0, 0, 0))
            self.screen.blit(text, (0, 0))
            pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    return

            self.clock.tick(60)