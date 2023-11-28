import Mar
import Mbr


class Memoria:

    def __init__(self):
        self.DirCont = {}
        self.mar = Mar()
        self.mbr = Mbr()

    def buscarDireccion(self):
        cont = 0
        for i in self.DirCont:
            if cont > len(self.DirCont):
                print("El dato buscado no existe")
                break
            elif cont == Mar.Mar.getDireccion(self):
                return i
            else:
                cont += 1

    # Carga el dato(Str) en la Mbr el dato se encuentra en la direccion proporcionada
    def cargarMBR(self, key):
        dato = self.DirCont[int(key)]
        self.mbr.setDato(dato)

    # carga la mar con la posicion a buscar
    def cargarMar(self, posicion):
        self.mar.setDireccion(posicion)
        print("Esta es la Mar", self.mar.getDireccion())

    # Carga las instruciones solicitadas a la memoria principal
    def cargarInstruccionesDiccionario(self, lista):
        longitudLista = len(lista)
        cont = 0
        print(longitudLista)
        for i in lista:
            self.DirCont[cont] = i
            cont = cont + 1
            longitudLista = longitudLista - 1
        print("Este es el diccionario de memoria", self.DirCont)

    # Envia el resgistro de instruccion completo para ser decodificado por la UC
    def cargarRegistro(self):
        direccion = self.buscarDireccion()
        self.cargarMBR(direccion)
        print("Esta es la MBR: ", self.mbr.getDato())

    def getMbr(self):
        return self.mbr

    def getMar(self):
        return self.mar

    def getLongitudPendientes(self):
        return len(self.DirCont)
