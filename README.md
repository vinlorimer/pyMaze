# pyMaze
A library to generate, solve and visualise pMazes. 
## Tutorial
In this tutorial we will see how to use pyMaze to generate and solve a maze. The goal is to create a maze, generate its walls using a standard maze algorithm, solve it using maze solver, and then visualise the maze using Pygame. 

We start by importing Maze from maze and creating a 20x20 maze. 

```python
>>> from maze import Maze
>>> maze = Maze(20, 20)
>>> (maze.rows, maze.columns)
(20, 20)

```


From this a `Maze` object is created containing a 20x20 grid of cell objects. The start cell is the top-left cell (`maze.startCell`) and the end cell is the bottom-right cell (`maze.endCell`).

Now we generate the maze using the DFS-based generator, also to repeat using the same maze we use random:

```python

>>> import random as rnd
>>> rnd.seed(0)
>>> from mazeGenerators import DFSGenerator
>>> maze = DFSGenerator(maze)

```

The generator will modify the maze by removing walls between cells, now the maze becomes fully connected (there now exists a route through the maze), then the function returns the generated maze. 

Before we can solve or visualise the maze, we "open" the maze so there is an entrance and exit:

```python
>>> maze.openMaze()

```

The start cell's north wall is removed (entrance) and the end cell's south wall is removed (exit).

Now we're in a position to solve the maze using the A* Solver:

```python
>>> from mazeSolvers import aStarSolver
>>> path = aStarSolver(maze)
>>> (len(path) > 0)
True

```

The path is then given as a list of cell objects describing a valid route from start to end. The first element of the path (path[0]) is the start cell and the last element (path[-1]) is the end cell.

The length of the path can be checked:

```python
>>> len(path) > 0
True

print(len(path))
```


A positive integer will be printed (larger mazes typically print longer paths). 

We can compare solvers by also solving the maze using the left-hand rule:

```python
>>> from mazeSolvers import humanSolver
>>> human_path = humanSolver(maze, rule="L")
>>> len(human_path) >0
True

print(len(path))
```

The left hand rule will usually produce a valid route, but it may be longer than the A* route. 

Finally, we can visualise the generated maze. This will open a Pygame window and draw the maze walls:

```python
from mazeVisualisation import mazeVisualiser
vis = mazeVisualiser(maze)
vis

```

A visualiser object is created and is ready to draw the maze.

From here we can display the maze, the solution path and the path length.

  
```python
vis.visualise(path)

```
A Pygame window will be opened showing the maze. The start cell is green and the end cell is red. The solution path is blue and the path length is displayed.

## How to guides
### How to generate a maze with DFS
Use this when you want a standard maze quickly.

**Steps:**

1. Create a maze with your chosen size.
2. Run DFSGenerator.
3. Open the entrance and exit. 

```python 
>>> from maze import Maze

>>> from mazeGenerators import DFSGenerator

>>> maze = Maze(rows=20, columns=20)
>>> maze = DFSGenerator(maze)
>>> maze.openMaze()

```

The maze is generated (walls removed between many cells) and the entrance and exit are oepn (start top-left, end bottom-right).

### How to generate a maze with a different algorithm (Prim/ Wilson)
Use this when you want a different "style" of maze without changing anything else.

**Steps:**

Swap the generator function you call.

```python
>>> from maze import Maze
>>> from mazeGenerators import primsGenerator, wilsonsGenerator

>>> maze = Maze(rows=20, columns=20)

>>> # Choose ONE:
>>> maze = primsGenerator(maze)
>>> # maze = wilsonsGenerator(maze)

>>> maze.openMaze()

```

You will get a maze of the same size but with a different structure.

### How to solve a maze with A* (shortest route)
Use this when you want an efficient path from start to end.

**Steps:**

1. Generate a maze.
2. Solve the maze using `aStarSolver`.

```python
>>> from maze import Maze
>>> from mazeGenerators import DFSGenerator
>>> from mazeSolvers import aStarSolver

>>> maze = Maze(rows=20, columns=20)
>>> maze = DFSGenerator(maze)
>>> maze.openMaze()

>>> path = aStarSolver(maze)
>>> len(path) > 0
True

print(len(path))

```

This will give:
- A path by a list of cell objects.
- path[0] is th start cell (`maze.startCell`).
- path[-1] is the end cell (`maze.endCell`).
- Printing `len(path)` outputs a positive integer.

### How to solve a maze using the human left-hand or right-hand rule.
Use this when you want a 'human-style" route that may not be the shortest path.

**Steps:** 

1. Generate a maze.
2. Call `humanSolver` with a rule (left hand or right hand).

