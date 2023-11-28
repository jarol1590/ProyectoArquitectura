class Pc:

    def __init__(self):
        self.numeroInstruccion = 0

    def aumentarNumeroInstruccion(self):
        self.numeroInstruccion = self.numeroInstruccion + 1

    def reiniciarNumeroInstruccion(self):
        self.numeroInstruccion = 0

    def getNumeroInstr(self):
        return self.numeroInstruccion
