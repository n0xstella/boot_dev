"""
Issues with the _solve_r method in terms of pathing.
Was going for a more pythonic method but nevermind.
"""


import time
import random
from cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        # Ensure the seed is a supported type, otherwise set it to None
        if isinstance(seed, (int, float, str, bytes, bytearray)) or seed is None:
            self._seed = seed
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        # Initialize cells and draw them
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i, column in enumerate(self._cells):
            for j, cell in enumerate(column):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
    # Calculate the coordinates for the current cell based on its column (i) and row (j)
        x1 = self._x1 + i * self._cell_size_x  # x-coordinate of the top-left corner
        y1 = self._y1 + j * self._cell_size_y  # y-coordinate of the top-left corner
        x2 = x1 + self._cell_size_x            # x-coordinate of the bottom-right corner
        y2 = y1 + self._cell_size_y            # y-coordinate of the bottom-right corner
        
        # Now that you have the coordinates for the cell, you can access the corresponding cell object
        cell = self._cells[i][j]
        
        # Use the cell's draw method to display it
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win:
            self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Breaing the entrance wall
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        #Breaking the exit wall
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        directions = [
            (-1, 0),  # Left
            (1, 0),   # Right
            (0, -1),  # Up
            (0, 1)    # Down
        ]

        # Shuffle directions for randomness
        random.shuffle(directions)

        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Ensure the next cell is within bounds and not yet visited
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows and not self._cells[ni][nj].visited:
                # Break walls between the current cell and the next cell
                if di == -1:  # Left
                    self._cells[i][j].has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                elif di == 1:  # Right
                    self._cells[i][j].has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                elif dj == -1:  # Up
                    self._cells[i][j].has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                elif dj == 1:  # Down
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False

                # Recursively visit the next cell
                self._break_walls_r(ni, nj)

        # Redraw the current cell after processing
        self._draw_cell(i, j)


    def _reset_cells_visited(self):
        for i, column in enumerate(self._cells):
            for j, cell in enumerate(column):
                cell.visited = False
        return
            
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if (i,j) == (self._num_cols - 1, self._num_rows - 1):
            return True
        
        directions = [
            ((-1, 0), "has_left_wall", "has_right_wall"), # Move left
            ((0, 1), "has_right_wall", "has_left_wall"),  # Move right
            ((0, -1), "has_top_wall", "has_bottom_wall"), # Move up
            ((1, 0), "has_bottom_wall", "has_top_wall"), # Move down
        ]

        # Randomize directions to vary the solving path
        random.shuffle(directions)

        for (di, dj), curr_wall, next_wall in directions:
            ni, nj = i + di, j + dj  # Neighbor coordinates

            # Ensure the neighbor is within bounds
            if 0 < ni < self._num_cols and 0 < nj < self._num_rows:
                # Check both current cell's wall and neighbor's wall
                if (
                    not getattr(self._cells[i][j], curr_wall) and
                    not getattr(self._cells[ni][nj], next_wall) and
                    not self._cells[ni][nj].visited
                ):
                    print(f"Moving to cell ({ni}, {nj})")  # Debug: Moving to a neighbor

                    # Draw the move to the neighbor cell
                    self._cells[i][j].draw_move(self._cells[ni][nj])

                    # Recursively solve from the neighbor cell
                    if self._solve_r(ni, nj):
                        return True

                    # Undo the move if no solution is found
                    print(f"Backtracking from cell ({ni}, {nj})")  # Debug: Backtracking
                    self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)

        # No valid moves from this cell, backtrack
        print(f"No moves possible from ({i}, {j}), backtracking...")  # Debug: No moves
        self._cells[i][j].visited = False
        return False
        
    def _solve(self):
        return self._solve_r(0, 0)