import numpy as np

class Nodo:
    def __init__(self, board):
        # Si board es un numpy array lo copiamos, de lo contrario lo convertimos
        if isinstance(board, np.ndarray):
            self.board = board.copy()
        else:
            self.board = np.array(board)

    def __hash__(self):
        # Usamos los bytes internos del array para generar la huella
        return hash(self.board.tobytes())

    def __eq__(self, other):
        return isinstance(other, Nodo) and np.array_equal(self.board, other.board)

    def __str__(self):
        return str(self.board)