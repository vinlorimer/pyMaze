from maze import Maze
import random as rnd

def DFSGenerator(maze: Maze):
    """
    A function to generate a maze using a depth first search algorithm.
    To do this, it first sets the current cell to the starting cell and marks it as visited, it then calculates how many cells in
    total there are in the maze, starts counting how many cells have been visited and creates an empty stack.

    Then, while there are unvisited cells, it gets all unvisited neighbours of the current cell, if there are unvisited neighbours
    then choose a random neighbour, add the current cell to the stack remove the walls between the current cell and random neighbour
    then make the random neighbour the new current cell and set it to visited, add one to the visited counter. If there are no
    unvisited neighbours then backtrack to a previous cell until there are unvisited neighbours.

    Parameters
    ---
    maze: Maze | Takes a maze to manipulate

    Returns
    ---
    maze | Returns the post generated maze
    """
    currentCell = maze.startCell
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

class DFSGeneratorAnimated():
    """
    testing 
    """
    def __init__(self, maze: Maze):
        self.currentCell = maze.startCell
        self.totalCells = maze.rows * maze.columns
        self.visitedCount = 0
        self.stack = []
        
    def step(self, maze: Maze):
        unvisitedNeighbours = maze.getUnvisited(self.currentCell)
        if (len(unvisitedNeighbours) > 0 ):                
            randomNeighbour = unvisitedNeighbours[rnd.randint(0, len(unvisitedNeighbours)-1)]
            self.stack.append(self.currentCell)
            maze.removeWall(self.currentCell, randomNeighbour)
            currentCell = randomNeighbour
            currentCell.visited = True
            visitedCounter += 1
        else:
            previousCell = self.stack.pop()
            self.currentCell = previousCell


def primsGenerator(maze: Maze):
    """
    A function to generate a maze using Prims Algorithm. 
    To do this, the function first chooses a random cell as the starting cell and setting it to having been visited. Then get all 
    unvisited cells around the starting cell and add them to be possible candidates to move to. While there are still candidates,
    choose a random cell from the candidates to be the current cell and remove it from being a candidate, then get all of the
    neighbours around that current cell. Create a list of all the neighbours around the current cell that HAVE been visited
    then choose a random visited neighbour and remove the walls between the current cell and that neighbour and mark the 
    current cell as visited. Get all the unvisited neighbours of the current cell iterate through them, and if that unvisited
    neighbour isn't already a candidate then add it to the list of candidate cells.

    Parameters
    ---
    maze: Maze | Takes a maze to manipulate

    Returns
    ---
    maze | Returns the post generated maze
    """
    startCell = maze.grid[rnd.randint(0, maze.rows-1)][rnd.randint(0, maze.columns-1)]
    startCell.visited = True
    candidateCells = maze.getUnvisited(startCell)

    while len(candidateCells) > 0:

        currentCell = candidateCells[rnd.randint(0, len(candidateCells)-1)]
        candidateCells.remove(currentCell)
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
            if neighbour not in candidateCells:
                candidateCells.append(neighbour)
                  
    return maze

def wilsonsGenerator(maze: Maze):
    """
    A function to generate a maze using Wilson's Algorithm.
    To do this 
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