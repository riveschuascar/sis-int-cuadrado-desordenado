from AgenteIA.Entorno import Entorno

class Tablero(Entorno):
    def __init__(self, N):
        super().__init__()
        self.__estado = None

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado: list[list[int]]):
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
        for fila in self.__estado:
            print(" ".join(f"{elem:2d}" for elem in fila))
