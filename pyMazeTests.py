from maze import Maze, Cell
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver

def getCellCoordinates(cells):
    """
    Function to help with testing by getting cell coordinates.
    """
    return {(cell.row, cell.column) for cell in cells}

def testCellInit():
    
    """
    Tests that the cell is constructed properly.
    """
    cell = Cell(6,7)

    assert cell.row == 6, "expected cell row 6"
    assert cell.column == 7, "expected cell row 7"
    assert cell.visited is False, "expected visited to be false"
    assert cell.NWall is True, "expected nwall to be true"
    assert cell.EWall is True, "expected ewall to be true"
    assert cell.SWall is True, "expected swall to be true"
    assert cell.WWall is True, "expected wwall to be true"

def testMazeInit():
    """
    Tests that the maze is constructed properly.
    """
    maze = Maze(6,9)

    assert maze.rows == 6, "expected 6 rows"
    assert maze.columns == 9, "expected 9 columns"
    assert len(maze.grid) == 6, "expected 6 rows in grid"
    assert len(maze.grid[0]) == 9, "expected 9 colums in the first row"
    assert len(maze.grid[1]) == 9, "expected 9 colums in the second row"
    assert len(maze.grid[2]) == 9, "expected 9 colums in the third row"
    assert len(maze.grid[3]) == 9, "expected 9 colums in the fourth row"
    assert len(maze.grid[4]) == 9, "expected 9 colums in the fifth row"
    assert len(maze.grid[5]) == 9, "expected 9 colums in the sixth row"
    assert maze.startCell == maze.grid[0][0], "expected start cell to be top left"
    assert maze.endCell == maze.grid[5][8], "expected end cell to be the bottom right"

def testCreateGrid():
    """
    Tests that createGrid creates all cells correctly
    """
    maze = Maze(4,20)

    for row in range(maze.rows):
        for column in range(maze.columns):
            cell = maze.grid[row][column]
            assert isinstance(cell, Cell), "expected the instance to be a cell... but its not"
            assert cell.row == row, f"expected the row to be {row}, got {cell.row}"
            assert cell.column == column, f"expected the column to be {column} got {cell.column}"

def testGetNeighboursTopLeft():
    """
    Tests that when using the getNeighbours method on the top left corner of a maze
    """
    maze = Maze(3, 3)
    cell = maze.grid[0][0]
    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)
    expectedCoordinates = {(1,0),(0,1)}

    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursTopEdge():
    """
    Tests the getNeighbours method on the top edge of the maze, this should return 3 neighbours as the neighbour above the cell is
    out of bounds.
    """
    maze = Maze(3,3)
    cell = maze.grid[0][1]
    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)
    expectedCoordinates = {(0,0),(0,2),(1,1)}

    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursMiddleCell():
    """
    Tests that getNeighbours returns all four neighbours around a middle cell as no cells around the cell should be out of bounds.
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]
    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)
    expectedCoordinates = {(0,1),(1,2),(2,1),(1,0)}

    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursBottomRight():
    """
    Tests that the getNegihbours returns only two neighbours when checking the bottom right cell of a maze as the other two will be 
    out of bounds.
    """
    maze = Maze(3,3)
    cell = maze.grid[2][2]
    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)
    expectedCoordinates = {(1,2),(2,1)}

    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetUnvisitedGetsAllNeighboursWhenUnvisited():
    """
    Tests that the getUnvisited method gets all cells around a specified cell that have the attribute visited as false.
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]
    unvisitedCells = maze.getUnvisited(cell)
    unvisitedCellsCoordinates = getCellCoordinates(unvisitedCells)
    expectedCoordinates = {(0,1),(1,2),(2,1),(1,0)}

    assert unvisitedCellsCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {unvisitedCellsCoordinates}"

