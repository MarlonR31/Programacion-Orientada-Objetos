#1. Cree el siguiente ejercicio utilizando POO . En este ejercicio debe de simular el registro de 
#notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para 
#iniciar el ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
#El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un 
#estudiante de una materia en específico. El mensaje para mostrar queda a su discreción.
from Estudiantes import Estudiantes
from Estudiantes import estudiantes
from Materias import Materias

class Notas(Estudiantes):
    pass
    def __init__(self, notaLaboratorio_1, notaParcial_1):
        self.notaLaboratorio_1 = notaLaboratorio_1
        self.notaParcial_1 = notaParcial_1

    def notasComputo(self):
        return "\nEl alumno {} de la carrera {} \nObtuvo las siguientes Notas de la materia de {}. \nNota de Laboratorio: {} \nNota de Parcial: {} ".format(estudiantes.nombre,estudiantes.carrera,Materias.materia_1,self.notaLaboratorio_1,self.notaParcial_1 )

asignarNotas = Notas(8, 9)

#IMPRIMIMOS EL RESULTADO FINAL DEL EJERCICIO
print(asignarNotas.notasComputo())