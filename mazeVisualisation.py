import pygame


class mazeVisualiser:
    """
    Class to visualise mazes using the library pyGame
    """
    def __init__(self, maze, windowWidth=800, windowHeight=800, margin=20):
        """
        TO DO
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
        self.pathCellsColour = (50,100,255)

        self.cellSize = min((self.windowWidth - 2 * self.margin) // self.maze.columns, (self.windowHeight - 2 * self.margin) // self.maze.rows)
        mazePixelWidth = self.maze.columns * self.cellSize
        mazePixelHeight = self.maze.rows * self.cellSize
        self.offsetX = (self.windowWidth - mazePixelWidth) // 2
        self.offsetY = (self.windowHeight - mazePixelHeight) // 2

    def getCellRect(self, cell):
        """
        TO DO
        """
        x = self.offsetX + cell.column * self.cellSize
        y = self.offsetY + cell.row * self.cellSize
        return pygame.Rect(x, y, self.cellSize, self.cellSize)

    def drawMaze(self, path=None):
        """
        TO DO
        """
        self.screen.fill(self.backgroundColour)
        pathCoords = set()
        if path is not None:
            for cell in path:
                pathCoords.add((cell.row, cell.column))

        for row in self.maze.grid:
            for cell in row:
                rect = self.getCellRect(cell)

                if (cell.row, cell.column) in pathCoords:
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

    def waitForKey(self):
        """
        TO DO
        """
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    waiting = False

            self.clock.tick(60)

    def keepOpen(self):
        """
        TO DO
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(60)

        pygame.quit()