def testGetUnvisitedExcludesVisitedNeigbhours():
    """
    Tests the getUnvisited method when some of the cells around a specified cell have been visited, and makes sure that it excludes
    them.
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]
    maze.grid[0][1].visited = True
    maze.grid[1][0].visited = True
    unvisitedCells = maze.getUnvisited(cell)
    unvisitedCellsCoordinates = getCellCoordinates(unvisitedCells)
    expectedCoordinates = {(2,1),(1,2)}

    assert unvisitedCellsCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {unvisitedCellsCoordinates}"

def testGetUnvisitedGetsNoVisitedCells():
    """
    Tests that when all the cells around a specified cell are visited that it returns an empty list as they are all visited.
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]
    for neighbour in maze.getNeighbours(cell):
        neighbour.visited = True
    unvisitedCells = maze.getUnvisited(cell)

    assert unvisitedCells == [], f"expected empty list, got {unvisitedCells}"

def testRemoveWallOpensNorthAndSouthWalls():
    """
    Tests when removing north and south walls that it actually does remove those walls.
    """
    maze = Maze(2,1)
    topCell = maze.grid[0][0]
    bottomCell = maze.grid[1][0]
    maze.removeWall(bottomCell, topCell)

    assert topCell.SWall is False, "expected swall to be false"
    assert topCell.NWall is True, "expected nwall to be true"
    assert bottomCell.NWall is False, "expected nwall to be false"
    assert bottomCell.SWall is True, "expected swall to be true"


def testRemoveWallOpensSouthAndNorthWalls():
    """
    Tests that when removing the south and north wall it actually does that and not something else 
    """
    maze = Maze(2,1)
    topCell = maze.grid[0][0]
    bottomCell = maze.grid[1][0]
    maze.removeWall(topCell, bottomCell)

    assert topCell.SWall is False, "expected swall to be false"
    assert topCell.NWall is True, "expected nwall to be true"
    assert bottomCell.NWall is False, "expected nwall to be false"
    assert bottomCell.SWall is True, "expected swall to be true"

def testRemoveWallOpensEastAndWestWalls():
    """
    Tests when removing the east and west walls that it does that rather than something else
    """
    maze = Maze(1,2)
    leftCell = maze.grid[0][0]
    rightCell = maze.grid[0][1]
    maze.removeWall(leftCell, rightCell)

    assert leftCell.EWall is False, "expected ewall to be false"
    assert leftCell.WWall is True, "expected wwall to be true"
    assert rightCell.WWall is False, "expected wwall to be false"
    assert rightCell.EWall is True, "expected eewall to be true"

def testRemoveWallOpensWestAndEastWalls():
    """
    Tests when removingthe west and east wall that it does that rather than something else.
    """
    maze = Maze(1,2)
    leftCell = maze.grid[0][0]
    rightCell = maze.grid[0][1]
    maze.removeWall(rightCell, leftCell)

    assert leftCell.EWall is False, "expected ewall to be false"
    assert leftCell.WWall is True, "expected wwall to be true"
    assert rightCell.WWall is False, "expected wwall to be false"
    assert rightCell.EWall is True, "expected eewall to be true"

def testOpenMaze():
    """
    Tests that when using the openMaze method it actually does open the correct walls of the maze.
    """
    maze = Maze(3,3)
    maze.openMaze()

    assert maze.startCell.NWall is False, "expected nwall to be false"
    assert maze.endCell.SWall is False, "expected swall to be false"

def testOpenMazeOn1x1():
    """

    """
    maze = Maze(1,1)
    maze.openMaze()

    assert maze.startCell == maze.endCell, "expected start cell and end cell to be the same cell"
    assert maze.startCell.NWall is False, "expected nwall to be open"
    assert maze.startCell.SWall is False, "expected swall to be openb"
    assert maze.startCell.EWall is True, "expected ewall to be closed"
    assert maze.startCell.WWall is True, "expected wwall to be closed"

def testGetCellsGetsAllCells():
    """
    """
    maze = Maze(2,3)
    cells = maze.getCells()

    assert len(cells) == 6, f"expected there to be 6 cells, got {len(cells)}"
    assert cells[0] == maze.grid[0][0], "first cell should be (0,0)"
    assert cells[-1] == maze.grid[1][2], "final cell should be (1,2)"

