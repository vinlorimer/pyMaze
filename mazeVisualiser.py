import pygame
from maze import Maze

def visualiseMaze(maze: Maze):
    """

    Takes maze as parameter, initialises pygame. Quite a few variables to start with, first few are all to do with drawing the maze
    margin is to make sure that outerwalls are properly visible. windowWidth & Height are for the pygame screen size, clock is for 
    any updates that may need to be called and finally running is a bool for our while loop.

    Inside of the while loop it is checking if the pygame quit event happens, if it does then the while loop ends.
    Window is coloured white, then we iterate through the mazes rows and columns in order to get the current cell. Then the x + y
    which is the top left of the cell is calculated, then four if statements to check what walls the current cell still has so
    then it can draw a black line. Then the screen is displayed and clock limited to 60 udpates a second.
   
     """
   
    pygame.init()
    maxWindowWidth = 1000
    maxWindowHeight = 800
    margin = 20
   

    usableWidth = maxWindowWidth - margin * 2
    usableHeight = maxWindowHeight - margin * 2

    cellSizeFromWidth = usableWidth // maze.columns
    cellSizeFromHeight = usableHeight // maze.rows
    cellSize = min(cellSizeFromWidth, cellSizeFromHeight)
    cellSize = max(1, cellSize)
    wallThickness = max(1, cellSize // 8)

    windowWidth = maze.columns * cellSize + margin * 2
    windowHeight = maze.rows * cellSize + margin * 2
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    clock = pygame.time.Clock()
    running = True

    while running  == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        for row in range(maze.rows):
            for column in range(maze.columns):
                currentCell = maze.grid[row][column]
                x = margin + column * cellSize
                y = margin + row * cellSize
                if currentCell.NWall == True:
                    pygame.draw.line(screen, "black", (x, y), (x + cellSize, y), wallThickness)
                if currentCell.SWall == True:
                    pygame.draw.line(screen, "black", (x, y + cellSize), (x + cellSize, y + cellSize), wallThickness)
                if currentCell.WWall == True:
                    pygame.draw.line(screen, "black", (x, y), (x, y + cellSize), wallThickness)
                if currentCell.EWall == True:
                    pygame.draw.line(screen, "black", (x + cellSize, y),(x + cellSize, y + cellSize), wallThickness)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()