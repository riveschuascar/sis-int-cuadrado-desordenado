# **********************************************************
# * Clase: Agente buscador                                 *
# * Autor: Victor Estevez                                  *
# * Version: v2023.03.29                                   *
# * Descripcion: Implementacion de algoritmos de busqueda  *
# *              sin informacion y con informacion         *
# **********************************************************

from AgenteIA.Agente import Agente
from copy import deepcopy
import time

class AgenteBuscador(Agente):
    def __init__(self):
        Agente.__init__(self)
        self.__estado_inicial = None
        self.__estado_meta = None
        self.__funcion_sucesor = []
        self.__tecnica = None

    def set_estado_inicial(self, e0):
        self.__estado_inicial = e0

    def set_estado_meta(self, ef):
        self.__estado_meta = ef

    def get_estado_inicial(self):
        return self.__estado_inicial

    def get_estado_meta(self):
        return self.__estado_meta

    def set_tecnica(self, t):
        self.__tecnica = t

    def add_funcion(self, f):
        self.__funcion_sucesor.append(f)

    def test_objetivo(self, e):
        return e == self.__estado_meta

    def generar_hijos(self, e):
        hijos = [fun(e) for fun in self.__funcion_sucesor]
        return hijos
    
    def get_costo(self, camino):
        raise Exception("Implementar")

    def mide_tiempo(funcion):
        def funcion_medida(*args, **kwards):
            inicio = time.time()
            c = funcion(*args, **kwards)
            t = time.time()-inicio
            print("Tiempo de ejecucion: ",t)
            return c
        return funcion_medida

    @mide_tiempo
    def programa(self):
        frontera = [[self.__estado_inicial]]
        visitados = []
        cont = 0

        while frontera:
            cont += 1
            if self.__tecnica == "profundidad":
                camino = frontera.pop()
            else:
                camino = frontera.pop(0)

            nodo = camino[-1]
            visitados.append(nodo)

            if self.test_objetivo(nodo):
                self.set_acciones(camino)
                self._medida_rendimiento["pasos"] = len(camino)
                self._medida_rendimiento["costo"] = self.get_costo(camino)
                self._medida_rendimiento["operaciones"] = cont
                break
            else:
                for hijo, costo in self.generar_hijos(nodo).items():
                    if hijo not in visitados:
                        aux = deepcopy(camino)
                        aux.append(hijo)
                        frontera.append(aux)

                # técnicas de búsqueda
                if self.__tecnica == "costouniforme":
                    frontera.sort(key=lambda tup: self.get_costo(tup))
                elif self.__tecnica == "astar":
                    frontera.sort(key=lambda tup: self.get_costo_estimado(tup))
                elif self.__tecnica == "heuristica":
                    frontera.sort(key=lambda tup: self.get_heuristica(tup))