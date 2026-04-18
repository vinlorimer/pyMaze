class Cell:
    """
    A class to represent a cell within the maze.
    """
    def __init__(self, row: int, column: int):
        """
        A method to construct the cell class.

        Parameters
        ---
        row: int | The row that the cell resides in (y coordinate)
        column: int | The column that the cell resides in (x coordinate)

        Attributes
        ---
        row | the cell's row position
        column | the cell's column position
        visited | the boolean value of whether or not a cell has been visited
        NWall | the boolean value to represent the north wall
        EWall | the boolean value to represent the east wall
        SWall | the boolean value to represent the south wall
        WWall | the boolean value to represent the west wall
        """
        self.row = row
        self.column = column
        self.visited = False
        self.NWall = True
        self.EWall = True
        self.SWall = True
        self.WWall = True

class Maze:
    """
    A class to represent a maze with useful methods to help in generation and solving said maze.
    """
    def __init__(self, rows: int, columns: int):
        """
        A method to construct the maze class.

        Parameters
        ---
        rows: int | The number of rows in the maze.
        columns: int | The number of columsn in the maze.

        Attributes
        ---
        rows | The number of rows in the maze.
        columns | The number of columns in the maze.
        grid | The 2D list of cell objects that represent the maze.
        startCell | Top left cell of the maze.
        endCell | Bottom right cell of the maze.
        """
        self.rows = rows
        self.columns = columns
        self.grid = self.createGrid()
        self.startCell = self.grid[0][0]
        self.endCell = self.grid[-1][-1]

    def createGrid(self):
        """
        A method to create the grid for the maze.

        Returns
        ---
        grid | The 2D list of cell objects that represent the maze.
        """ 
        grid = []

        for row in range(self.rows):
            tempRowList = []
            for column in range(self.columns):
                cell = Cell(row, column)
                tempRowList.append(cell)
            grid.append(tempRowList)

        return grid
       
    def getNeighbours(self, cell: Cell):
        """
        A method to return all adjacent in-bound neighbouring cells of the specified cell.

        Parameters
        ---
        cell: Cell | The cell whose neighbours we look for.
        
        Returns
        ---
        neighbours | A list of the neighbouting cells.
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
        A method to get all unvisited neighbouring cells around the specified cell.
        
        Paramters
        ---
        cell: Cell | The cell whose neighbours are checked.
        
        Returns
        ---
        unvisitedNeighbours | A list of the neighbouring cells whose visited attribute is false.
        """
        cellNeighbours = self.getNeighbours(cell)
        unvisitedNeighbours = []
        
        for neighbour in cellNeighbours:
            if neighbour.visited == False:
                unvisitedNeighbours.append(neighbour)

        return unvisitedNeighbours
    
    def removeWall(self, cell: Cell, otherCell: Cell):
        """
        Removes the walls between two neighbouring cells.

        Parameters
        ---
        cell: Cell | First specified cell
        otherCell: Cell | Second specified cell
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
        A method to open the maze entrance and exit by removing the north wall of the start cell
        and the south wall of the end cell.
        """
        self.startCell.NWall = False
        self.endCell.SWall = False
    
    def getCells(self):
        """
        A method to return a list of all the cells within the maze.

        Returns
        ---
        cells | A list containing every cell in the maze.
        """
        cells = []
        for row in self.grid:
            for cell in row:
                cells.append(cell)

        return cells
        

    def getReachableCells(self, cell: Cell):
        """
        A method to get all the cells that can be directly reached from the specified cell.
        The cells are "reachable" if it is a neighbouring cell and there is no walls between them.

        Paramters
        ---
        cell: Cell | The cell whose neighbours need to be checked if reachable.

        Returns
        ---
        reachableCells | Return the list of all cell(s) that are reachable
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