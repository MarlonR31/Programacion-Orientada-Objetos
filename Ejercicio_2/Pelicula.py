from Categoria import Categoria
from Categoria import categoria

class Pelicula(Categoria):
    def __init__(self):
        pass

    def accion(self):
        return "\nLa pelicula {} pertenece a la categoria de ACCION".format(categoria.accion1)
    
    def comedia(self):
        return "la pelicula {} pertenece a la categoria de COMEDIA".format(categoria.comedia1)

pelicula = Pelicula()

print(pelicula.accion())