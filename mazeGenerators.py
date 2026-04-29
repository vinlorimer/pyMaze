from maze import Maze
import random as rnd

def DFSGenerator(maze: Maze, seed = None):
    """
    A function to generate a maze using a depth-first search algorithm.

    The algorithm works by starting at the start cell, marking it as visited,
    then continuously move to a random UNVISITED neighbour. When there are no 
    more unvisited neighbours, backtrack until at a cell that does have unvisited
    neighbours. Continue until all cells are visited.

    Parameters
    ---
    maze: Maze | The maze to generate.
    seed: int | Optional random seed so mazes can be reproduced & compared.
    
    Returns
    ---
    maze | The generated maze.
    """
    maze.openMaze()
    rng = rnd.Random(seed)
    currentCell = maze.startCell
    currentCell.visited = True
    totalCells = maze.rows * maze.columns
    visitedCounter = 1
    stack = []

    while visitedCounter < totalCells:
        unvisitedNeighbours = maze.getUnvisited(currentCell)
        if (len(unvisitedNeighbours) > 0 ):                
            randomNeighbour = unvisitedNeighbours[rng.randint(0, len(unvisitedNeighbours)-1)]
            stack.append(currentCell)
            maze.removeWall(currentCell, randomNeighbour)
            currentCell = randomNeighbour
            currentCell.visited = True
            visitedCounter += 1
        else:
            previousCell = stack.pop()
            currentCell = previousCell

    return maze

def primsGenerator(maze: Maze, seed = None):
    """
    A function to generate a maze using Prim's algorithm.

    The algorithm works by choosing a random starting cell, and marking it as visited
    All unvisited neighbours of the current cell are added to a list of "candidate cells"
    While there are candidate cells, one is chosen randomly and then connected to by a 
    random already VISITED neighbour, then the candidate cell is marked as visited and 
    any UNVISITED neighbour cells are added to the candidate list. Continue until all cells
    are visited.

    Parameters
    ---
    maze: Maze | The maze to generate.
    seed: int | Optional random seed so mazes can be reproduced & compared.
    
    Returns
    ---
    maze | The generated maze.
    """
    maze.openMaze()
    rng = rnd.Random(seed)
    startCell = maze.grid[rng.randint(0, maze.rows-1)][rng.randint(0, maze.columns-1)]
    startCell.visited = True
    candidateCells = maze.getUnvisited(startCell)

    while len(candidateCells) > 0:

        currentCell = candidateCells[rng.randint(0, len(candidateCells)-1)]
        candidateCells.remove(currentCell)
        allNeighbours = maze.getNeighbours(currentCell)
        visitedNeighbours = []

        for neighbour in allNeighbours:
            if neighbour.visited == True:
                visitedNeighbours.append(neighbour)

        randomVisitedNeighbour = visitedNeighbours[rng.randint(0, len(visitedNeighbours)-1)]
        maze.removeWall(currentCell, randomVisitedNeighbour)
        currentCell.visited = True
        unvisitedNeighbours = maze.getUnvisited(currentCell)
        
        for neighbour in unvisitedNeighbours:
            if neighbour not in candidateCells:
                candidateCells.append(neighbour)
                  
    return maze

def wilsonsGenerator(maze: Maze, seed = None):
    """
    A function to generate a maze using Wilson's algorithm.

    The algorithm works by marking a random cell as visited, then it continuously selects
    a random unvisited cell and performs a random walk until it reaches a visited cell. If 
    the walk forms a loop, the loop is removed. Once the walk hits a visited cell, the path is
    put into the maze and all cells in the path are marked as visited. Continue until all cells 
    are visited.

    Parameters
    ---
    maze: Maze | The maze to generate.
    seed: int | Optional random seed so mazes can be reproduced & compared.
    
    Returns
    ---
    maze | The generated maze.
    """
    maze.openMaze()
    rng = rnd.Random(seed)
    allCells = maze.getCells()
    randomCell = allCells[rng.randint(0, len(allCells)-1)]
    randomCell.visited = True
    allCells.remove(randomCell)

    while len(allCells) > 0:
        currentCell = allCells[rng.randint(0, len(allCells)-1)]
        walkPath = [currentCell]

        while currentCell.visited == False:
            currentCellNeighbours = maze.getNeighbours(currentCell)
            randomNeighbour = currentCellNeighbours[rng.randint(0, len(currentCellNeighbours)-1)]
            
            if randomNeighbour in walkPath:
                loopStart = walkPath.index(randomNeighbour)
                walkPath = walkPath[:loopStart + 1] 
                currentCell = walkPath[-1]
            elif randomNeighbour.visited == True:
                walkPath.append(randomNeighbour)
                break
            else:
                walkPath.append(randomNeighbour)
                currentCell = randomNeighbour
        
        for i in range(len(walkPath)-1):
            maze.removeWall(walkPath[i], walkPath[i+1])

        for cell in walkPath:
            if cell.visited == False:
                cell.visited = True
                allCells.remove(cell)

    return maze