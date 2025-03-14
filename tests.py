import unittest
from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][1].has_right_wall,
            False,
        )

    
    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 2, 2, 10, 10, win=None)
        m1._cells[0][0].visited = True
        m1._cells[1][1].visited = True
        m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[0][0].visited,
            False,
        )
        self.assertEqual(
            m1._cells[1][1].visited,
            False,
        )

    
if __name__ == "__main__":
    unittest.main()