import tkinter as tk
from tkinter import font
from tkinter import filedialog
import readTXT
import writeTXT
import main
import main2D

class Janela_Principal():
    
    def __init__(self):

        self.app_config = dict()

        self.app_config['width'] = 600
        self.app_config['height'] = 300
        
        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        window_width = self.app_config['width']
        window_height = self.app_config['height']

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(window_width, 
                                                  window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("TransCal")
        #self.window.resizable(False, False)
    
        #Geometria da pagina
        self.window.rowconfigure(0, minsize = window_height)
        self.window.columnconfigure(0, minsize = window_height)
        
        #Variaveis
        self.fileName       = ""
        self.tipo           = 0
        self.alfa           = 0.0
        self.Npontos        = 0
        self.tTotal         = 0
        self.condInicial    = 0.0
        self.comprimento    = 0
        self.deltaT         = 0.0
        self.tA1            = 0.0
        self.tA2            = 0.0
        self.tA3            = 0.0
        self.tA4            = 0.0
        self.tolerancia     = 0.0

        #Menu
        menubar = tk.Menu(self.window)
        
        filemenu = tk.Menu(menubar, tearoff = 0)
        editmenu = tk.Menu(menubar, tearoff=0)
        
        filemenu.add_command(label="New", command = self.newFile)
        filemenu.add_command(label="Open", command = self.openFile)
        filemenu.add_command(label="Save", command = self.saveFile)
        filemenu.add_command(label="Save As", command = self.saveAsFile)

        editmenu.add_command(label = "1D", command = self.mostrar_form1D)
        editmenu.add_command(label = "2D", command = self.mostrar_form2D)


        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.window.configure(menu = menubar)
    
        #Menu Principal
        self.menu_principal = Menu_Principal(self)
        
        #Iniciar menu
        self.menu_principal.mostrar()

    def newFile(self):
        self.menu_principal.mostrar()       

    def openFile(self):
        self.fileName = filedialog.askopenfilename(filetypes=(("text files", "*.txt"), ("all files", "*.*")))

        read = readTXT.ArquivoTXT(self.fileName)
        self.tipo           = read.tipo
        self.alfa           = read.alfa
        self.Npontos        = read.Npontos
        self.tTotal         = read.tTotal
        self.condInicial    = read.condInicial
        self.comprimento    = read.comprimento
        self.deltaT         = read.deltaT
        self.tA1            = read.tA1
        self.tA2            = read.tA2
        self.tA3            = read.tA3
        self.tA4            = read.tA4
        self.tolerancia     = read.tolerancia

        if(self.tipo == 1):
            self.mostrar_form1D()
            main.Main_1D(self.alfa, self.Npontos,
                        self.tTotal, self.condInicial,
                        self.comprimento,self.deltaT)
        
        elif(self.tipo == 2):
            self.mostrar_form2D()
           
            main2D.Main_2D(self.alfa, self.Npontos, 
                           self.tTotal, self.condInicial,
                           self.comprimento, self.deltaT,
                           self.tA1, self.tA2,
                           self.tA3, self.tA4,self.tolerancia)
   
    def saveFile(self):
        if (self.fileName == ""):
            self.saveAsFile()
        
        else:
            writeTXT.ArquivoTXT(self.tipo,self.alfa, self.Npontos, 
                            self.tTotal, self.condInicial,
                            self.comprimento, self.deltaT,
                            self.tA1, self.tA2,
                            self.tA3, self.tA4, self.fileName, self.tolerancia)
        
    def saveAsFile(self):
        self.fileName = filedialog.asksaveasfilename(defaultextension=".txt")
        writeTXT.ArquivoTXT(self.tipo,self.alfa, self.Npontos, 
                            self.tTotal, self.condInicial,
                            self.comprimento, self.deltaT,
                            self.tA1, self.tA2,
                            self.tA3, self.tA4,self.fileName, self.tolerancia)

    def mostrar_form1D(self):
        self.form1D_window = Form1D_window(self)
        
        self.tipo = 1
        self.form1D_window.mostrar()
        
    def mostrar_form2D(self):
        self.form2D_window = Form2D_window(self)
        
        self.tipo = 2
        self.form2D_window.mostrar()
        
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        
        
        self.janela_principal.alfa          = 0.0
        self.janela_principal.Npontos       = 0
        self.janela_principal.tTotal        = 0.0
        self.janela_principal.condInicial   = 0.0
        self.janela_principal.comprimento   = 0
        self.janela_principal.deltaT        = 0.0
        self.janela_principal.A1            = 0.0
        self.janela_principal.A2            = 0.0
        self.janela_principal.A3            = 0.0
        self.janela_principal.A4            = 0.0
        self.janela_principal.tolerancia    = 0.0

        
    def mostrar(self):
        self.window1.tkraise()

class Form1D_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window2 = tk.Frame(self.janela_principal.window)
        self.window2.grid(row = 0, column = 0, sticky = "nsew")
        #self.window2 = tk.Tk()
        
        self.window2.columnconfigure(0, minsize = (self.janela_principal.app_config['width'] / 2)  )
        self.window2.columnconfigure(1, minsize = (self.janela_principal.app_config['width'] / 7) )
        self.window2.columnconfigure(2, minsize = (self.janela_principal.app_config['width'] / 8) )
        self.window2.columnconfigure(3, minsize = (self.janela_principal.app_config['width'] / 4) )

        #Fonte
        self.font = font.Font(family='Courier New', size = 10)
        
        #Comprimento
        self.labelComprimento = tk.Label(self.window2)
        self.labelComprimento.configure(text = "Comprimento : ", font = self.font)
        self.labelComprimento.grid(row = 0, column = 1, sticky = "w")


        self.varComprimento = tk.IntVar()
        self.varComprimento.set( self.janela_principal.comprimento)
        self.entryComprimento = tk.Entry(self.window2, background = "white", textvariable = self.varComprimento)
        self.entryComprimento.grid(row = 0, column = 2)

        self.labelComprimentoSimbol = tk.Label(self.window2)
        self.labelComprimentoSimbol.configure(text = "cm", font = self.font)
        self.labelComprimentoSimbol.grid(row = 0, column = 3, sticky = "w")

        #CondiInicial
        self.labelCondInicial = tk.Label(self.window2)
        self.labelCondInicial.configure(text = "Condição Inicial : ", font = self.font)
        self.labelCondInicial.grid(row = 1, column = 1, sticky = "w")

        self.varCondInicial = tk.DoubleVar()
        self.varCondInicial.set( self.janela_principal.condInicial)
        self.entryCondInicial = tk.Entry(self.window2, background = "white", textvariable = self.varCondInicial)
        self.entryCondInicial.grid(row = 1, column = 2)

        
        self.labelCondInicialSimbol = tk.Label(self.window2)
        self.labelCondInicialSimbol.configure(text = "ºC", font = self.font)
        self.labelCondInicialSimbol.grid(row = 1, column = 3, sticky = "w")


        #Numero Pontos
        self.labelNpontos = tk.Label(self.window2)
        self.labelNpontos.configure(text = "Numero de pontos : ", font = self.font)
        self.labelNpontos.grid(row = 2, column = 1, sticky = "w")

        self.varNpontos = tk.IntVar()
        self.varNpontos.set( self.janela_principal.Npontos)
        self.entryNpontos = tk.Entry(self.window2, background = "white", textvariable = self.varNpontos)
        self.entryNpontos.grid(row = 2, column = 2)
        

        #Alfa
        self.labelAlfa = tk.Label(self.window2)
        self.labelAlfa.configure(text = "Difusidade Termica : ", font = self.font)
        self.labelAlfa.grid(row = 3, column = 1,sticky = "w" )

        self.varAlfa = tk.DoubleVar()
        self.varAlfa.set( self.janela_principal.alfa)
        self.entryAlfa = tk.Entry(self.window2, background = "white", textvariable = self.varAlfa)
        self.entryAlfa.grid(row = 3, column = 2)
        
        self.labelAlfaSimbol = tk.Label(self.window2)
        self.labelAlfaSimbol.configure(text = "cm²/s", font = self.font)
        self.labelAlfaSimbol.grid(row = 3, column = 3,sticky = "w" )


        #Tempo total
        self.labelTtotal = tk.Label(self.window2)
        self.labelTtotal.configure(text = "Tempo Total : ", font = self.font)
        self.labelTtotal.grid(row = 4, column = 1,sticky = "w")

        self.varTtotal = tk.IntVar()
        self.varTtotal.set( self.janela_principal.tTotal)
        self.entryTtotal = tk.Entry(self.window2, background = "white", textvariable = self.varTtotal)
        self.entryTtotal.grid(row = 4, column = 2)

        self.labelTtotalSimbol = tk.Label(self.window2)
        self.labelTtotalSimbol.configure(text = "s", font = self.font)
        self.labelTtotalSimbol.grid(row = 4, column = 3,sticky = "w")


        #Delta T
        self.labelDeltaT = tk.Label(self.window2)
        self.labelDeltaT.configure(text = "Intervalo de Tempo : ", font = self.font)
        self.labelDeltaT.grid(row = 5, column = 1,sticky = "w")

        self.varDeltaT = tk.DoubleVar()
        self.varDeltaT.set( self.janela_principal.deltaT)
        self.entryDeltaT = tk.Entry(self.window2, background = "white", textvariable = self.varDeltaT)
        self.entryDeltaT.grid(row = 5, column = 2)

        
        self.labelDeltaTSimbol = tk.Label(self.window2)
        self.labelDeltaTSimbol.configure(text = "s", font = self.font)
        self.labelDeltaTSimbol.grid(row = 5, column = 3,sticky = "w")


        self.buttonConfimar = tk.Button(self.window2)
        self.buttonConfimar.configure(text = "Confirmar",command = self.confirmar)
        self.buttonConfimar.grid(row = 6, column  = 1, columnspan = 2, sticky = "nsew")

    def confirmar(self):
        self.janela_principal.alfa          = self.varAlfa.get()
        self.janela_principal.Npontos       = self.varNpontos.get()
        self.janela_principal.tTotal        = self.varTtotal.get()
        self.janela_principal.condInicial   = self.varCondInicial.get()
        self.janela_principal.comprimento   = self.varComprimento.get()
        self.janela_principal.deltaT        = self.varDeltaT.get()

        main.Main_1D(self.janela_principal.alfa, self.janela_principal.Npontos, 
                     self.janela_principal.tTotal, self.janela_principal.condInicial,
                     self.janela_principal.comprimento,self.janela_principal.deltaT)



    def mostrar(self):
        self.window2.tkraise()



class Form2D_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window3 = tk.Frame(self.janela_principal.window)
        self.window3.grid(row = 0, column = 0, sticky = "nsew")
        
        
        self.window3.columnconfigure(0, minsize = (self.janela_principal.app_config['width'] / 2)  )
        self.window3.columnconfigure(1, minsize = (self.janela_principal.app_config['width'] / 8) + 20)
        self.window3.columnconfigure(2, minsize = (self.janela_principal.app_config['width'] / 8) )
        self.window3.columnconfigure(3, minsize = (self.janela_principal.app_config['width'] / 4) )
  
        #Fonte
        self.font = font.Font(family='Courier New ', size = 10)
        
        #Comprimento
        self.labelComprimento = tk.Label(self.window3)
        self.labelComprimento.configure(text = "Comprimento : ", font = self.font)
        self.labelComprimento.grid(row = 0, column = 1, sticky = "w")

        self.varComprimento = tk.IntVar()
        self.varComprimento.set( self.janela_principal.comprimento)
        self.entryComprimento = tk.Entry(self.window3, background = "white", textvariable = self.varComprimento)
        self.entryComprimento.grid(row = 0, column = 2)
        
        self.labelComprimentoSimbol = tk.Label(self.window3)
        self.labelComprimentoSimbol.configure(text = "cm", font = self.font)
        self.labelComprimentoSimbol.grid(row = 0, column = 3, sticky = "w")

      
        #Condiçao Inicial
        self.labelCondInicial = tk.Label(self.window3)
        self.labelCondInicial.configure(text = "Condição Inicial : ", font = self.font)
        self.labelCondInicial.grid(row = 1, column = 1, sticky = "w")

        self.varCondInicial = tk.DoubleVar()
        self.varCondInicial.set( self.janela_principal.condInicial)    
        self.entryCondInicial = tk.Entry(self.window3, background = "white", textvariable = self.varCondInicial)
        self.entryCondInicial.grid(row = 1, column = 2)

        self.labelCondInicialSimbol = tk.Label(self.window3)
        self.labelCondInicialSimbol.configure(text = "ºC")
        self.labelCondInicialSimbol.grid(row = 1, column = 3, sticky = "w")


        #Numero Pontos
        self.labelNpontos = tk.Label(self.window3)
        self.labelNpontos.configure(text = "Numero de pontos : ", font = self.font)
        self.labelNpontos.grid(row = 2, column = 1, sticky = "w")

        self.varNpontos = tk.IntVar()
        self.varNpontos.set( self.janela_principal.Npontos)
        self.entryNpontos = tk.Entry(self.window3, background = "white", textvariable = self.varNpontos)
        self.entryNpontos.grid(row = 2, column = 2)



        #Alfa
        self.labelAlfa = tk.Label(self.window3)
        self.labelAlfa.configure(text = "Difusidade Termica : ", font = self.font)
        self.labelAlfa.grid(row = 3, column = 1,sticky = "w" )

        self.varAlfa = tk.DoubleVar()
        self.varAlfa.set( self.janela_principal.alfa)
        self.entryAlfa = tk.Entry(self.window3, background = "white", textvariable = self.varAlfa)
        self.entryAlfa.grid(row = 3, column = 2)

        self.labelAlfaSimbol = tk.Label(self.window3)
        self.labelAlfaSimbol.configure(text = "cm²/s", font = self.font)
        self.labelAlfaSimbol.grid(row = 3, column = 3,sticky = "w" )

        #Tempo Total
        self.labelTtotal = tk.Label(self.window3)
        self.labelTtotal.configure(text = "Tempo Total : ", font = self.font)
        self.labelTtotal.grid(row = 4, column = 1,sticky = "w")

        self.varTtotal = tk.IntVar()
        self.varTtotal.set( self.janela_principal.tTotal)
        self.entryTtotal = tk.Entry(self.window3, background = "white", textvariable = self.varTtotal)
        self.entryTtotal.grid(row = 4, column = 2)

        self.labelTtotalSimbol = tk.Label(self.window3)
        self.labelTtotalSimbol.configure(text = "s", font = self.font)
        self.labelTtotalSimbol.grid(row = 4, column = 3,sticky = "w")



        self.labelDeltaT = tk.Label(self.window3)
        self.labelDeltaT.configure(text = "Intervalo de Tempo : ", font = self.font)
        self.labelDeltaT.grid(row = 5, column = 1,sticky = "w")

        self.varDeltaT = tk.DoubleVar()
        self.varDeltaT.set( self.janela_principal.deltaT)
        self.entryDeltaT = tk.Entry(self.window3, background = "white", textvariable = self.varDeltaT)
        self.entryDeltaT.grid(row = 5, column = 2)

        self.labelDeltaTSimbol = tk.Label(self.window3)
        self.labelDeltaTSimbol.configure(text = "s", font = self.font)
        self.labelDeltaTSimbol.grid(row = 5, column = 3,sticky = "w")

        #A1
        self.labelA1 = tk.Label(self.window3)
        self.labelA1.configure(text = "Temperatura Borda_N : ", font = self.font)
        self.labelA1.grid(row = 6, column = 1,sticky = "w")

        self.varA1 = tk.DoubleVar()
        self.varA1.set( self.janela_principal.tA1)
        self.entryA1 = tk.Entry(self.window3, background = "white", textvariable = self.varA1)
        self.entryA1.grid(row = 6, column = 2)

        self.labelA1Simbol = tk.Label(self.window3)
        self.labelA1Simbol.configure(text = "ºC", font = self.font)
        self.labelA1Simbol.grid(row = 6, column = 3,sticky = "w")

        #A2
        self.labelA2 = tk.Label(self.window3)
        self.labelA2.configure(text = "Temperatura Borda_S : ", font = self.font)
        self.labelA2.grid(row = 7, column = 1,sticky = "w")

        self.varA2 = tk.DoubleVar()
        self.varA2.set( self.janela_principal.tA2)
        self.entryA2 = tk.Entry(self.window3, background = "white", textvariable = self.varA2)
        self.entryA2.grid(row = 7, column = 2)

        self.labelA2Simbol = tk.Label(self.window3)
        self.labelA2Simbol.configure(text = "ºC", font = self.font)
        self.labelA2Simbol.grid(row = 7, column = 3,sticky = "w")

        #A3
        self.labelA3 = tk.Label(self.window3)
        self.labelA3.configure(text = "Temperatura Borda_L : ", font = self.font)
        self.labelA3.grid(row = 8, column = 1,sticky = "w")

        self.varA3 = tk.DoubleVar()
        self.varA3.set( self.janela_principal.tA3)
        self.entryA3 = tk.Entry(self.window3, background = "white", textvariable = self.varA3)
        self.entryA3.grid(row = 8, column = 2)

        self.labelA3Simbol = tk.Label(self.window3)
        self.labelA3Simbol.configure(text = "ºC", font = self.font)
        self.labelA3Simbol.grid(row = 8, column = 3,sticky = "w")

        #A4
        self.labelA4 = tk.Label(self.window3)
        self.labelA4.configure(text = "Temperatura Borda_W : ", font = self.font)
        self.labelA4.grid(row = 9, column = 1,sticky = "w")

        self.varA4 = tk.DoubleVar()
        self.varA4.set( self.janela_principal.tA4)
        self.entryA4 = tk.Entry(self.window3, background = "white", textvariable = self.varA4)
        self.entryA4.grid(row = 9, column = 2)

        self.labelA4Simbol = tk.Label(self.window3)
        self.labelA4Simbol.configure(text = "ºC", font = self.font)
        self.labelA4Simbol.grid(row = 9, column = 3,sticky = "w")

        #Tolerancia
        self.labelTolerancia = tk.Label(self.window3)
        self.labelTolerancia.configure(text = "Tolerancia : ", font = self.font)
        self.labelTolerancia.grid(row = 10, column = 1,sticky = "w")

        self.varTolerancia = tk.DoubleVar()
        self.varTolerancia.set( self.janela_principal.tolerancia)
        self.entryTolerancia = tk.Entry(self.window3, background = "white", textvariable = self.varTolerancia)
        self.entryTolerancia.grid(row = 10, column = 2)


        self.buttonConfimar = tk.Button(self.window3)
        self.buttonConfimar.configure(text = "Confirmar",command = self.confirmar)
        self.buttonConfimar.grid(row = 11, column  = 1, columnspan = 2, sticky = "nsew")



    def confirmar(self):
        self.janela_principal.alfa          = self.varAlfa.get()
        self.janela_principal.Npontos       = self.varNpontos.get()
        self.janela_principal.tTotal        = self.varTtotal.get()
        self.janela_principal.condInicial   = self.varCondInicial.get()
        self.janela_principal.comprimento   = self.varComprimento.get()
        self.janela_principal.deltaT        = self.varDeltaT.get()
        self.janela_principal.tA1           = self.varA1.get()
        self.janela_principal.tA2           = self.varA2.get()
        self.janela_principal.tA3           = self.varA3.get()
        self.janela_principal.tA4           = self.varA4.get()
        self.janela_principal.tolerancia    = self.varTolerancia.get()
    

        main2D.Main_2D(self.janela_principal.alfa, self.janela_principal.Npontos, 
                     self.janela_principal.tTotal, self.janela_principal.condInicial,
                     self.janela_principal.comprimento, self.janela_principal.deltaT,
                     self.janela_principal.tA1, self.janela_principal.tA2,
                     self.janela_principal.tA3, self.janela_principal.tA4,self.janela_principal.tolerancia)


    def mostrar(self):
        self.window3.tkraise()
      



app = Janela_Principal()
app.iniciar()