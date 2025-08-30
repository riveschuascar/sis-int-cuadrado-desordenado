from Tablero import Tablero
from AgentePuzzle import AgentePuzzle
import numpy as np

def llenar_tablero(tablero: Tablero, N: int):
    np.random.seed(69420)
    numbers = np.random.shuffle(np.arange(N * N))
    tablero.__tablero = numbers.reshape(N, N)

if __name__ == "__main__":
    N = 4
    tablero = Tablero(N)
    llenar_tablero(tablero, N)
    agentito = AgentePuzzle()
    agentito.__estado_inicial = tablero.__tablero
    agentito.__estado_meta = np.arange(N*N).reshape(N, N).tolist()
    tablero.add_agente(agentito)
    tablero.run()