from src.cell import Cell
from src.graphics import Window
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x1 =x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


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
        x1 = self._x1 + self._cell_size_x * i
        x2 = self._x1 + (i + 1) * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = self._y1 + (j + 1) * self._cell_size_y
        print(f"cell in postion x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_left_wall = False
        entrance.draw(entrance._x1, entrance._y1, entrance._x2, entrance._y2)
        maze_exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        maze_exit.has_right_wall = False
        maze_exit.draw(maze_exit._x1, maze_exit._y1, maze_exit._x2, maze_exit._y2)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        current = self._cells[i][j]
        print(f"current cell: {i}, {j}")
        while True:
            not_visited = []
            if i != 0:
                left_cell = self._cells[i-1][j]
                if not left_cell.visited:
                    print(f"cell {i-1}, {j} not visited")
                    not_visited.append("left")
            if j != 0:
                up_cell = self._cells[i][j-1]
                if not up_cell.visited:
                    print(f"cell {i}, {j-1} not visited")
                    not_visited.append("up")
            if i < self._num_cols - 1:
                right_cell = self._cells[i+1][j]
                if not right_cell.visited:
                    print(f"cell {i+1}, {j} not visited")
                    not_visited.append("right")
            if j < self._num_rows - 1:
                down_cell = self._cells[i][j+1]
                if not down_cell.visited:
                    print(f"cell {i}, {j+1} not visited")
                    not_visited.append("down")

            if len(not_visited) is 0:
                current.draw(current._x1, current._y1, current._x2, current._y2)
                return   
            
            next = not_visited[random.randrange(0, len(not_visited))]
            not_visited.remove(next)

            if next is "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                #current.draw(current._x1, current._y1, current._x2, current._y2)
                self._break_walls_r(i-1, j)
            if next is "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                #current.draw(current._x1, current._y1, current._x2, current._y2)
                self._break_walls_r(i, j-1)
            if next is "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                #current.draw(current._x1, current._y1, current._x2, current._y2)
                self._break_walls_r(i+1, j)
            if next is "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                #current.draw(current._x1, current._y1, current._x2, current._y2)
                self._break_walls_r(i, j+1)


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False