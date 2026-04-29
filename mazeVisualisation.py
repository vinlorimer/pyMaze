import pygame


class mazeVisualiser:
    """
    A class to visualise mazes using the library pyGame.
    """
    def __init__(self, maze, windowWidth: int=800, windowHeight: int=800, margin: int=20):
        """
        A method to construct the class.

        Parameters
        ---
        maze: Maze | The maze to visualise.
        windowWidth: int | The width of the display in pixels, default 800.
        windowHeight: int | The height of the display window in pixels, default 800.
        margin: int | The margin around the maze inside of the window in pixels, default being 20.

        Attributes
        ---
        maze | Stores the maze being visualised
        windowWidth | Stores the width of the window.
        windowHeight | Stores the height of the window.
        margin | Stores the margin of the window.
        screen | The display window used to draw the maze.
        clock | A pygame clock used to control the speed of event loops.
        backgroundColour | The colour of the background in RGB (white).
        wallColour | The colour of walls within the maze in RGB (black).
        startCellColour | The colour of the starting cell in RGB (green).
        endCellColour | The colour of the ending cell in RGB (red).
        pathCellColour | The colour of the path taken by any given solver in RGB (blue) .
        font | The font fr the text to be used in displaying length of solutions.
        cellSize | The size of each cell in pixels.
        offsetX | The x axis offset used to centre the maze.
        offsetY | The y axis offset used to centre the maze.
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

        self.cellSize = min((self.windowWidth - 2 * self.margin) // self.maze.columns, (self.windowHeight - 2 * self.margin) // self.maze.rows)
        if self.cellSize <= 0:
            raise ValueError("Window is too small for this maze and margin.")
        self.offsetX = (self.windowWidth - self.maze.columns * self.cellSize) // 2
        self.offsetY = (self.windowHeight - self.maze.rows * self.cellSize) // 2

    def getCellRect(self, cell):
        """
        A method to get a rectangle representing the size and position of a given cell.

        Parameters
        ---
        cell: Cell | The given cell.

        Returns
        ---
        rect: pygame.Rect | A rectangle representing the given cell.
        """
        x = self.offsetX + cell.column * self.cellSize
        y = self.offsetY + cell.row * self.cellSize
        return pygame.Rect(x, y, self.cellSize, self.cellSize)

    def drawMaze(self, path=None):
        """
        A method that draws the maze to the display window.

        The maze background is first drawn ,followed by any path cells, the start & end cells, then finally
        the walls are drawn for each cell.

        Parameters
        ---
        path: list | An optional list of cells represnting the solution path.
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
        A method to display the maze and its solutions.

        If there is a path provided then the path is drawn and its length worked out and displayed. The display window stays open
        until the user exits it or presses any key on their keybaord.

        Parameters
        ---
        path: list | An optional list of cells represnting the solution path.
        """
        self.drawMaze(path)
        if path is not None:    
            pathLength = len(path)
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