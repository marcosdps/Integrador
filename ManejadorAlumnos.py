from claseAlumno import Alumno
import csv
import os

class ManejadorAlumno:

    def cargarAlumnos(self, tablaAlumnos):
        i=0
        archiAlu = open("alumnos.csv")
        reader = csv.reader(archiAlu, delimiter=";")
        next(reader)#Ignoro la primera linea que tiene los nombres de las columnas
        for lista in reader:
            unAlumno = Alumno()
            unAlumno.cargoAlumno(lista)
            #print(unAlumno)
            tablaAlumnos[i] = unAlumno
            i +=1
        for i in range(len(tablaAlumnos)):
            print(tablaAlumnos[i])
            

    def analizarCantMuestra(self):
        archiAlu = open("alumnos.csv")
        aLeer = archiAlu.readlines() #readlines devuelve una lista de todas las lineas del archivo
        cant = len(aLeer)
        archiAlu.close
        return cant-1 #El -1 es porque no quiero guardar el encabezado
    """Nota: por alguna razon, si abria el archivo, leia la cantidad
    de lineas del archivo en "analizarCantMuestra" y luego leia en 
    cargarAlumnos para llenar el objeto con lo datos, en la segunda vez
    que leia, no funcionaba, directamente no entraba en el bucle de
    for lista in reader, asique vi que el problema estaba en la lectura del archivo
    asique lo abri y cerré y problema solucionado, no se por que."""

    def listarPromocionales(self, listaMaterias, tablaAlumnos, nombreMateria):
        alumnosEncontrados = False
        for i in range(len(listaMaterias)):
            bandera = False
            if nombreMateria == listaMaterias[i].getNombre() and listaMaterias[i].getAprobacion() == "P":
                p = 0
                print("\n   DNI\t   Apellido y nombre\t   Fecha\tNota\tAño que cursa")
                while not bandera and p < len(tablaAlumnos):
                    if listaMaterias[i].getDNI() == tablaAlumnos[p].getDNI():
                        bandera = True
                        alumnosEncontrados = True
                        print(f"{tablaAlumnos[p].getDNI()}   {tablaAlumnos[p].getApeYNom()}\t{listaMaterias[i].getFecha()}\t  {listaMaterias[i].getNota()}\t    {tablaAlumnos[p].getAñoQueCursa()}")
                    p +=1
        if not alumnosEncontrados:
            print("Sin alumnos promocionales en la materia ingresada")

    def listadoOrdenado(self, tablaAlumnos):
        cota = len(tablaAlumnos)
        aux = Alumno()
        k = 1
        while k != -1:
            k = -1
            for i in range(cota-1):
                if tablaAlumnos[i] > tablaAlumnos[i+1]:
                    aux.intercambio(tablaAlumnos[i])
                    tablaAlumnos[i].intercambio(tablaAlumnos[i+1])
                    tablaAlumnos[i+1].intercambio(aux)
                    k = i
        cota = k

