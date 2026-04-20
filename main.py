from maze import Maze
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver
from mazeVisualisation import mazeVisualiser

maze = Maze(50,50)
visualiser = mazeVisualiser(maze)
visualiser.visualise()
maze = DFSGenerator(maze, seed = 5)
visualiser.visualise()
mazeSolution = aStarSolver(maze)
visualiser.visualise(mazeSolution)

test = (maze.rows, maze.columns)
print(test)
