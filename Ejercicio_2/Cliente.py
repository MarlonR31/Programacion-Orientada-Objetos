from Categoria import Categoria
from Pelicula import Pelicula

class Cliente(Pelicula, Categoria):
    pass
    def __init__(self):
        pass
    
    #Indicamos al cliente que categoria quiere ver
    print("Por favor ingresa una categoria segun su numero:")
    print("Accion = 1\nComedia = 2 \nTerror = 3")
    numCategoria = input() #Guardamos su respuesta
    
    if numCategoria == 1:
        print("Usted eligio la categoria de ACCION")
    elif numCategoria == 2:
        print("")
    #Evaluamos la respuesta del cliente
    def imprimir(numCategoria):
        pass
        
        
           
streaming = Cliente()

print(streaming.imprimir())