from src.graphics import Window
from src.cell import Cell
from src.maze import Maze

def main():
    win = Window(800, 600)

    #c = Cell(win)
    #c.draw(50, 50, 100, 100)

    #c2 = Cell(win)
    #c2.draw(100, 50, 150, 100)

    #c.draw_move(c2)

    maze = Maze(50,50,4,4,50,50,win)


    win.wait_for_close()
    

if __name__ == "__main__":
    main()