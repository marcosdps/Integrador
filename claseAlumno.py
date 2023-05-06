

class Alumno:
    __dni: int
    __apellido: str
    __nombre: str
    __carrera: str
    __añoCursa: int


    def __init__(self, dni=None, apellido=None, nombre=None, carrera=None, añoCursa=None):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__añoCursa = añoCursa

    def cargoAlumno(self,lista):
        self.__dni = int(lista[0])
        self.__apellido = lista[1]
        self.__nombre = lista[2]
        self.__carrera = lista[3]
        self.__añoCursa = int(lista[4])
    
    def muestroAlu(self):
        print(self.__apellido)
        print(self.__nombre)
        
    def __str__(self):
        return f"DNI: {self.__dni} //Apellido y nombre: {self.__apellido} {self.__nombre} //carrera: {self.__carrera} //Año que cursa: {self.__añoCursa}"
    
    def getDNI(self):
        return self.__dni
    
    def getApeYNom(self):
        return self.__apellido + " " +self.__nombre
    
    def getAñoQueCursa(self):
        return self.__añoCursa
    
    def __gt__(self, otro):
        if self.__añoCursa > otro.__añoCursa:
            return True
        elif self.__añoCursa == otro.__añoCursa:
            if self.__apellido > otro.__apellido:
                return True
            else: return False
        else: return False
        
        """elif self.__añoCursa == otro.__añoCursa:
            if self.__apellido < otro.__apellido:
                return True
            else: return False"""
    
    def intercambio(self, otro):
        self.__apellido = otro.__apellido
        self.__añoCursa = otro.__añoCursa
        self.__carrera = otro.__carrera 
        self.__dni = otro.__dni
        self.__nombre = otro.__nombre
