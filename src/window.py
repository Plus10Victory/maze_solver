from tkinter import Tk, BOTH, Canvas
from src.line import Point, Line

# constructor should take a width and height
# create a new root widget using Tk() and save as a data member
# set the tilte property of the root widget
# create a canvas widget and save it as a data member
# pack the canvas widget so that it's ready to be drawn
# create a data member to represent that the window is "running" and set it to false

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False