def testGetReachableCellsGetsNothingWhenAllWallsClosed():
    """
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]
    reachableCells = maze.getReachableCells(cell)

    assert reachableCells == [], f"expected no reachable cells, got {reachableCells}"        

def testGetReachableCellsReturnsHorizontalNeighbours():
    """
    """
    maze = Maze(3,3)
    middleCell = maze.grid[1][1]
    leftCell = maze.grid[1][0]
    rightCell = maze.grid[1][2]
    maze.removeWall(middleCell, leftCell)
    maze.removeWall(middleCell, rightCell)
    reachableCells = maze.getReachableCells(middleCell)
    reachableCellsCoordinates = getCellCoordinates(reachableCells)
    expectedCoordinates = {(1,0),(1,2)}
    
    assert reachableCellsCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, instead got {reachableCellsCoordinates}"

def testGetReachableCellsReturnsVerticalNeighbours():
    """
    """
    maze = Maze(3,3)
    middleCell = maze.grid[1][1]
    topCell = maze.grid[0][1]
    bottomCell = maze.grid[2][1]
    maze.removeWall(middleCell, topCell)
    maze.removeWall(middleCell, bottomCell)
    reachableCells = maze.getReachableCells(middleCell)
    reachableCellsCoordinates = getCellCoordinates(reachableCells)
    expectedCoordinates = {(0,1),(2,1)}
    
    assert reachableCellsCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, instead got {reachableCellsCoordinates}"

def testGetReachableSymmetry():
    """
    """
    maze = Maze(3,3)
    cellOne = maze.grid[0][0]
    cellTwo = maze.grid[0][1]
    maze.removeWall(cellOne, cellTwo)
    reachableFromCellOne = maze.getReachableCells(cellOne)
    reachableFromCellTwo = maze.getReachableCells(cellTwo)

    assert cellTwo in reachableFromCellOne, "expected celltwo to be reachable"
    assert cellOne in reachableFromCellTwo, "expected cellone to be reachable"

def getMazeSignature(maze):
    """
    A helper function that is used to compare if two generated mazes have the same signature

    Parameters
    ---
    maze: Maze | the maze to get a signature for 

    Returns
    ---
    A tuple with the mazes signature
    """
    signature = []

    for cell in maze.getCells():
        signature.append((cell.row, cell.column, cell.NWall, cell.EWall, cell.SWall, cell.WWall))
    
    return tuple(signature)
    
def countMazePassages(maze):
    """
    A helper function that is used to count the number of open passages in a given maze. The reason for using only checking south
    and east walls is so that it doesn't count duplicate passages.

    Parameters
    ---
    maze: Maze | the maze which passages are to be counted

    Returns
    ---
    An int that is the number of passages in the given maze
    """

    passages = 0 

    for cell in maze.getCells():
        if cell.column < maze.columns - 1 and cell.EWall is False:
            passages += 1
        
        if cell.row < maze.rows - 1 and cell.SWall is False:
            passages += 1

    return passages

def getConnectedCellsFromStartCell(maze):
    """
    Another helper function that gets all the cells reachable from the start cell.

    Parameters
    ---
    maze: Maze | the maze to check

    Returns
    ---
    visited: set | A set of all the cells visitable
    """

    visited = set()
    stack = [maze.startCell]

    while stack:
        currentCell = stack.pop()

        if currentCell not in visited:
            visited.add(currentCell)

            for neighbour in maze.getReachableCells(currentCell):
                if neighbour not in visited:
                    stack.append(neighbour)
    
    return visited

def testAllCellsVisited(generator, rows=5, columns=5, seed=10):
    """
    A function to test that all the cells 
    """
    maze = Maze(rows, columns)
    maze = generator(maze, seed)

    for cell in maze.getCells():
        assert cell.visited is True, f"Expected cell {cell.row}, {cell.column} to be visited"

def testGeneratedMazeIsConnected(generator, rows=5, columns=5, seed=10):
    """
    """
    maze = Maze(rows, columns)
    maze = generator(maze, seed)

    connectedCells = getConnectedCellsFromStartCell(maze)
    expectedConnectedCells = rows*columns

    assert len(connectedCells) == expectedConnectedCells, f"expected {expectedConnectedCells}, got {len(connectedCells)}"

def testGeneratedMazeIsPerfect(generator, rows=5, columns=5, seed=10):
    """
    """
    maze = Maze(rows, columns)
    maze = generator(maze, seed)

    totalCells = rows*columns
    passages = countMazePassages(maze)

    assert totalCells-1 == passages, f"expected there to be {totalCells-1} passages, instead got {passages}"

def testSameSeedGeneration(generator, rows=5, columns=5, seed=42):
    """
    """
    mazeOne = Maze(rows, columns)
    mazeTwo = Maze(rows, columns)

    mazeOne = generator(mazeOne, seed)
    mazeTwo = generator(mazeTwo, seed)

    mazeOneSignature = getMazeSignature(mazeOne)
    mazeTwoSignature = getMazeSignature(mazeTwo)

    assert mazeOneSignature == mazeTwoSignature, "expected the same seed to generate the same maze"


def testGeneratedMazeIsAMazeObject(generator, rows=5, columns=5, seed=10):
    """
    """
    maze = Maze(rows, columns)
    generatedMaze = generator(maze, seed)

    assert generatedMaze is maze, "expected the generated maze to still be a maze object"

def testGeneratorsWorkOn1x1(generator, seed=10):
    """
    """
    maze = Maze(1,1)
    maze = generator(maze, seed)
    
    assert maze.startCell == maze.endCell, "expected the start and end cell to be the same cell."
    assert maze.startCell.visited is True, "expected the start cell to have been visited"
    assert countMazePassages(maze) == 0, f"expected there to be 0 passages in a 1x1 maze, instead got {countMazePassages(maze)}"

def testGeneratorsWorkOnNonSquareMaze(generator, seed=10):
    """
    """
    rows = 6
    columns = 7
    maze = Maze(rows, columns)
    maze = generator(maze, seed)

    connectedCells = getConnectedCellsFromStartCell(maze)
    expectedConnectedCells = rows * columns

    assert len(connectedCells) == expectedConnectedCells, f"expected {expectedConnectedCells} connected cells instead got {len(connectedCells)}"

    for cell in maze.getCells():
        assert cell.visited is True, f"expected {cell.row}, {cell.column} to have been visited."

def testDFSGeneratorReturnsMaze():
    """
    Tests that DFSGenerator returns the same maze object.
    """
    testGeneratedMazeIsAMazeObject(DFSGenerator)

def testDFSGeneratorVisitsAllCells():
    """
    Tests that DFSGenerator visits every cell.
    """
    testAllCellsVisited(DFSGenerator)

def testDFSGeneratorCreatesConnectedMaze():
    """
    Tests that DFSGenerator creates a fully connected maze.
    """
    testGeneratedMazeIsConnected(DFSGenerator)

def testDFSGeneratorCreatesPerfectMaze():
    """
    Tests that DFSGenerator creates a perfect maze.
    """
    testGeneratedMazeIsPerfect(DFSGenerator)

def testDFSGeneratorSameSeedSameMaze():
    """
    Tests that DFSGenerator is reproducible with the same seed.
    """
    testSameSeedGeneration(DFSGenerator)

def testDFSGeneratorWorksOn1x1():
    """
    Tests that DFSGenerator works on a 1x1 maze.
    """
    testGeneratorsWorkOn1x1(DFSGenerator)

def testDFSGeneratorWorksOnNonSquareMaze():
    """
    Tests that DFSGenerator works on a non-square maze.
    """
    testGeneratorsWorkOnNonSquareMaze(DFSGenerator)

def testPrimsGeneratorReturnsMaze():
    """
    Tests that primsGenerator returns the same maze object.
    """
    testGeneratedMazeIsAMazeObject(primsGenerator)


def testPrimsGeneratorVisitsAllCells():
    """
    Tests that primsGenerator visits every cell.
    """
    testAllCellsVisited(primsGenerator)


def testPrimsGeneratorCreatesConnectedMaze():
    """
    Tests that primsGenerator creates a fully connected maze.
    """
    testGeneratedMazeIsConnected(primsGenerator)


def testPrimsGeneratorCreatesPerfectMaze():
    """
    Tests that primsGenerator creates a perfect maze.
    """
    testGeneratedMazeIsPerfect(primsGenerator)


def testPrimsGeneratorSameSeedSameMaze():
    """
    Tests that primsGenerator is reproducible with the same seed.
    """
    testSameSeedGeneration(primsGenerator)


def testPrimsGeneratorWorksOn1x1():
    """
    Tests that primsGenerator works on a 1x1 maze.
    """
    testGeneratorsWorkOn1x1(primsGenerator)


def testPrimsGeneratorWorksOnNonSquareMaze():
    """
    Tests that primsGenerator works on a non-square maze.
    """
    testGeneratorsWorkOnNonSquareMaze(primsGenerator)

def testWilsonsGeneratorReturnsMaze():
    """
    Tests that wilsonsGenerator returns the same maze object.
    """
    testGeneratedMazeIsAMazeObject(wilsonsGenerator)


def testWilsonsGeneratorVisitsAllCells():
    """
    Tests that wilsonsGenerator visits every cell.
    """
    testAllCellsVisited(wilsonsGenerator)


def testWilsonsGeneratorCreatesConnectedMaze():
    """
    Tests that wilsonsGenerator creates a fully connected maze.
    """
    testGeneratedMazeIsConnected(wilsonsGenerator)


def testWilsonsGeneratorCreatesPerfectMaze():
    """
    Tests that wilsonsGenerator creates a perfect maze.
    """
    testGeneratedMazeIsPerfect(wilsonsGenerator)


def testWilsonsGeneratorSameSeedSameMaze():
    """
    Tests that wilsonsGenerator is reproducible with the same seed.
    """
    testSameSeedGeneration(wilsonsGenerator)


def testWilsonsGeneratorWorksOn1x1():
    """
    Tests that wilsonsGenerator works on a 1x1 maze.
    """
    testGeneratorsWorkOn1x1(wilsonsGenerator)


def testWilsonsGeneratorWorksOnNonSquareMaze():
    """
    Tests that wilsonsGenerator works on a non-square maze.
    """
    testGeneratorsWorkOnNonSquareMaze(wilsonsGenerator)

def runAllTests():
    """
    The name.
    """
    testCellInit()
    testMazeInit()
    testCreateGrid()
    testGetNeighboursTopLeft()
    testGetNeighboursTopEdge()
    testGetNeighboursBottomRight()
    testGetNeighboursMiddleCell()
    testGetUnvisitedGetsAllNeighboursWhenUnvisited()
    testGetUnvisitedExcludesVisitedNeigbhours()
    testGetUnvisitedGetsNoVisitedCells()
    testRemoveWallOpensEastAndWestWalls()
    testRemoveWallOpensNorthAndSouthWalls()
    testRemoveWallOpensSouthAndNorthWalls()
    testRemoveWallOpensWestAndEastWalls()
    testOpenMaze()
    testOpenMazeOn1x1()
    testGetCellsGetsAllCells()
    testGetReachableCellsGetsNothingWhenAllWallsClosed()
    testGetReachableCellsReturnsHorizontalNeighbours()
    testGetReachableCellsReturnsVerticalNeighbours()
    testGetReachableSymmetry()

    testDFSGeneratorReturnsMaze()
    testDFSGeneratorVisitsAllCells()
    testDFSGeneratorCreatesConnectedMaze()
    testDFSGeneratorCreatesPerfectMaze()
    testDFSGeneratorSameSeedSameMaze()
    testDFSGeneratorWorksOn1x1()
    testDFSGeneratorWorksOnNonSquareMaze()
    testPrimsGeneratorReturnsMaze()
    testPrimsGeneratorVisitsAllCells()
    testPrimsGeneratorCreatesConnectedMaze()
    testPrimsGeneratorCreatesPerfectMaze()
    testPrimsGeneratorSameSeedSameMaze()
    testPrimsGeneratorWorksOn1x1()
    testPrimsGeneratorWorksOnNonSquareMaze()
    testWilsonsGeneratorReturnsMaze()
    testWilsonsGeneratorVisitsAllCells()
    testWilsonsGeneratorCreatesConnectedMaze()
    testWilsonsGeneratorCreatesPerfectMaze()
    testWilsonsGeneratorSameSeedSameMaze()
    testWilsonsGeneratorWorksOn1x1()
    testWilsonsGeneratorWorksOnNonSquareMaze()

    print("NO ERRORS")

runAllTests()