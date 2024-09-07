import tkinter as tk

from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        # Window title
        self.root.title("Maze Solver")
        # Window size
        self.root.geometry(f"{self.width}x{self.height}")
        
    def run(self):
        self.root.mainloop()
        
        
window = Window(800,600)
window.run()