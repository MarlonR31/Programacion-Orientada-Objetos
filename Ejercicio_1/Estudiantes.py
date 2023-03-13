#1. Cree el siguiente ejercicio utilizando POO . En este ejercicio debe de simular el registro de 
#notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para 
#iniciar el ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
#El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un 
#estudiante de una materia en específico. El mensaje para mostrar queda a su discreción.

class Estudiantes:
    def __init__(self, nombre, carrera):
        self.nombre =  nombre
        self.carrera = carrera

    def infoAlumno(self):
        return "{}".format(self.nombre)

estudiantes = Estudiantes("Marlon Ramos", "Ing. en Desarrollo de Software")
