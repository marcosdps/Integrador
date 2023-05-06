from claseMateria import Materia
import csv

class ManejadorMateria:
    
    def cargoLista(self, listaMaterias):
        archiMaterias = open("materiasAprobadas.csv")
        reader = csv.reader(archiMaterias, delimiter=";")
        next(reader)
        for fila in reader:
            unaMateria = Materia()
            unaMateria.cargoMateria(fila)
            listaMaterias.append(unaMateria)
        for i in range(len(listaMaterias)):
            print(listaMaterias[i])

    def calculoProm(self, DNIaBuscar, listaMaterias):
        sumaSINaplazo = sumaCONaplazo = contadorConAplazo = contadorSinAplazo = 0
        bandera = False
        for i in range(len(listaMaterias)):
            if DNIaBuscar == listaMaterias[i].getDNI():
                bandera = True
                sumaCONaplazo += listaMaterias[i].getNota()
                contadorConAplazo += 1
                if listaMaterias[i].getNota() >= 4:
                    sumaSINaplazo += listaMaterias[i].getNota()
                    contadorSinAplazo += 1
        if bandera:
            print("El promedio con aplazos es de ",sumaCONaplazo/contadorConAplazo)
            print("El promedio sin aplazos es de ",sumaSINaplazo/contadorSinAplazo)
        else: print("Alumno no encontrado")
        
