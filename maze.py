class Cell():
    """
    A class to represent cells within the maze.
    """
    def __init__(self, row: int, column: int):
        """
        A method to construct the cell class.

        Parameters
        ---
        row: int | the row that the cell resides in (y coordinate)
        column: int | the column that the cell resides in (x coordinate)

        Properties
        ---
        row & column to store the coordinate of the cell within the grid of the maze
        visited property to know if a cell has been visited or not
        a property for each cardinal directions wall
        """
        self.row = row
        self.column = column
        self.visited = False
        self.NWall = True
        self.EWall = True
        self.SWall = True
        self.WWall = True

    def __eq__(self, value):
        pass

class Maze():
    """
    A class for the maze, with useful functions to aid in both generation & solving.
    """
    def __init__(self, rows: int, columns: int):
        """
        A method to construct the maze class.

        Parameters
        ---
        rows: int | the number of rows that the maze should be constructed with.
        columns: int | the number of columns that the maze should be constructed with.

        Properties
        ---
        rows & columns are the dimensions of the maze
        grid property uses a method stated just below to create the grid of cells that represent the maze
        startcell & endcell are hardcoded as I want it to always start top left and end bottom right B)
        """
        self.rows = rows
        self.columns = columns
        self.grid = self.createGrid()
        self.startCell = self.grid[0][0]
        self.endCell = self.grid[-1][-1]

    def createGrid(self):
        """
        A method to create the mazes grid.
        To do this it uses nested iteration to iterate through each row and for each row iterate through all columns on that row 
        and create a cell object, add each cell to a temporary list, when at the end of that row add it all to the grid

        Returns
        ---
        grid | a list that represents the grid of cells
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
        A method to get all surrounding AND IN BOUND cells around a specified cell.
        To do this just uses simple if checks to check indexing of cell coordinates with mazes total rows/columns.

        Paramters
        ---
        cell: Cell | takes a cell as an argument to look around.

        Returns
        ---
        neighbours | a list of all surrounding cells that are in bounds of the maze
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
        A method to get all unvisited cells around a specified cell.
        To do this uses the neighbours method to get all a cells neighbours then iterates through each one checking its visited
        property.

        Paramters
        ---
        cell: Cell | Takes a cell as an argument to check if its neighbours are unvisited or not.

        Returns
        ---
        unvisitedNeighbours | A list of all cell(s) around the specified cell that have their property visited == false.
        """
        cellNeighbours = self.getNeighbours(cell)
        unvisitedNeighbours = []
        
        for neighbour in cellNeighbours:
            if neighbour.visited is False:
                unvisitedNeighbours.append(neighbour)

        return unvisitedNeighbours
    
    def removeWall(self, cell: Cell, otherCell: Cell):
        """
        A method to remove the walls between two specified cells.
        To do this it uses conditional statements to check where in relation with each other the two cells are, then removes the
        corresponding walls by changing the two cells properties.

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
        A method to "open" the maze.
        Since start cell and end cell are hardcoded we know to always remove the north and south wall respectively... thats it.
        """
        self.startCell.NWall = False
        self.endCell.SWall = False
    
    def getCells(self):
        """
        A method to create a list of all cells within the maze.
        To do this create an empty list, then iterate through each row in the maze then as each row is a list iterate through that
        row and add each cell into the list.

        Returns
        ---
        cells | list of all cells in the maze
        """
        cells = []
        for row in self.grid:
            for cell in row:
                cells.append(cell)

        return cells
        

    def getReachableCells(self, cell: Cell):
        """
        A method to get all reachable cells i.e. check for cells that have no walls between them
        To do this create an empty list, then use conditional statements to check if the cells around the specified cell
        are in bounds of the maze and if the wall in that direction exists or not. If it is in bounds and the wall doesn't exist
        then add it to the list.

        Paramters
        ---
        cell: Cell | Takes a cell to check around

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