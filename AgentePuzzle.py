from AgenteIA.AgenteBuscador import AgenteBuscador
import copy

class AgentePuzzle(AgenteBuscador):
    def __init__(self):
        super().__init__()
        self.costos = [[]]
        self.distacias_manhattan = [[]]

    def generar_hijos(self, estado):
        N = len(estado)
        hijos = {}
        
        # Find zero position
        for i in range(N):
            for j in range(N):
                if estado[i][j] == 0:
                    x, y = i, j
                    break
        
        movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if isinstance(estado, tuple):
                    nuevo = [list(row) for row in estado]
                else:
                    nuevo = copy.deepcopy(estado)
                
                nuevo[x][y], nuevo[nx][ny] = nuevo[nx][ny], nuevo[x][y]
                hijos[tuple(map(tuple, nuevo))] = 1
        
        return hijos

    def get_costo(self, camino):
        # Cost is just the number of moves
        return len(camino) - 1

    def get_costo_estimado(self, camino):
        # A* cost: g(n) + h(n)
        estado_actual = camino[-1]
        return self.get_costo(camino) + self.get_heuristica_manhattan(estado_actual)

    def get_heuristica_manhattan(self, estado):
        N = len(estado)
        distancia = 0
        for i in range(N):
            for j in range(N):
                valor = estado[i][j]
                if valor != 0:
                    meta_i = (valor - 1) // N
                    meta_j = (valor - 1) % N
                    distancia += abs(i - meta_i) + abs(j - meta_j)
                # If valor == 0, its goal position is (N-1, N-1)
        return distancia
    
    def get_heuristica_fichas_mal_colocadas(self, estado):
        N = len(estado)
        fichas_mal_colocadas = 0
        for i in range(N):
            for j in range(N):
                valor_actual = estado[i][j]
                
                if valor_actual != 0 and valor_actual != self.get_estado_meta()[i][j]:
                    fichas_mal_colocadas += 1
        
        return fichas_mal_colocadas