```python
>>> from maze import Maze
>>> from mazeGenerators import DFSGenerator
>>> from mazeSolvers import humanSolver

>>> maze = Maze(rows=20, columns=20)
>>> maze = DFSGenerator(maze)
>>> maze.openMaze()

>>> left_path = humanSolver(maze, rule="L")
>>> right_path = humanSolver(maze, rule="R")
>>> len(left_path) > 0
True
>>> len(right_path) > 0
True

print(len(left_path), len(right_path))

```

A valid path is returned in most cases, but the human-rule path may be longer than A* path.

### How to run a random "mouse" solver (for exploration).
Use this when you want a path that behaves like random wandering. 

**Steps:**

1. Generate a maze.
2. Call `mouseSolver`.
3. Use `maxSteps` to prevent infinite wandering.

```python
>>> from maze import Maze
>>> from mazeGenerators import DFSGenerator
>>> from mazeSolvers import mouseSolver

>>> maze = Maze(rows=20, columns=20)
>>> maze = DFSGenerator(maze)
>>> maze.openMaze()

>>> mouse_path = mouseSolver(maze, maxSteps=10000)
>>> len(mouse_path) > 0
True

print(len(mouse_path))

```

This will return a list of visited cells (the mouse's journey), if it fails to reach the end within `maxSteps`, the the path will stop at that limit. 

### How to visualise a generated maze using Pygame.
Use this when you want to view the maze layout in a window.

**Steps:**

1. Generate a maze.
2. Call `mazeVisualiser(maze)`.

```python
from mazeVisualisation import mazeVisualiser
vis = mazeVisualiser(maze)
vis.visualise()

```

A widow opens showing maze walls, start cell (green), and end cell (red), but no path is drawn.

#### How to visualise a maze with a solved path.

When you want to show the route produced by a solver use the following.

```python
from mazeVisualisation import mazeVisualiser
vis = mazeVisualiser(maze)
vis.visualise(path)

```
The solver path presented is coloured blue and the window displays the solution length.

### How to compare solvers on the same maze.
Use this when you want to compare "efficiency" of different solvers using a simple metric like path length.

**Steps:**
1. Generate **one** maze.
2. Solve it using multiple solvers.
3. Compare `len(path)`.

```python
>>> from mazeSolvers import aStarSolver, humanSolver, mouseSolver

>>> a_star_path = aStarSolver(maze)
>>> left_hand_path = humanSolver(maze, rule="L")
>>> mouse_path = mouseSolver(maze, maxSteps=10000)

>>> len(a_star_path) > 0
True
>>> len(left_hand_path) > 0
True
>>> len(mouse_path) > 0
True

print("A* steps:", len(a_star_path))

print("Left-hand steps:", len(left_hand_path))

print("Mouse steps:", len(mouse_path))

```

For each route a positive integer will be returned. A* should usually produce the shortest route (fewest steps). Human and mouse solvers will typically take more steps.

## Explanation.
### Mazes as a simple maths model.

A grid maze can be viewed as a graph.
- Each cell is a vertex (node)
- A passage between 2 adjacent cells is an edge.
- Walls determine whether an edge exists: if there's no wall between two neighbouring cells, the cells are connected.

Solving the maze then becomes a graph problem: find a route from the start cell $s$ to the end cell $t$.

If the maze has $R$ rows and $C$ columnns, then the total number of cells is
$V = RC$.

Two cells are neighbours if they share a side (north, south, east, west). A cell has at most 4 neighbours (less at boundaries).

### Perfect mazes.
Many classic maze generators aim to produce a perfect maze, meaning:
- The maze is connected (every cell can be reached from every other cell)
- The maze has no loops (there's exactly one simple path between any 2 cells).

These properties create the "maze feel":
- No loops mean dead ends naturally appear
- The route from $s$ and $t$ is unique, so the maze has a clear correct solution.
  
pyMaze focuses on generation methods that produce mazes with strong structure and reliable solvability. 

### Why we store walls on each cell.
In pyMaze each cell stores four wall flags: north, east, south, west. This representation keeps the whole library consistent:
- Generation removes walls to create passages, 
- Solving moves only through open walls, 
- Visualisation draws whichever walls remain.

This wall based model makes it easy to switch between different generators and solvers without changing how the maze is stored.

### Neighbours vs reachable cells.
pyMaze uses two useful ideas:
- Neighbours: cells next to you in the grid (up/ down/ right/ left), regardless of walls.
- Reachable cells: Neighbours that you can actually move to because there is no wall blocking the way. 

This is useful beacuse generators will often check neighbours to decide where to carve and solvers must use reachable cells so they don't "walk through walls".

### Maze generation. 
Maze generation starts with all walls present, then the algorithm adds edges by removing walls between neighbouring cells to build a connected maze. Each time we remove a wall between 2 adjacent cells we add an edge.

A generator algorithm is essentially a rule for deciding which walls to remove to build a desirable maze. Different rules create different maze characteristics (corridor length, branching, number of dead ends), even when they satisify the same core properties (connectivity, no loops).

#### DFS generation (depth-first carving)
The DFS- style generator explores "as far as possible" before backtracking:

1. Start at a cell and mark it as visited.
2. Randomly choose an unvisited neighbour, carve a passage to it, and move there.
3. If no unvisited neighbours exist, back track to the most recent cell that still has unvisited neighbours.

In return this tends to create longer corrdiors and many dead ends. This is beacuse DFS commits deeply and backtracking leaves behind terminal branches. 

#### Prim-style generation (frontier growth)
A Prim-style generator grows the maze outward from a visited region:
1. Maintain a set of candidate cells next to the visited region (the "frontier").
2. Pick a random candidate cell.
3. Connect it to a random visited neighbour.
  
This will tend to create more evenly distributed branching and shorter corrdiors in comparison to DFS in many cases.

#### Wilson's algorithm and loop-erased random walks. 
Wilson's algorithm generates a maze using random walks:
1. Start with one visited cell.
2. Pick an unvisted cell and perform a random walk until it reaches the visited set. 
3. If the walk forms a loop, erase the loop (loop-erasure).
4. Carve a passage along the remaining walk, and marking those cells as visted. 

The loop-erasure step is the key idea: it prevents cycles and produces mazes that look more "uniform" (less biased).

### Solving a maze.
Once a maze is generated, solving it means finding a path from $s$ to $t$. If every move has equal cost, the shortest path is the route with the smallest number of steps.

#### A* solving and why it is efficient. 
A* is a goal-directed search method that balances:
- The cost so far (steps from start to current cell)
- An estimate of how far remains (a heurustic distance to the goal).

This helps A* "aim" toward the exit rather than exploring blindly, so it typically explores fewer cells than a purely uniformed method, while still finding a valid route when one exists. 

#### Human-style wall following(left-hand/ right-hand).
Human wall-following solvers simulate a local rule: always keep one hand on a wall (left-hand or right-hand).

This produces a path that can be very different from the shortest path because it is based on local choices rather than global optimality.

From a modelling viewpoint, wall following is useful because it mimics a realistic strategy a person might use without knowing the full map.

#### Mouse solver (random exploration).
The mouse solver simulates a very simple way of navigating a maze:
- At each step, it looks at cells it can actually move to (reachable neighbours).
- It chooses one at random.
- It repeats until it reaches the end (or hits a safety limit).
  
Because the mouse makes random decisions, the path it produces is usally:
1. Not the shortest path.
2. Often contains revisits/ loops.
3. Highly variable (two runs can look different).

From a modelling viewpoint, the mouse solver is useful beacuse it represents a "no strategy" baseline - like someone exploring without a plan. 

### Difficulty and comparison.
Maze diffciulty is subjective, so pyMaze treats it as something we define using measureable features like the the shortest path length. We compare lengths of routes as typically a maze with a longer route often feels harder.

### Maze visualisation. 
The maze visualiser is responsible for turning the maze data structure into something the user can see without changing the maze. It will read:
- each cell's position (row, column)
- each cell's wall flags (NWall, EWall, SWall, WWall)
- and optionally a solver path (a list of cells)

The visualiser draws in layers:
1. Background.
2. Path Cells.
3. Start cell (green) and end cell (red).
4. Walls (black lines on top).

This order ensures the wall lines remain visible even when cells are coloured.

Visualisation is seperate from generating and solving for modularity as generating and solving can run without the need for graphics also, we can display the same maze using different renderers and the visualiser is optional for the user.

## Reference. 

### List of functionality.
The following classes are provided in pyMaze:
- `Cell`
- `Maze`

The following generation functions are provided in mazeGenerators:
- `DFSGenerator`
- `primsGenerator`
- `wilsonsGen erator`

The following solving functions are provided in mazeSolvers:
- `aStarSolver`
- `humanSolver`
- `mouseSolver`

The following visualisation function is provided in mazeVisualiser:
- `mazeVisualiser`

The following are used in Maze internally by generators and solvers:
- `createGrid`
- `getNeighbours`
- `getUnvisited`
- `removeWall`
- `openMaze`
- `getcells`
- `getReachableCells`

### Testing the software
To test the code:

```python
$ python testpyMaze.py
```

To test the documentation:

```python
$ python -m doctest README.md
```

### Bibliography.

The following are sites and wikipedia pages which give an insightive overview of maze generation algorithms, maze solving algorithms and graph theory.

- [Graph theory](https://en.wikipedia.org/wiki/Graph_theory)
- [Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Maze-solving algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
- [Maze Generation Algorithms - An Exploration](https://professor-l.github.io/mazes/)
