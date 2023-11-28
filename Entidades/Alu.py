import math


class Alu:

    def __init__(self):
        self.operando1 = []
        self.operando2 = []
        self.operacion = ""
        self.resultado = []

    def operar(self):
        if self.operando1 != [] and self.operando2 != []:
            if (self.validarOperandoDigito(self.operando1[0]) and
                    self.validarOperandoDigito(self.operando2[0])):

                match self.operacion:
                    case '==':
                        self.resultado.append(int(self.operando1[0]) == int(self.operando2[0]))
                    case "+1":
                        self.resultado.append(math.trunc(int(self.operando1[0]) + 1))
                    case "-1":
                        self.resultado.append(math.trunc(int(self.operando1[0]) + 1))
                    case "+":
                        self.resultado.append(math.trunc((int(self.operando1[0]) + int(self.operando2[0]))))
                    case "-":
                        self.resultado.append(math.trunc((int(self.operando1[0]) - int(self.operando2[0]))))
                    case "/":
                        self.resultado.append(math.trunc((int(self.operando1[0]) / int(self.operando2[0]))))
                    case "*":
                        self.resultado.append(math.trunc((int(self.operando1[0]) * int(self.operando2[0]))))
            else:
                match self.operacion:
                    case '==':
                        self.resultado.append(self.operando1[0] == self.operando2[0])
                    case "+":
                        self.resultado.append(self.operando1[0] + self.operando2[0])

    def validarOperandoDigito(self, operando):
        print(operando)
        return operando.isdigit()

    def setOperando1(self, numero):
        self.operando1.append(numero)

    def setOperando2(self, numero):
        self.operando2.append(numero)

    def setOperacion(self, operacion):
        self.operacion = operacion

    def getResultado(self):
        if (self.resultado != []):
            return self.resultado[0]
        else:
            return None

    def setResultado(self):
        self.resultado = []
        self.operando2 = []
        self.operando1 = []
        self.operacion = ""
