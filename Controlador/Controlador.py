from Entidades.Uc import Uc

class Controlador:

    def __init__(self):
        self.uc = Uc()

    
    def reset(self):
        self.uc=None
        self.uc=Uc()

    def cargarIntruccionesVista(self, lista):
        print("Esta es la lista inicial: ", lista)
        self.uc.cargarInstrucciones(lista)
        # Aqui en ejecucion es donde apilo las instrucciones en la lista pilaOperandos
        self.uc.ejecucion()
        print(self.uc.alu.getResultado())

    def obtenerRecorrido(self):
        return self.uc.diccionarioMovimiento

    def resultado(self):
        return self.uc.pilaOperandos.pop()

    def obtenerPilas(self):
        return self.uc.pilaOperandosAuxiliar