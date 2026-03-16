from maze import Maze
import random as rnd

def DFSGenerator(maze: Maze):
    """

    Takes maze as a parameter, initiates 5 initial variables, the current cell which is always top left [0][0], sets that cell to 
    being visited, then calculates how many cells there are in the maze, keeps count of how many cells have been visited and finally
    an empty stack.

    While loop continues until the number of visited cells is less than the total cells (until all cells have been visited).
    Logic is as follows:
    -> Get unvisited neighbours of the current cell
    -> If they exist, then do the following:
    ----> Pick a random neighbour from the list of unvisited neighbours using the random library picking a random int between 0 
          and the length of the unvisitedneighbours (-1 to account for indexing beginning at 0)
          Push the current cell onto the stack
          Remove the walls between the current cell & the random neighbouring cell.
          Set the current cell to the random neighbour, and set the new current cell to being visited and add one to the visited
          counter.
    -> Else (if no other unvisited neighbours exist)
    ----> Store the latest cell in the stack, then pop it from the stack, set the popped cell to the current cell so that the 
          algorithm can backtrack until all cells have been visited.
    
    Finally, return the maze in its new form.


    REDO
    
    """
    currentCell = maze.grid[0][0]
    currentCell.visited = True
    totalCells = maze.rows * maze.columns
    visitedCounter = 1
    stack = []

    while visitedCounter < totalCells:
        unvisitedNeighbours = maze.getUnvisited(currentCell)
        if (len(unvisitedNeighbours) > 0 ):                
            randomNeighbour = unvisitedNeighbours[rnd.randint(0, len(unvisitedNeighbours)-1)]
            stack.append(currentCell)
            maze.removeWall(currentCell, randomNeighbour)
            currentCell = randomNeighbour
            currentCell.visited = True
            visitedCounter += 1
        else:
            previousCell = stack.pop()
            currentCell = previousCell

    return maze

def primsGenerator(maze: Maze):
    """

    to do
     
    """
    startCell = maze.grid[rnd.randint(0, maze.rows-1)][rnd.randint(0, maze.columns-1)]
    startCell.visited = True
    frontier = maze.getUnvisited(startCell)

    while len(frontier) > 0:

        currentCell = frontier[rnd.randint(0, len(frontier)-1)]
        frontier.remove(currentCell)
        allNeighbours = maze.getNeighbours(currentCell)
        visitedNeighbours = []

        for neighbour in allNeighbours:
            if neighbour.visited == True:
                visitedNeighbours.append(neighbour)

        randomVisitedNeighbour = visitedNeighbours[rnd.randint(0, len(visitedNeighbours)-1)]
        maze.removeWall(currentCell, randomVisitedNeighbour)
        currentCell.visited = True
        unvisitedNeighbours = maze.getUnvisited(currentCell)
        
        for neighbour in unvisitedNeighbours:
            if neighbour in frontier:
                pass
            else:
                frontier.append(neighbour)
    
    return maze


def wilsonsGenerator(maze: Maze):
    """
    
    ts is long brah

    """
    allCells = maze.getCells()
    randomCell = allCells[rnd.randint(0, len(allCells)-1)]
    randomCell.visited = True
    allCells.remove(randomCell)

    while len(allCells) > 0:
        currentCell = allCells[rnd.randint(0, len(allCells)-1)]
        walkpath = [currentCell]

        while currentCell.visited == False:
            currentCellNeighbours = maze.getNeighbours(currentCell)
            randomNeighbour = currentCellNeighbours[rnd.randint(0, len(currentCellNeighbours)-1)]
            
            if randomNeighbour in walkpath:
                loopStart = walkpath.index(randomNeighbour)
                walkpath = walkpath[:loopStart + 1]
                currentCell = walkpath[-1]
            elif randomNeighbour.visited == True:
                walkpath.append(randomNeighbour)
                break
            else:
                walkpath.append(randomNeighbour)
                currentCell = randomNeighbour
        
        for i in range(len(walkpath)-1):
            maze.removeWall(walkpath[i], walkpath[i+1])

        for cell in walkpath:
            if cell.visited == False:
                cell.visited = True
                allCells.remove(cell)

    return maze