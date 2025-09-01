from AgenteIA.AgenteBuscador import AgenteBuscador
from Nodo import Nodo
import numpy as np
import copy

class AgentePuzzle(AgenteBuscador):
    def __init__(self):
        super().__init__()
        self.costos = [[]]
        self.distacias_manhattan = [[]]

    def generar_hijos(self, estado):
        # Se asume que 'estado' es un array plano (1D)
        board = np.array(estado)
        total = board.size
        N = int(np.sqrt(total))  # lado del tablero
        hijos = {}

        # Encontrar el índice del 0 en el array plano
        idx_zero = np.where(board == 0)
        row = idx_zero // N
        col = idx_zero % N

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in movimientos:
            new_row = row + dx
            new_col = col + dy
            if 0 <= new_row < N and 0 <= new_col < N:
                new_idx = new_row * N + new_col
                nuevo = board.copy()
                nuevo[idx_zero], nuevo[new_idx] = nuevo[new_idx], nuevo[idx_zero]
                nodo_hijo = Nodo(nuevo)
                hijos[nodo_hijo] = 1  # coste uniforme 1 paso
        return hijos

    def get_costo(self, camino):
        # Cost is just the number of moves
        return len(camino) - 1

    def get_costo_estimado(self, camino):
        # A* cost: g(n) + h(n)
        estado_actual = camino[-1]
        return self.get_costo(camino) + self.get_heuristica_manhattan(estado_actual)

    def get_heuristica_manhattan(self, estado):
        board = np.array(estado)
        total = board.size
        N = int(np.sqrt(total))
        distancia = 0
        for i, valor in enumerate(board):
            if valor != 0:
                current_row = i // N
                current_col = i % N
                target_row = (valor - 1) // N
                target_col = (valor - 1) % N
                distancia += abs(current_row - target_row) + abs(current_col - target_col)
        return distancia

    def get_heuristica_fichas_mal_colocadas(self, estado):
        board = np.array(estado)
        meta = np.array(self.get_estado_meta())
        # Asumiendo que meta también es un array plano
        return int(np.sum((board != 0) & (board != meta)))