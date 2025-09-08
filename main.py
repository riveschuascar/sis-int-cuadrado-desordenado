from Tablero import Tablero
from AgentePuzzle import AgentePuzzle
import numpy as np

np.random.seed(69420)
TECNICAS = ["manhattan", "fichas_mal_colocadas"]

def aplanar_matriz(matrix):
    return [num for row in matrix for num in row if num != 0]

def count_inversions(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def encontrar_fila_cero_desde_abajo(matrix):
    N = len(matrix)
    for i in range(N-1, -1, -1):
        if 0 in matrix[i]:
            return N - i

def es_solvable(matrix):
    N = len(matrix)
    flat_list = aplanar_matriz(matrix)
    inversions = count_inversions(flat_list)
    
    if N % 2 == 1:
        return inversions % 2 == 0
    else:
        fila_cero = encontrar_fila_cero_desde_abajo(matrix)
        if fila_cero % 2 == 0:
            return inversions % 2 == 1
        else:
            return inversions % 2 == 0
        
def generar_estado_meta(N: int):
    meta = np.arange(1, N * N)
    meta = np.append(meta, 0)
    meta = meta.reshape(N, N).tolist()
    return tuple(map(tuple, meta))

def generar_tablero(N: int):
    numeros = np.arange(N * N)
    np.random.shuffle(numeros)
    tablero_desordenado = numeros.reshape(N, N).tolist()
    tablero_desordenado = tuple(map(tuple, tablero_desordenado))
    if not es_solvable(tablero_desordenado):
        print("Tablero no resolvible, generando otro...")
        return generar_tablero(N)
    print("Tablero resolvible generado.")
    return tablero_desordenado

if __name__ == "__main__":
    # Parametos
    N = 4
    tecnica = TECNICAS[0]
    print(f"Tecnica usada: {tecnica}")

    for i in range(10):
        # Tablero
        tablero = Tablero(N)
        tablero.set_estado(generar_tablero(N))
        tablero.mostrar_tablero()

        agentito = AgentePuzzle()
        agentito.set_estado_inicial(tablero.get_estado())
        agentito.set_estado_meta(generar_estado_meta(N))
        agentito.set_tecnica(tecnica)

        tablero.insertar(agentito)
        tablero.run()