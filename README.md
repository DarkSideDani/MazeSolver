# Maze Generator and Solver

This project implements a maze generator and solver using Python's Tkinter for graphical display. The maze is generated using a recursive backtracking algorithm and can be solved using depth-first search.

## Features

- **Maze Generation**: Generates a random maze using recursive backtracking.
- **Maze Solving**: Solves the maze using depth-first search.
- **Graphical Display**: Visualizes the maze and its solution using Tkinter.
- **Executable**: The project includes an executable version for easy execution.

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DarkSideDani/MazeSolver.git
   cd MazeSolver
   ```

2. **Install Dependencies**:
   - Ensure you have Python installed. Tkinter is included with standard Python installations, so no additional installation is needed for Tkinter.
   - Install PyInstaller if you want to create executables. You can install it using pip:
     ```bash
     pip install pyinstaller
     ```

## Running the Project

### Using the Python Script

1. **Run the Main Script**:
   - Execute the following command to run the project using the Python script:
     ```bash
     python main.py
     ```

## How It Works

- **Maze Generation**: The maze is created using a recursive backtracking algorithm, which carves out paths in a grid of cells.
- **Maze Solving**: The maze is solved using a depth-first search algorithm, which finds a path from the start to the end of the maze.
- **Graphical Display**: Tkinter is used to render the maze and solution on the screen. The maze is drawn with walls, and the solution path is highlighted.

## Testing

To ensure the functionality of the maze generator and solver, unit tests have been written using Python's `unittest` module. To run the tests, use the following command:

```bash
python -m unittest discover
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter for the graphical user interface.
- Recursive backtracking algorithm for maze generation.
- Depth-first search for maze solving.

---