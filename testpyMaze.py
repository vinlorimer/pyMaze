from maze import Maze, Cell
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver

def testCellConstruction():
    """
    This tests the constructor method in the cell class.
    """
    cell = Cell(6,7)
     