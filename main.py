from maze import Maze
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver
from mazeVisualisation import mazeVisualiser

maze = Maze(150,150)
visualiser = mazeVisualiser(maze)
visualiser.visualise()
maze = wilsonsGenerator(maze, seed = 5)
visualiser.visualise()
mazeSolution = humanSolver(maze, "l")
visualiser.visualise(mazeSolution)