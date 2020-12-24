import numpy as np

from brange import brange


# Player colors
BLACK = -1
WHITE = 1


class Game:
    def __init__(self, width, height):
        # Who's the current player
        self.turn = np.random.choice([BLACK, WHITE])

        # Dimensionality
        self.width = width
        self.height = height

        # Board
        self.board = np.zeros((self.width, self.height))
        self.available = (None, set(), set())

    def __getitem__(self, xy):
        x, y = xy
        return self.board[x][y]

    def __setitem__(self, xy, value):
        x, y = xy
        self.update(x, y, value)

    def update(self, x, y, value):
        self.board[x][y] = value
        
        # Do nothing if removing piece
        # TODO: Consider this later!
        if value == 0:
            return

        # Loop through all ---

    def is_blocked(self, a, b):
        """ Check if two tiles are blocked by the other player """

        # Separate each component
        ax, ay = a
        bx, by = b

        color = self[ax, ay]

        if color == 0:
            raise RuntimeError("Can't check if path is blocked without a defined color")
        

        # Distance between tiles
        dx = bx - ax
        dy = by - ay

        # Polarity
        plx = 1 if dx > 0 else -1
        ply = 1 if dy > 0 else -1

        if abs(dx) == abs(dy) or abs(dx) not in (1, 2) or abs(dy) not in (1, 2):
            raise ValueError('Tiles must be a Horse move apart')

        # Pick the two lines determining the connection
        if abs(dx) > abs(dy):
            u = self[ax:bx - plx, by]
            v = self[ax + plx:bx, ay]
        else:
            u = self[bx, ay:by - ply]
            v = self[ax, ay + ply:by]

        # Check whether either of the lines
        # is blocked by a piece of the opponent's color
        
        u_blocked = any(i == -color for i in u)
        v_blocked = any(j == -color for j in v)

        if u_blocked and v_blocked:
            return True
        return False

    def is_connected(self, x, y):
        for px, py in self.get_hooks(x, y):
            if self[px, py] == self[px, py]:
                pass

    # Areas / Regions

    def affected(self, x, y):
        n = 3
        for i in range(-n, n + 1):
            spread = n - abs(i)
            for j in range(-spread, spread + 1):
                yield x + i, y + j