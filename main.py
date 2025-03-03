from tkinter import Tk, BOTH, Canvas
from src.window import Window
from src.line import Point, Line

def main():
    win = Window(800, 600)

    point_a = Point(150, 150)
    point_b = Point(400, 150)

    line_a = Line(point_a,point_b)
    win.draw_line(line_a, fill_color="black")

    win.wait_for_close()

if __name__ == "__main__":
    main()