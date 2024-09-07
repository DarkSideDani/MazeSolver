from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__root = Tk() # Root Widget
        self.__root.title("Maze Solver") # Window title
        
        self.__canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        
        self.__running = False # Data member to represent if the window is "running"
        
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # Close protocol
        
    def redraw(self):
        # Updating the window to process any pending events
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
            
    def close(self):
        self.__running = False # helps stop the wait_for_close loop