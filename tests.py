import unittest
from unittest.mock import MagicMock

from cell import Cell
from maze import Maze

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        # Test the creation of a maze with 12 columns and 10 rows
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        # Test the creation of a maze with 16 columns and 12 rows
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_cell_initialization(self):
        # Test the default initialization of a Cell object
        cell = Cell()
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)
        self.assertIsNone(cell._x1)
        self.assertIsNone(cell._x2)
        self.assertIsNone(cell._y1)
        self.assertIsNone(cell._y2)
        self.assertIsNone(cell._win)
    
    def test_set_cell_walls(self):
        # Test setting wall attributes of a Cell object
        cell = Cell()
        cell.has_left_wall = False
        cell.has_right_wall = False
        cell.has_top_wall = False
        cell.has_bottom_wall = False
        
        self.assertFalse(cell.has_left_wall)
        self.assertFalse(cell.has_right_wall)
        self.assertFalse(cell.has_top_wall)
        self.assertFalse(cell.has_bottom_wall)
    
    def test_cell_draw(self):
        # Test that a Cell is drawn correctly with the expected walls
        mock_win = MagicMock()  # Create a mock Window object
        cell = Cell(mock_win)
        
        # Draw a cell with specific coordinates
        cell.draw(10, 10, 20, 20)
        
        # Check that draw_line was called with the correct Line objects
        self.assertEqual(mock_win.draw_line.call_count, 4)
        
        # Retrieve the arguments passed to draw_line
        calls = mock_win.draw_line.call_args_list
        
        # Check the first line (left wall)
        line = calls[0][0][0]
        self.assertEqual(line.p1.x, 10)
        self.assertEqual(line.p1.y, 10)
        self.assertEqual(line.p2.x, 10)
        self.assertEqual(line.p2.y, 20)
        
        # Check the second line (top wall)
        line = calls[1][0][0]
        self.assertEqual(line.p1.x, 10)
        self.assertEqual(line.p1.y, 10)
        self.assertEqual(line.p2.x, 20)
        self.assertEqual(line.p2.y, 10)
        
        # Check the third line (right wall)
        line = calls[2][0][0]
        self.assertEqual(line.p1.x, 20)
        self.assertEqual(line.p1.y, 10)
        self.assertEqual(line.p2.x, 20)
        self.assertEqual(line.p2.y, 20)
        
        # Check the fourth line (bottom wall)
        line = calls[3][0][0]
        self.assertEqual(line.p1.x, 10)
        self.assertEqual(line.p1.y, 20)
        self.assertEqual(line.p2.x, 20)
        self.assertEqual(line.p2.y, 20)
    
    def test_maze_dimensions(self):
        # Test the maze dimensions to ensure the number of cells matches
        num_cols = 5
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Check that the maze dimensions are as expected
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)
        
        
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
