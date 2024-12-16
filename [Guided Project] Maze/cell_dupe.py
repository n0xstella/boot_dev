from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2

        # Draw walls based on presence
        walls = {
            "left": (Point(x1, y1), Point(x1, y2), self.has_left_wall),
            "right": (Point(x2, y1), Point(x2, y2), self.has_right_wall),
            "top": (Point(x1, y1), Point(x2, y1), self.has_top_wall),
            "bottom": (Point(x1, y2), Point(x2, y2), self.has_bottom_wall),
        }

        for _, (start, end, has_wall) in walls.items():
            color = "black" if has_wall else "white"
            self._win.draw_line(Line(start, end), fill_color=color)

    def draw_move(self, to_cell, undo=False):
        # Ensure coordinates are initialized
        if (
            self._x1 is None or self._y1 is None or self._x2 is None or self._y2 is None or
            to_cell._x1 is None or to_cell._y1 is None or to_cell._x2 is None or to_cell._y2 is None
        ):
            return

        # Calculate centers of current cell and target cell
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y1 + self._y2) / 2
        to_x_center = (to_cell._x1 + to_cell._x2) / 2
        to_y_center = (to_cell._y1 + to_cell._y2) / 2

        # Draw the move line
        if self._win:
            line = Line(Point(x_center, y_center), Point(to_x_center, to_y_center))
            fill_color = "red" if not undo else "gray"
            self._win.draw_line(line, fill_color=fill_color)