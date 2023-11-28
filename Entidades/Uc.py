import Ir
import Pc
import Memoria
import Alu


class Uc:

    def __init__(self):
        self.pilaOperandos = []
        self.pilaOperandosAuxiliar = []
        self.registroInstrucciones = Ir()
        self.contadorPrograma = Pc()
        self.memoriaPrincipal = Memoria()
        self.alu = Alu()
        self.decodificador = ""
        self.operacionesPosibles = {'OUTPUT': "print",
                                    'COMPARE': "==",
                                    'CLEAR': "[]",
                                    'PUSH': "append",
                                    'POP': "pop",
                                    'INCREMENT': "+1",
                                    'DECREMENT': "-1",
                                    'AND': "and",
                                    'OR': "or",
                                    'NOT': "not",
                                    'ADD': '+',
                                    'SUB': '-',
                                    'DIV': '/',
                                    'MPY': '*'
                                    }
        self.diccionarioMovimiento = []
        self.auxiliarDireccion = ()

    # cargar lo q se mando a la memoria
    def cargarInstrucciones(self, lista):
        self.memoriaPrincipal.cargarInstruccionesDiccionario(lista)
        self.auxiliarDireccion = ("UC", "Memoria")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

    # contador arranca en cero y empieza la primera
    # busqueda de memoria
    def captacion(self):
        print("\n La pila es", self.pilaOperandos)
        # while(self.contadorPrograma.getNumeroInstr() < self.memoriaPrincipal.getLongitudPendientes()):
        self.memoriaPrincipal.cargarMar(self.contadorPrograma.getNumeroInstr())

        self.auxiliarDireccion = ("PC", "UC")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.auxiliarDireccion = ("UC", "MAR")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.contadorPrograma.aumentarNumeroInstruccion()

        self.auxiliarDireccion = ("PC", "PC")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.memoriaPrincipal.cargarRegistro()

        self.auxiliarDireccion = ("Memoria", "MBR")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.registroInstrucciones.setInstruccion(self.memoriaPrincipal.getMbr().getDato())

        self.auxiliarDireccion = ("MBR", "UC")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.auxiliarDireccion = ("UC", "IR")
        self.diccionarioMovimiento.append(self.auxiliarDireccion)

        self.decodificar()
        # print("Esta es la instruccion", self.decodificador)
        self.ejecutarInstruccion(self.decodificador)

        # print("Esta es la pila", self.pilaOperandos)

    def ejecucion(self):
        while (self.contadorPrograma.getNumeroInstr() < self.memoriaPrincipal.getLongitudPendientes()):
            self.captacion()
            self.alu.operar()
            self.comprobarPendientes()

    def comprobarPendientes(self):
        if (self.alu.getResultado() != None):
            self.auxiliarDireccion = ("UC", "ALU")
            self.diccionarioMovimiento.append(self.auxiliarDireccion)
            self.pilaOperandos.append(self.alu.getResultado())
            self.pilaOperandosAuxiliar.append(self.pilaOperandos)
            self.alu.setResultado()

    # Asigna la funcion a ejecutar
    def decodificar(self):
        nueva = self.registroInstrucciones.getInstruccion()
        print("Esta es la IR", self.registroInstrucciones.getInstruccion())
        auxiliar = nueva.split(' ')
        instruccion = auxiliar[0]
        print("Esta es la isntruccion al dividir", instruccion)
        self.comprobarFuncion(instruccion)

    # comprueba lka funcion solicitada si es posible o no
    def comprobarFuncion(self, funcion):
        if (funcion in self.operacionesPosibles):
            self.decodificador = funcion
        else:
            self.decodificador = None

    def ejecutarInstruccion(self, instruccion):
        dato = self.memoriaPrincipal.getMbr().getDato()
        match instruccion:
            case "PUSH":
                self.pilaOperandos.append(self.obtenerOperando(dato))
                self.pilaOperandosAuxiliar.append(self.pilaOperandos)
            case "OUTPUT":
                print(self.pilaOperandos.pop())
            case "COMPARE":
                self.enviarAlu('==')
            case "CLEAR":
                self.pilaOperandos = []
                self.pilaOperandosAuxiliar.append(self.pilaOperandos)
            case "POP":
                print(self.pilaOperandos.pop())
            case "INCREMENT":
                self.enviarAlu2("1", "+1")
            case "DECREMENT":
                self.enviarAlu2("1", "-1")
            case "AND":
                self.enviarAlu1("and")
            case "OR":
                self.enviarAlu1("or")
            case "NOT":
                self.enviarAlu1("-1", "*")
            case "ADD":
                self.enviarAlu1("+")
            case "SUB":
                self.enviarAlu1("-")
            case "DIV":
                self.enviarAlu1("/")
            case "MPY":
                self.enviarAlu1("*")

    def obtenerOperando(self, dato):
        aux = dato.split(' ')

        return aux[1]

    def enviarAlu1(self, operacion):
        self.alu.setOperando1(str(self.pilaOperandos.pop()))
        self.pilaOperandosAuxiliar.append(self.pilaOperandos)
        self.alu.setOperando2(str(self.pilaOperandos.pop()))
        self.pilaOperandosAuxiliar.append(self.pilaOperandos)
        self.alu.setOperacion(operacion)

    def enviarAlu2(self, operando2, operacion):
        self.alu.setOperando1(str(self.pilaOperandos.pop()))
        self.pilaOperandosAuxiliar.append(self.pilaOperandos)
        self.alu.setOperando2(str(operando2))
        self.alu.setOperacion(operacion)
