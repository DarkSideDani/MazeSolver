from graphics import Window, Line, Point
from maze import Maze
import sys

def main():
    # Main function to set up and run the maze generation and display.
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    
    # Calculate the size of each cell based on the screen size and margin
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    # Create a Window object with specified width and height
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    # Create a Maze object with specified parameters
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    # Wait for the window to close
    win.wait_for_close()
    

main()