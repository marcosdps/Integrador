

from typing import Any


class Materia:
    __dni: int
    __nombreMateria: str
    __fecha: str
    __nota: int
    __aprobacion: str


    def __init__(self, dni=None, nombreMateria=None, fecha=None, nota=None, aprobacion=None):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def cargoMateria(self, fila):
        self.__dni = int(fila[0])
        self.__nombreMateria = fila[1]
        self.__fecha = fila[2]
        self.__nota = int(fila[3])
        self.__aprobacion = fila[4]

    def __str__(self):
        return f"DNI: {self.__dni}, Nombre de la materia: {self.__nombreMateria}, fecha: {self.__fecha}, Nota: {self.__nota}, Aprobacion: {self.__aprobacion}"
    
    def getDNI(self):
        return self.__dni
    
    def getNota(self):
        return self.__nota
    
    def getAprobacion(self):
        return self.__aprobacion
    
    def getFecha(self):
        return self.__fecha
    
    def getNombre(self):
        return self.__nombreMateria
        