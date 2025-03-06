from src.cell import Cell
from src.graphics import Window
import time

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

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
                print(f"cell {i},{j} has been added")
            self._cells.append(col)
            print(f"row {i} has been added")
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                print(f"now drawing cell {i}, {j}")
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * j
        x2 = self._x1 + (j + 1) * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        y2 = self._y1 + (i + 1) * self._cell_size_y
        print(f"cell in postion x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)