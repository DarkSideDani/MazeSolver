# Maze Solver

## Overview

The Maze Solver project is a Python application that generates and solves mazes using graphical visualization. The project utilizes Tkinter for rendering the maze and its solution, and employs algorithms for both maze generation and solving. The core functionality includes creating a maze, removing walls to form paths, and solving the maze using depth-first search.

## Features

- **Maze Generation**: Generates a maze using a randomized depth-first search algorithm. The maze is created with walls between cells, which are then removed to form a solvable path.
- **Maze Solving**: Uses depth-first search to find a path from the top-left cell to the bottom-right cell of the maze.
- **Graphical Interface**: Provides a visual representation of the maze and the solution using Tkinter. The maze and solution paths are drawn on a canvas, with walls being displayed or removed dynamically.

## Components

### 1. **Main Application (`main.py`)**

The main script sets up the graphical window and initializes the maze with specified dimensions. It handles the maze generation and solving processes, and ensures that the window remains open until the user closes it.

### 2. **Maze Class (`maze.py`)**

The `Maze` class is responsible for creating the maze structure, including:
- **Cell Initialization**: Creates a grid of cells, each with walls on all sides.
- **Maze Generation**: Uses a randomized depth-first search to remove walls and generate a solvable maze.
- **Breaking Entrance and Exit Walls**: Removes walls at the entrance (top-left) and exit (bottom-right) of the maze to ensure a path is available.
- **Solving the Maze**: Implements a depth-first search algorithm to find a path from the entrance to the exit.

### 3. **Cell Class (`cell.py`)**

The `Cell` class represents individual cells within the maze. Each cell can have walls on its four sides, and the class includes methods to:
- **Draw the Cell**: Draws the cell and its walls on the canvas. Walls are represented as lines, and removed walls are drawn in a different color to indicate they are no longer present.
- **Draw Movement Path**: Visualizes the path taken while solving the maze, with different colors indicating movement and undo actions.

### 4. **Graphics Handling (`graphics.py`)**

The `graphics.py` module defines the graphical window and drawing functions:
- **Window Class**: Manages the Tkinter window, including the canvas for drawing the maze and handling user interactions.
- **Point and Line Classes**: Represent geometric shapes used for drawing the maze and solution paths.

## Techniques Used

- **Depth-First Search (DFS)**: Employed both for generating the maze (to create a randomized layout) and for solving the maze (to find a path from start to finish).
- **Recursive Algorithms**: Utilized for both maze generation and solving, allowing for elegant and straightforward implementations.
- **Graphical Visualization**: Leveraged Tkinter to provide real-time feedback of the maze generation and solving processes, enhancing user interaction and experience.

## Getting Started

1. **Installation**: Ensure you have Python and Tkinter installed. Clone the repository and install any required dependencies.
2. **Run the Application**: Execute `main.py` to generate and solve a maze. The graphical window will display the maze and solution.
3. **Customization**: Modify the maze dimensions, cell size, and other parameters in `main.py` to explore different maze configurations.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.