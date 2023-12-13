from tkinter import *
from Controlador.Controlador import Controlador
import time

class main:
    def __init__(self):
        self.pausado = False
        self.app = Tk()
        self.app.title('Procesador')
        #self.app.state('zoomed')
        self.controlador = Controlador()
        self.alu = PhotoImage(file=r"C:\Users\Stokker\Desktop\ProyectoArquitectura\img\alu.png")

        self.frame = Frame(self.app)
        self.frame.pack(fill="both")
        self.frame.config(width=1360, height=760, bg='#0E3B65')

        self.mensaje = Text(self.frame, width=25, height=20,bg='#FAF1CA')
        self.mensaje.place(x=10, y=20)

        self.simbolos = {'INPUT': (1), #NO FUNCIONA
                         'OUTPUT': (2),
                         'COMPARE': (3),
                         'CLEAR': (4),
                         'SET': (5),    #NO FUNCIONA
                         'PUSH': (6),
                         'POP': (7),
                         'INCREMENT': (8),
                         'DECREMENT': (9),
                         'AND': (10),
                         'OR': (11),
                         'NOT': (12),
                         'ADD': (9),
                         'SUB': (10),
                         'DIV': (11),
                         'MPY': (12)
                         }
        self.listaSimbolosCadena = []
        self.recorrido = []
        self.contador = 0
        self.resultadoFinal = ''
        self.pilas = []
        self.button2 = Button(
            button2=Button(self.frame, text="Ejecutar", command=self.cargarTodo).place(x=100, y=400))
        self.buttonReset = Button(
            buttonReset=Button(self.frame, text="Resetear",command=self.resetear).place(x=100, y=450))

        self.button3 = Button(button2=Button(self.frame, text="Animar", command=self.contadorPintada).place(x=100, y=500))

        self.map = Canvas(self.frame, width=1360, height=760, bg='#0E3B65')
        self.map.place(x=250, y=0)



        # ALU
        self.map.create_image(60, 200, anchor=NW, image=self.alu)
        self.map.create_text(250, 530, fill="#FAF1CA",
                             font="Calibri 30", text="ALU")

        # MAR
        self.map.create_rectangle(30, 30, 180, 120, fill="#FAF1CA")
        self.map.create_text(100, 100, fill="black",
                             font="Calibri 30", text="MAR")

        # IR
        self.map.create_rectangle(350, 30, 500, 120, fill="#FAF1CA")
        self.map.create_text(425, 100, fill="black",
                             font="Calibri 30", text="IR")

        # MBR
        self.map.create_rectangle(330, 610, 480, 700, fill="#F4D35F")
        self.map.create_text(380, 680, fill="black",
                             font="Calibri 30", text="MBR")

        # PC
        self.map.create_rectangle(600, 200, 750, 300, fill="#F4D35F")
        self.map.create_text(670, 270, fill="black",
                             font="Calibri 30", text="PC")

        # UC
        self.map.create_rectangle(600, 350, 800, 600, fill="#FA5738")
        self.map.create_rectangle(620, 360, 780, 400, fill="#EE964C")
        self.map.create_text(700, 410, fill="black",font="Calibri 20", text="Instruccion")
        self.map.create_text(670, 550, fill="black",font="Calibri 30", text="UC")

        # Resultado
        self.map.create_rectangle(900, 10, 1100, 250, fill="#F4D35F")
        self.map.create_text(1000, 30, fill="black",font="Calibri 30", text="Resultado: ")

        # Memoria
        self.map.create_rectangle(850, 350, 1050, 700, fill="#F4D35F")
        self.map.create_text(970, 330, fill="black",font="Calibri 30", text="MEMORIA")
        self.map.create_text(950, 370, fill="black", font="Calibri 30", text="Dir    Cont")
        self.map.create_line(850, 400, 1050, 400, width=8, fill="black")
        self.map.create_line(935, 350, 935, 700, width=8, fill="black")

        # Datos que ingresan a la alu
        #self.map.create_rectangle(60, 190, 200, 250, fill="#FAF1CA")
        #self.map.create_rectangle(340, 190, 480, 250, fill="#FAF1CA")

        # Lineas Mbr - ALU
        # self.map.create_line(300, 490, 300, 660, width=8, fill="black")
        # self.map.create_line(300, 660, 180, 660, width=8, fill="black")

        # Lineas Mbr - memoria
        self.map.create_line(480, 690, 850, 690, width=8, fill="black")

        # Lineas uc - mar
        self.map.create_line(600, 420, 546, 420, width=8, fill="black")
        self.map.create_line(550, 420, 550, 146, width=8, fill="black")
        self.map.create_line(550, 150, 96, 150, width=8, fill="black")
        self.map.create_line(100, 150, 100, 120, width=8, fill="black")

        # Lineas uc - ir
        self.map.create_line(600, 380, 576, 380, width=8, fill="black")
        self.map.create_line(580, 380, 580, 96, width=8, fill="black")
        self.map.create_line(580, 100, 500, 100, width=8, fill="black")

        # Lineas uc - pc
        self.map.create_line(650, 300, 650, 350, width=8, fill="black")

        # Lineas pc a pc
      #  self.map.create_line(670, 200, 670, 170, width=8, fill="black")
      #  self.map.create_line(670, 170, 780, 170, width=8, fill="black")
      #  self.map.create_line(780, 170, 780, 250, width=8, fill="black")
      #  self.map.create_line(780, 250, 750, 250, width=8, fill="black")

        # lineas mar - memoria
        self.map.create_line(150, 30, 150, 6, width=8, fill="black")
        self.map.create_line(150, 10, 874, 10, width=8, fill="black")
        self.map.create_line(870, 10, 870, 350, width=8, fill="black")

        # Lineas Mbr - uc
        self.map.create_line(650, 600, 650, 675, width=8, fill="black")
        self.map.create_line(654, 675, 480, 675, width=8, fill="black")

        # Lineas UC - ALU
        self.map.create_line(350, 490, 350, 550, width=8, fill="black")
        self.map.create_line(346, 550, 600, 550, width=8, fill="black")

        # self.openFile()
        self.app.mainloop()

    # metodo para mostrar la cadena ingresada
    def mostrar(self):
        self.map.create_text(1000, 100, fill="black", font="Calibri 30", text=self.resultadoFinal)
        # listaRetorno = self.separar_Cadena(self.mensaje.get(1.0, "end-1c"))
        # self.mostrarDatosMemoria(listaRetorno)

    # Pintar datos en la memoria
    def mostrarDatosMemoria(self, listaRetorno):
        aux = 0
        aux2 = 0
        for e in listaRetorno:
            if str(e[0]) in str(self.simbolos.keys()):
                self.map.create_text(1000, 420 + aux, fill="black", font="Calibri 10", text=e[0])
                self.map.create_text(900, 420 + aux, fill="black", font="Calibri 10", text=aux2)
                aux += 15
                aux2 += 1
        return listaRetorno

    # Pintar Lineas Mbr - ALU
    def pintar_mbr_alu(self):

