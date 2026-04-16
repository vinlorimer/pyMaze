from maze import Maze, Cell
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver

def testCellConstruction():
    """
    This tests the constructor method in the cell class.
    """
    cell = Cell(6,7)
    assert cell.row == 6, "unexpected row"
    assert cell.column == 7, "unexpected column"
    assert cell.visited == False, "expected to be unvisited"
    assert cell.NWall == True, "expected a north wall"
    assert cell.EWall == True, "expected an east wall"
    assert cell.SWall == True, "expected a south wall"
    assert cell.WWall == True, "expected a west wall"

def testMazeConstructorAttributes():
    """
    This tests that the attributes in the constructor for the maze class are correct for a 3x3 maze.
    """
    maze = Maze(3,3)
    assert maze.rows == 3, "expected 3 rows"
    assert maze.columns == 3, "expected 3 columns"



testCellConstruction()
testMazeConstructorAttributes()