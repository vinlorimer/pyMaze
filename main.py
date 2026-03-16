from maze import Maze
from mazeGenerators import DFSGenerator, primsGenerator, wilsonsGenerator
from mazeVisualiser import visualiseMaze

maze = Maze(100,100)
#maze = DFSGenerator(maze)
#maze2 = primsGenerator(maze)
#maze = wilsonsGenerator(maze)
maze.openMaze()
visualiseMaze(maze)

# commentttt