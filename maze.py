class Cell():
    """

    This class is for cells within the grid of our mazes, it simply creates the object "cell" which has the following properties:
    row & column (integers) then visited, nwall, ewall, swall & wwall (all booleans).

    I.E.

    cell = Cell(0,1) 
    creates a cell object that is on the first row and second column with the properties visited set to false and
    nwall, ewall, swall and wwall all set to true.
    
    """
    def __init__(self, row: int, column: int):
        """

        Constructor, takes in row & column values and then assigns boolean values to visited and each wall.
        
        """
        self.row = row
        self.column = column
        self.visited = False
        self.NWall = True
        self.EWall = True
        self.SWall = True
        self.WWall = True


class Maze():
    """

    This is the class for our maze, creates a maze object which is a grid of cell objects.

    I.E.
    maze = Maze(2,2)
    creates a maze object that has 4 cells ([0][0],[0][1],
                                            [1][0],[1][1])
    each of the cells have the properties declared in the cell class.

    """
    def __init__(self, rows: int, columns: int):
        """

        Constructor, as above mentioned takes rows & columns as parameters and assigns them to itself, then creates a grid using
        the createGrid function.
        
        """
        self.rows = rows
        self.columns = columns
        self.grid = self.createGrid()

    def createGrid(self):
        """

        Creates an empty list (grid) then uses nested iteration to loop through each row & column. Logic is as follows:

        for each row, create a temporary list while on the specified row, and then go through each column on that row adding the 
        cell from each column into the temporary list for that specified row. Once finished looping through all of the columns
        append that row into the list grid. Once finished going through all rows, it will return the list grid.
        
        """ 
        grid = []

        for row in range(self.rows):
            tempRowList = []
            for col in range(self.columns):
                cell = Cell(row, col)
                tempRowList.append(cell)
            grid.append(tempRowList)

        return grid
       
    def getNeighbours(self, cell: Cell):
        """

        Takes a cell as its parameter, then initiates two variables (cellRow & cellColumn) using the parameters properties, and an
        empty list named neighbours.

        Four if statements to check if the north, south, west and east cells are in bounds of the grid, if they are then add them to 
        the list neighbours, once all four potential neighbours have been checked return the list of neighbours.
       
         """
        neighbours = []

        if cell.row-1 >= 0:
            neighbours.append(self.grid[cell.row-1][cell.column])
        if cell.row+1 <= self.rows-1:
            neighbours.append(self.grid[cell.row+1][cell.column])
        if cell.column-1 >= 0:
            neighbours.append(self.grid[cell.row][cell.column-1])
        if cell.column+1 <= self.columns-1:
            neighbours.append(self.grid[cell.row][cell.column+1])

        return neighbours

    def getUnvisited(self, cell: Cell):
        """

        Again, take cell as a parameter, then using the findNeighbours function create a list called cellNeighbours that contain
        all valid neighbours of the specified cell. Initiate an empty list called unvisitedNeighbours in preperation to store 
        all neighbouring cells that have visited as false. Check each cell in the list to see if their visited property is false,
        if it is false add to the empty list. Once all four have been checked return the new list of all unvisited neighbours.
        
        """
        cellNeighbours = self.getNeighbours(cell)
        unvisitedNeighbours = []
        
        for neighbour in cellNeighbours:
            if neighbour.visited is False:
                unvisitedNeighbours.append(neighbour)

        return unvisitedNeighbours
    
    def removeWall(self, cell: Cell, otherCell: Cell):
        """
        
        Takes two cells as parameters, then gets the row & column position of each of them and stores them in variables. Then just 
        an if, elif statement that checks the north, south east and west of the current cell to see where the other cell is, if it
        finds it then it removes the two walls between them.

        """

        if (cell.row < otherCell.row):
            cell.SWall = False
            otherCell.NWall = False
        elif (cell.row > otherCell.row):
            cell.NWall = False
            otherCell.SWall = False
        elif (cell.column < otherCell.column):
            cell.EWall = False
            otherCell.WWall = False
        elif (cell.column > otherCell.column):
            cell.WWall = False
            otherCell.EWall = False

    def openMaze(self):
        """

        Simply chooses the top left cell ([0][0]) to be the start and removes the north wall and then chooses the bottom right 
        ([-1][-1] which is last cell in grid) to be the end and removes south wall.

        """
        startCell = self.grid[0][0]
        startCell.NWall = False
        finishCell = self.grid[-1][-1]
        finishCell.SWall = False
    
    def getCells(self):
        """

        TO DO
        
        """
        cells = []
        for row in self.grid:
            for cell in row:
                cells.append(cell)

        return cells
        

    def getReachableCells(self, cell: Cell):
        """
        
        TO DO
        
        """
        reachableCells = []

        if cell.row-1 >= 0 and cell.NWall == False:
            reachableCells.append(self.grid[cell.row-1][cell.column])
        if cell.row+1 <= self.rows-1 and cell.SWall == False:
            reachableCells.append(self.grid[cell.row+1][cell.column])
        if cell.column-1 >= 0 and cell.WWall == False:
            reachableCells.append(self.grid[cell.row][cell.column-1])
        if cell.column+1 <= self.columns-1 and cell.EWall == False:
            reachableCells.append(self.grid[cell.row][cell.column+1])
            
        return reachableCells