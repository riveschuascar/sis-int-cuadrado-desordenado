from AgenteViajero import AgenteViajero
import json
from Pais import Pais

if __name__=="__main__":
    rumania = Pais()

    f = open('rumania.json')
    data = json.load(f)

    for c in data["rumania"].keys():
        rumania.add_ciudad(c)

    for c in data["rumania"].keys():
        for a in data["rumania"][c].keys():
            rumania.add_conexion(c, a, data["rumania"][c][a])
    f.close()

    pedrito = AgenteViajero()
    pedrito.set_estado_inicial("Arad")
    pedrito.set_estado_meta("Bucarest")
    pedrito.set_tecnica("profundidad")
    rumania.insertar(pedrito)
    rumania.run()
