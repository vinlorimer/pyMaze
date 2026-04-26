from maze import Maze
import random as rnd

def mouseSolver(maze: Maze, maxSteps: int = 10000):
    """
    A function to solve the maze by completely random movement.

    The solver starts at the maze's starting cell and then continuously chooses a random 
    reachable neighbouring cell until it reaches the end or hits its maxSteps limit.
    
    Parameters
    ---
    maze: Maze | The maze to solve.
    maxSteps: int | The maximum number of steps the "mouse" is allowed to take.
    
    Returns
    ---
    path: list | The list of cells representing the path taken by the "mouse".
    """

    currentCell = maze.startCell
    endCell = maze.endCell
    path = [currentCell]
    steps = 0
    

    while currentCell != endCell and steps < maxSteps:
        neighbours = maze.getReachableCells(currentCell)
        randomNeighbour = neighbours[rnd.randint(0, len(neighbours)-1)]
        currentCell = randomNeighbour
        path.append(currentCell)
        steps+=1

    return path

def humanSolver(maze: Maze, rule = "L"):
    """
    A function to solve the maze "humanly" using the left/right-hand wall following rule.

    The solver starts at the starting cell then moves through the maze keeping its left/right "hand" in contact
    with the wall depending on the rule. This is continued until the path reaches the end cell.

    Parameters
    ---
    maze: Maze | The maze to solve.
    rule: str | The rule to use, accepts any form of "r"/"right" or "l"/"left" for the corresponding rule.

    Returns
    ---
    path: list | The list of cells representing the path taken by the solver.
    """
    currentCell = maze.startCell
    endCell = maze.endCell
    path = [currentCell]
    facing = "S"
    directions = []

    while currentCell != endCell:
        if rule.upper() == "L" or rule.upper() == "LEFT":
            if facing == "N":
                directions = ["W", "N", "E", "S"]
            elif facing == "S":
                directions = ["E", "S", "W", "N"]
            elif facing == "E":
                directions = ["N", "E", "S", "W"]
            elif facing == "W":
                directions = ["S", "W", "N", "E"]

        elif rule.upper() == "R" or rule.upper() == "RIGHT":
            if facing == "N":
                directions = ["E", "N", "W", "S"]
            elif facing == "S":
                directions = ["W", "S", "E", "N"]
            elif facing == "E":
                directions = ["S", "E", "N", "W"]
            elif facing == "W":
                directions = ["N", "W", "S", "E"]

        for direction in directions:
            if direction == "N":
                if currentCell.row > 0 and currentCell.NWall == False:
                    currentCell = maze.grid[currentCell.row - 1][currentCell.column]
                    facing = "N"
                    path.append(currentCell)
                    break

            elif direction == "S":
                if currentCell.row < maze.rows - 1 and currentCell.SWall == False:
                    currentCell = maze.grid[currentCell.row + 1][currentCell.column]
                    facing = "S"
                    path.append(currentCell)
                    break

            elif direction == "E":
                if currentCell.column < maze.columns - 1 and currentCell.EWall == False:
                    currentCell = maze.grid[currentCell.row][currentCell.column + 1]
                    facing = "E"
                    path.append(currentCell)
                    break

            elif direction == "W":
                if currentCell.column > 0 and currentCell.WWall == False:
                    currentCell = maze.grid[currentCell.row][currentCell.column - 1]
                    facing = "W"
                    path.append(currentCell)
                    break

    return path

def aStarSolver(maze: Maze):
    """
    A function to solve the maze using the A* algorithm.

    The solver starts at the starting cell of the maze and explores reachable cells based off of the lowest
    estimated total cost of traveling there. The cost is calculated by using the current travelled distance and the Manhattan distance
    to the end cell. Once the end cell is reached, the shortest path is used.

    Parameters
    ---
    maze: Maze | The maze to solve.

    Returns
    ---
    path: list | The list of cells representing the path taken by the solver.
    """
    startCell = maze.startCell
    endCell = maze.endCell

    path = []
    openSet = [startCell]
    closedSet = set()
    gScore = {}
    fScore = {}
    cameFrom = {}

    gScore[startCell] = 0
    fScore[startCell] = abs(endCell.row - startCell.row) + abs(endCell.column - startCell.column)

    while len(openSet) > 0:
        currentCell = min(openSet, key=lambda cell: fScore.get(cell, float("inf")))

        if currentCell == endCell:
            path = [currentCell]
            while currentCell in cameFrom:
                currentCell = cameFrom[currentCell]
                path.append(currentCell)

            path.reverse()
            break

        openSet.remove(currentCell)
        closedSet.add(currentCell)

        reachableCells = maze.getReachableCells(currentCell)
        for cell in reachableCells:
            if cell in closedSet:
                continue

            tentativeG = gScore[currentCell] + 1

            if cell not in gScore or tentativeG < gScore[cell]:
                cameFrom[cell] = currentCell
                gScore[cell] = tentativeG
                fScore[cell] = tentativeG + abs(endCell.row - cell.row) + abs(endCell.column - cell.column)

                if cell not in openSet:
                    openSet.append(cell)

    return path