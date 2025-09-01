from Tablero import Tablero
from AgentePuzzle import AgentePuzzle
from Nodo import Nodo
import numpy as np

TECNICAS = ["manhattan", "fichas_mal_colocadas"]

def generar_estado_meta(N: int):
    meta = np.arange(1, N * N)
    meta = np.append(meta, 0)
    return meta

def generar_tablero(N: int):
    np.random.seed(69420)
    tablero = np.arange(N * N)
    np.random.shuffle(tablero)
    return tablero

if __name__ == "__main__":
    # Parametos
    N = 4
    tecnica = TECNICAS[1]

    # Tablero
    tablero = Tablero(N)
    tablero.set_estado(generar_tablero(N))
    tablero.mostrar_tablero()

    agentito = AgentePuzzle()
    agentito.set_estado_inicial(Nodo(tablero.get_estado()))
    agentito.set_estado_meta(generar_estado_meta(N))
    agentito.set_tecnica(TECNICAS[1])
    
    tablero.insertar(agentito)
    tablero.run()
    print(f"Tecnica usada: {TECNICAS[1]}")