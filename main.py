from ManejadorAlumnos import ManejadorAlumno
from claseAlumno import Alumno
from claseMateria import Materia
from ManejadorMateria import ManejadorMateria
import numpy as np
import os

if __name__ == "__main__":
    manejadorAlu = ManejadorAlumno()
    tablaAlumnos = np.empty(manejadorAlu.analizarCantMuestra(), dtype=Alumno)
    manejadorAlu.cargarAlumnos(tablaAlumnos)
    print("-----DATOS DE ALUMNOS CARGADOS------")
    listaMaterias = []
    manejadorMat = ManejadorMateria()
    manejadorMat.cargoLista(listaMaterias)
    print("-----DATOS DE MATERIAS CARGADOS------")

    print("""\n---------MENU DE OPCIONES---------
    -1- Mostrar promedio de alumno
    -2- Listado de alumnos promocionales
    -3- Listado de alumnos que cursan
    -0- SALIR""")
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                print("----LISTA DE ALUMNOS----")
                for i in range(len(listaMaterias)):
                    print(listaMaterias[i])
                DNIaBuscar = int(input("Ingrese el DNI del alumno: "))
                os.system("cls")
                manejadorMat.calculoProm(DNIaBuscar, listaMaterias)
            case 2:
                nombreMateria = input("Ingrese el nombre de la materia: ")
                manejadorAlu.listarPromocionales(listaMaterias, tablaAlumnos, nombreMateria)
            case 3:
                manejadorAlu.listadoOrdenado(tablaAlumnos)
                print("LISTA ORDENADA")
                for i in range(len(tablaAlumnos)):
                    print(tablaAlumnos[i])
        print("""\n---------MENU DE OPCIONES---------
    -1- Mostrar promedio de alumno
    -2- Listado de alumnos promocionales
    -3- Listado de alumnos que cursan
    -0- SALIR""")
        opcion = int(input("Ingrese una opcion: "))