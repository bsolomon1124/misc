"""NumPy/SciPy implementation of Conway's Game of Life.

https://bitstorm.org/gameoflife/
"""

from itertools import repeat

import numpy as np
from scipy import signal

# Convolutional kernel that counts diagonals and top/bottom/sides as neighbors
diag_kernel = np.ones((3, 3), dtype=np.int8)
diag_kernel[1, 1] = 0

# Convolutional kernel that doesn't count diagonals as neighbors
cross_kernel = np.zeros((3, 3), dtype=np.uint8)
rows = np.array([[0, 2], [1, 1]])
cols = np.array([[1, 1], [0, 2]])
cross_kernel[rows, cols] = 1


class Board(np.ndarray):

    def __new__(cls, size=15, diag=True):
        """Inherit a square array of zeros, dimensions `size` X `size`."""
        obj = np.zeros((size, size), dtype=np.uint8).view(cls)
        if diag:
            obj.kernel = diag_kernel
        else:
            obj.kernel = cross_kernel
        return obj

    def clear(self, out=True):
        """Clear (reset) the board to be empty."""
        self[:] = 0.
        if out:
            return self

    def start(self, n, out=True):
        """Place a length-n row of ones somewhere randomly on the board."""
        if n >= self.shape[1]:
            raise ValueError('Piece must fit on board.')
        self.clear(out=False)

        row = np.random.randint(0, len(self))
        col = np.random.randint(0, self.shape[1] - n + 1)
        self[row, col:col+n] = np.ones((1, n), dtype=np.uint8)
        if out:
            return self

    @property
    def neighbors(self):
        """Elementwise number of neighbors."""
        # TODO: Borders fluid?  (We're currently treating them as such)
        return signal.convolve(self, self.kernel, mode='same')

    @property
    def is_empty(self):
        """True if entire board is empty.  'Stop' condition."""
        return np.count_nonzero(self) == 0

    def _evolve(self, out=True):
        """Make one turn."""
        populated = self.astype(np.bool_)
        empty_3n = np.logical_and(~populated, self.neighbors >= 3)
        pop_14n = np.logical_and(populated, np.logical_or(
            self.neighbors <= 1, self.neighbors >= 4))
        pop_23n = np.logical_and(populated, np.logical_or(
            self.neighbors == 2, self.neighbors == 3))
        self[:] = np.where(pop_14n, 0,
                           np.where(pop_23n, 1,
                                    np.where(empty_3n, 1, self)))
        if out:
            return self

    def evolve(self, out=True, turns=1):
        """Make multiple turns."""
        for _ in repeat(None, turns):
            self._evolve(out=False)
            if self.is_empty:
                break
        if out:
            return self
