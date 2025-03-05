from src.cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self._x1 =x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
                self._draw_cell(i, j)
            self._cells.append(col)

    def _draw_cell(self, i, j):
        #set cells x1, x2, y1, y2 points
        #x1 = self._x1 * i * self._cell_size_x
        #x2 = self._x2 * (i+1) * self._cell_size_x 
        #self._cells[i][j].draw(x1, x2, y1, y1)
