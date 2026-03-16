from maze import Maze
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeVisualiser import visualiseMaze

maze = Maze(10,10)
maze = DFSGenerator(maze)
#maze2 = primsGenerator(maze)
#maze = wilsonsGenerator(maze)
maze.openMaze()
visualiseMaze(maze)

# commentttt