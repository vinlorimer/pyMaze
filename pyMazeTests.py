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
    Tests that the top left corners neighbours are (1,0) and (0,1) as any other coordinates wouldn't be neighbours, or would be neighbours 
    outside the bounds of the maze.
    """
    maze = Maze(3, 3)
    cell = maze.grid[0][0]

    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)

    expectedCoordinates = {(1,0),(0,1)}
    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursTopEdge():
    """
    """
    maze = Maze(3,3)
    cell = maze.grid[0][1]

    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)

    expectedCoordinates = {(0,0),(0,2),(1,1)}
    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursMiddleCell():
    """
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]

    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)

    expectedCoordinates = {(0,1),(1,2),(2,1),(1,0)}
    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetNeighboursBottomRight():
    """
    """
    maze = Maze(3,3)
    cell = maze.grid[2][2]

    neighbours = maze.getNeighbours(cell)
    neighboursCoordinates = getCellCoordinates(neighbours)

    expectedCoordinates = {(1,2),(2,1)}
    assert neighboursCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {neighboursCoordinates}"

def testGetUnvisitedGetsAllNeighboursWhenUnvisited():
    """
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]

    unvisitedCells = maze.getUnvisited(cell)
    unvisitedCellsCoordinates = getCellCoordinates(unvisitedCells)

    expectedCoordinates = {(0,1),(1,2),(2,1),(1,0)}
    assert unvisitedCellsCoordinates == expectedCoordinates, f"expected {expectedCoordinates}, got {unvisitedCellsCoordinates}"

def testGetUnvisitedExcludesVisitedNeigbhours():
    """
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
    """
    maze = Maze(3,3)
    cell = maze.grid[1][1]

    for neighbour in maze.getNeighbours(cell):
        neighbour.visited = True
    
    unvisitedCells = maze.getUnvisited(cell)

    assert unvisitedCells == [], f"expected empty list, got {unvisitedCells}"

def testRemoveWallOpensSouthAndNorthWalls():
    """
    """
    maze = Maze(2,1)
    topCell = maze.grid[0][0]
    bottomCell = maze.grid[1][0]

    maze.removeWall(topCell, bottomCell)

    assert topCell.SWall is False, "expected swall to be false"
    assert topCell.NWall is True, "expected nwall to be true"
    assert bottomCell.NWall is False, "expected nwall to be false"
    assert bottomCell.SWall is True, "expected swall to be true"

def testRemoveWallOpensNorthAndSouthWalls():
    """
    """
    maze = Maze(2,1)
    topCell = maze.grid[0][0]
    bottomCell = maze.grid[1][0]

    maze.removeWall(bottomCell, topCell)

    assert topCell.SWall is False, "expected swall to be false"
    assert topCell.NWall is True, "expected nwall to be true"
    assert bottomCell.NWall is False, "expected nwall to be false"
    assert bottomCell.SWall is True, "expected swall to be true"

def testRemoveWallOpensEastAndWestWalls():
    """
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
    maze = Maze(3,3)

    maze.openMaze()

    assert maze.startCell.NWall is False, "expected nwall to be false"
    assert maze.endCell.SWall is False, "expected swall to be false"

def testOpenMazeOn1x1():
    maze = Maze(1,1)

    maze.openMaze()

    assert maze.startCell == maze.endCell, "expected start cell and end cell to be the same cell"
    assert maze.startCell.NWall is False, "expected nwall to be open"
    assert maze.startCell.SWall is False, "expected swall to be openb"
    assert maze.startCell.EWall is True, "expected ewall to be closed"
    assert maze.startCell.WWall is True, "expected wwall to be closed"

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
    
    print("NO ERRORS")

runAllTests()