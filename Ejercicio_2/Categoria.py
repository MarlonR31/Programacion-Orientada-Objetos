#2- Cree el siguiente ejercicio utilizando POO. Una plataforma de streaming publica contenido 
#como series , películas y documentales según sea la clasificación de su categoría. Podemos 
#tomar 3 categorías (Acción, Comedia y Terror) tomando en cuenta que esta seria la primera 
#clase, debemos de heredar a una clase películas la categoría a la que pueda estar ligada la 
#película mostrando un mensaje de referencia a su criterio. 
#La última clase ara referencia a las dos clases anteriores ya que esta será la Cliente donde 
#por una estructura de condición mostrará la película a ver. Ejemplo: si el usuario escoge 
#Acción imprimir las películas de acción a las que se hagan referencia. Puede trabajar solo 
#con 1 película para cada categoría.
class Categoria:
    def __init__(self, accion1, comedia1):
        self.accion1 = accion1
        self.comedia1 = comedia1
    
    def contenido(self):
        return "".format(self.accion1)
    
categoria = Categoria("La Roca (The Rock)", "Ser o no ser (1942)")
#print(categoria.contenido())
