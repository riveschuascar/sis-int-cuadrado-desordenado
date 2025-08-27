from AgenteIA.Entorno import Entorno
import pyttsx4

class Pais(Entorno):
    def __init__(self):
        Entorno.__init__(self)
        self.ciudades = {}
        self.distancias = {}
        self.lineal = {}
        self.voz = pyttsx4.init()
        self.voz.setProperty('rate', 150)
        self.voz.setProperty('voice', 'spanish')
        self.voz.setProperty('volume', 0.9)

    def add_ciudad(self, c):
        self.ciudades[c] = {}

    def add_conexion(self, origen, destino, costo):
        self.ciudades[origen][destino] = costo
        self.distancias[(origen, destino)] = costo
        self.ciudades[destino][origen] = costo
        self.distancias[(destino, origen)] = costo

    def get_percepciones(self, agente):
        agente.set_percepciones(self.ciudades)
        agente.distancias = self.distancias
        agente.lineal = self.lineal
        agente.programa()

    def ejecutar(self, agente):
        self.voz.say("Iniciamos el viaje")
        self.voz.runAndWait()
        self.voz.say("Te encuentras en " + agente.get_acciones()[0])
        for a in agente.get_acciones()[1:]:
            print(a, " - ")
            self.voz.say("Dirígete a " + a)
        self.voz.say("llegaste a tu destino")
        self.voz.say("distancia total " + str(agente.get_medida_rendimiento()["costo"])+" kilómetros")
        self.voz.say("numero de pasos " + str(agente.get_medida_rendimiento()["pasos"]))
        self.voz.say("numero de operaciones " + str(agente.get_medida_rendimiento()["operaciones"]))
        self.voz.runAndWait()
        agente.inhabilitar()
        