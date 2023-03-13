from Jugador1 import Jugador1
from jugador2 import Jugador2

class Juego(Jugador1, Jugador2):
    def __init__(self, numLucha):
        self.numLucha = numLucha
        pass

    print("INICIANDO JUEGO...\n")
    print("Nombres de los luchadores:")
    print("Luchador 1: " + Jugador1.luchador)
    print("Luchador 2: " + Jugador2.luchador) 
    print("\nPelea de " + Jugador1.luchador + " VS " + Jugador2.luchador)

    def lucha(self):
        print("Ingrese el luchador a empezar la pelea (1 o 2)".format(Jugador1.vidaLuchador1))
        Lucha = input() 
        print("")

        if Lucha == "1":
            print(Jugador1.luchador + " golpeo a " + Jugador2.luchador + " y le resto 30 de vida")
            nuevaVidaBackman = 100 - 30
            print("La nueva Vida de " + Jugador2.luchador + " es de {}".format(nuevaVidaBackman))
        if Lucha == "2":
            print(Jugador2.luchador + " golpeo a " + Jugador1.luchador + " y le resto 30 de vida")
            nuevaVidaFlash = 100 - 30
            print("La nueva Vida de " + Jugador1.luchador + " es de {}".format(nuevaVidaFlash))
        return "{}".format(self.numLucha)

juego = Juego("Seguir Lucha...")

#IMPRIMIR METODO
print(juego.lucha())

