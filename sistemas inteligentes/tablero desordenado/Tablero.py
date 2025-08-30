from AgenteIA import Entorno

class Tablero(Entorno):
    def __init__(self, N):
        self.__tamano: int = N
        self.__tablero: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]

    def get_percepciones(self, agente):
        pass

    def ejecutar(self, agente):
        pass

    def mostrar_tablero(self):
        for fila in self.__tablero:
            print('|'.join(fila))
            print('-' * (2 * self.__columnas - 1))
