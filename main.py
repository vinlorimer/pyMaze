from maze import Maze
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeSolvers import mouseSolver, humanSolver, aStarSolver
from mazeVisualisation import mazeVisualiser

maze = Maze(150,15)
renderer = mazeVisualiser(maze)
renderer.drawMaze()
renderer.waitForKey()
primsGenerator(maze)
maze.openMaze()
renderer.drawMaze()
renderer.waitForKey()
solution = aStarSolver(maze)   
renderer.drawMaze(path=solution)
renderer.keepOpen()