#----------------------------------
        self.map.create_line(300, 490, 300, 660, width=4, fill="gold")
        self.map.create_line(300, 660, 180, 660, width=4, fill="gold")

    # Pintar Lineas Mbr - memoria
    def pintar_mbr_memoria(self):
        self.map.create_line(480, 690, 850, 690, width=8, fill="#EE964C")


    # Pintar Lineas uc - mar
    def pintar_uc_mar(self):
        self.map.create_line(600, 420, 546, 420, width=8, fill="#EE964C")
        self.map.create_line(550, 420, 550, 146, width=8, fill="#EE964C")
        self.map.create_line(550, 150, 96, 150, width=8, fill="#EE964C")
        self.map.create_line(100, 150, 100, 120, width=8, fill="#EE964C")

    # Pintar Lineas uc - ir
    def pintar_uc_ir(self):
        self.map.create_line(600, 380, 576, 380, width=8, fill="#EE964C")
        self.map.create_line(580, 380, 580, 96, width=8, fill="#EE964C")
        self.map.create_line(580, 100, 500, 100, width=8, fill="#EE964C")

    # Pintar Lineas uc - pc
    def pintar_uc_pc(self):
        self.map.create_line(650, 300, 650, 350, width=4, fill="gold")

    # Pintar Lineas pc a pc
    def pintar_pc_pc(self):
        print("")
       # self.map.create_line(670, 200, 670, 170, width=4, fill="gold")
        #self.map.create_line(670, 170, 780, 170, width=4, fill="gold")
        #self.map.create_line(780, 170, 780, 250, width=4, fill="gold")
        #self.map.create_line(780, 250, 750, 250, width=4, fill="gold")

    # Pintar lineas mar - dir cont
    def pintar_mar_memoria(self):
        self.map.create_line(150, 30, 150, 6, width=8, fill="#EE964C")
        self.map.create_line(150, 10, 874, 10, width=8, fill="#EE964C")
        self.map.create_line(870, 10, 870, 350, width=8, fill="#EE964C")

    # Lineas Mbr - uc
    def píntar_mbr_uc(self):
        self.map.create_line(650, 600, 650, 675, width=8, fill="#EE964C")
        self.map.create_line(654, 675, 480, 675, width=8, fill="#EE964C")

    # Lineas UC - ALU
    def pintar_uc_alu(self):
        self.map.create_line(350, 490, 350, 550, width=8, fill="#EE964C")
        self.map.create_line(346, 550, 600, 550, width=8, fill="#EE964C")

    # Metodo para separar la cadena que ingresa
    def separar_Cadena(self, texto):
        listaCadena = texto.split('\n')
        for e in listaCadena:
            aux = e.split(' ')
            self.listaSimbolosCadena.append(aux)
        for f in self.listaSimbolosCadena:
            print("examino la lista de los simbolos")
            if str(f[0]) in str(self.simbolos.keys()):
                print("si estoy : ", f[0])
        print(" Estos son los simbolos cadena ", self.listaSimbolosCadena)
        print(" Esta es la cadena ", listaCadena)
        print(" Estos son los simbolos ", self.simbolos)

        return listaCadena

    def cargarTodo(self):
        i=0
        lista = []
        lista = self.separar_Cadena(self.mensaje.get(1.0, "end-1c"))
        print("Esta es la lista de cargarTodo", lista)
        self.mostrarDatosMemoria(self.listaSimbolosCadena)
        #para tratar de meter los datos en al interfaz

        datosmemoria = self.controlador.cargarIntruccionesVista(lista)
        print("Recorrido", self.controlador.obtenerRecorrido())
        self.recorrido = self.controlador.obtenerRecorrido()
        #self.pintarRecorrido()
        self.resultadoFinal = self.controlador.resultado()
        self.mostrar()
        self.pilas = self.controlador.obtenerPilas()
        self.pintarPila()


    def resetear(self):
        self.controlador.reset()
        self.app.destroy()
        main()

    def pintarRecorrido(self):

        for i in self.recorrido:
            if (i[0] == 'UC' and i[1] == 'Memoria'):
                self.pintar_uc_mar()
                self.pintar_mar_memoria()
            if (i[0] == 'PC' and i[1] == 'UC'):
                self.pintar_uc_pc()
            if (i[0] == 'UC' and i[1] == 'MAR'):
                self.pintar_uc_mar()
            if (i[0] == 'PC' and i[1] == 'PC'):
                self.pintar_pc_pc()
            if (i[0] == 'Memoria' and i[1] == 'MBR'):
                self.pintar_mbr_memoria()
            if (i[0] == 'MBR' and i[1] == 'UC'):
                self.píntar_mbr_uc()
            if (i[0] == 'UC' and i[1] == 'IR'):
                self.pintar_uc_ir()
            if (i[0] == 'UC' and i[1] == 'ALU'):
                self.pintar_uc_alu()
            

    def contadorPintada(self):
        self.pintarNegro()
        tupla = self.recorrido[self.contador]
        print("esta es la tupla", tupla)
        if (tupla[0] == 'UC' and tupla[1] == 'Memoria'):
            self.pintar_uc_mar()
            self.pintar_mar_memoria()
        if (tupla[0] == 'PC' and tupla[1] == 'UC'):
            self.pintar_uc_pc()
        if (tupla[0] == 'UC' and tupla[1] == 'MAR'):
            self.pintar_uc_mar()
        if (tupla[0] == 'PC' and tupla[1] == 'PC'):
            self.pintar_pc_pc()
        if (tupla[0] == 'Memoria' and tupla[1] == 'MBR'):
            self.pintar_mbr_memoria()
        if (tupla[0] == 'MBR' and tupla[1] == 'UC'):
            self.píntar_mbr_uc()
        if (tupla[0] == 'UC' and tupla[1] == 'IR'):
            self.pintar_uc_ir()
        if (tupla[0] == 'UC' and tupla[1] == 'ALU'):
            self.pintar_uc_alu()
        self.contador = self.contador + 1

    def pintarNegro(self):
        # Lineas Mbr - memoria
        self.map.create_line(480, 690, 850, 690, width=8, fill="black")


        # Lineas uc - mar
        self.map.create_line(600, 420, 546, 420, width=8, fill="black")
        self.map.create_line(550, 420, 550, 146, width=8, fill="black")
        self.map.create_line(550, 150, 96, 150, width=8, fill="black")
        self.map.create_line(100, 150, 100, 120, width=8, fill="black")

        # Lineas uc - ir
        self.map.create_line(600, 380, 576, 380, width=8, fill="black")
        self.map.create_line(580, 380, 580, 96, width=8, fill="black")
        self.map.create_line(580, 100, 500, 100, width=8, fill="black")

        # Lineas uc - pc
        self.map.create_line(650, 300, 650, 350, width=8, fill="black")


        # Lineas pc a pc
      #  self.map.create_line(670, 200, 670, 170, width=8, fill="black")
      #  self.map.create_line(670, 170, 780, 170, width=8, fill="black")
      #  self.map.create_line(780, 170, 780, 250, width=8, fill="black")
      #  self.map.create_line(780, 250, 750, 250, width=8, fill="black")

        # lineas mar - memoria
        self.map.create_line(150, 30, 150, 6, width=8, fill="black")
        self.map.create_line(150, 10, 874, 10, width=8, fill="black")
        self.map.create_line(870, 10, 870, 350, width=8, fill="black")

        # Lineas Mbr - uc
        self.map.create_line(650, 600, 650, 675, width=8, fill="black")
        self.map.create_line(654, 675, 480, 675, width=8, fill="black")

        # Lineas UC - ALU
        self.map.create_line(350, 490, 350, 550, width=8, fill="black")
        self.map.create_line(346, 550, 600, 550, width=8, fill="black")

    def pintarPila(self):
        print("La pila es", self.pilas)
        for i in self.pilas:
            for e in i:
                self.map.create_text(700, 470, fill="black", font="Calibri 30", text="pila")
                self.map.create_text(700, 490, fill="black", font="Calibri 10", text=e)


main()
