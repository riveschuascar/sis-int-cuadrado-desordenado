import numpy as np
from AgenteIA.Entorno import Entorno

class Tablero(Entorno):
    def __init__(self, N):
        super().__init__()
        self.__estado = None
        self.N = N

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_percepciones(self, agente):
        pass

    def ejecutar(self, agente):
        agente.programa()
        for tupla in agente.get_acciones():
            for lista in tupla:
                print(f"{lista}", end="\n")
            print("->")
        for r in agente.get_medida_rendimiento().items():
            print(f"{r[0]}: {r[1]}")
        agente.inhabilitar()

    def mostrar_tablero(self):
        if self.__estado is None:
            print("El tablero está vacío.")
            return
        tablero = np.array(self.__estado)
        if tablero.ndim == 1:
            tablero = tablero.reshape((self.N, self.N))
        print(tablero)
