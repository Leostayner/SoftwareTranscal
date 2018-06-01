import tkinter as tk
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
        self.window.resizable(False, False)
    
        #Geometria da pagina
        self.window.rowconfigure(0, minsize = window_height)
        self.window.columnconfigure(0, minsize = window_height)
        
        #Variaveis
        self.alfa           = 0
        self.Npontos        = 0
        self.tTotal         = 0
        self.condInicial    = 0
        self.comprimento    = 0
        self.deltaT         = 0
        self.A1             = 0
        self.A2             = 0
        self.A3             = 0
        self.A4             = 0

        #Menu
        menubar = tk.Menu(self.window)
        
        filemenu = tk.Menu(menubar, tearoff = 0)
        editmenu = tk.Menu(menubar, tearoff=0)
        
        filemenu.add_command(label="New")
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
    
        #Form1D
        self.form1D_window = Form1D_window(self)
        
        #Form2D
        self.form2D_window = Form2D_window(self)
        
        #Iniciar menu
        self.menu_principal.mostrar()

       

    def openFile(self):
        fileName = filedialog.askopenfilename()

        read = readTXT.ArquivoTXT(fileName)
        self.alfa = read.alfa
        self.Npontos = read.Npontos
        self.tTotal = read.tTotal
        self.condInicial = read.condInicial
        self.comprimento = read.comprimento
        self.deltaT
        
        main.Main_1D(self.alfa, self.Npontos, self.tTotal, self.condInicial, self.comprimento,self.janela_principal.deltaT)

    def saveFile(self):
        print("save")
    
    def saveAsFile(self):
        fileName = filedialog.asksaveasfilename()
        writeTXT.ArquivoTXT(self.alfa, self.Npontos, self.tTotal, self.condInicial, self.comprimento, fileName)


    def mostrar_form1D(self):
        self.form1D_window.mostrar()
        
    def mostrar_form2D(self):
        self.form2D_window.mostrar()
        
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        

        

    def mostrar(self):
        self.window1.tkraise()

class Form1D_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window2 = tk.Frame(self.janela_principal.window)
        self.window2.grid(row = 0, column = 0, sticky = "nsew")
        
        
        self.window2.columnconfigure(0, minsize = (self.janela_principal.app_config['width'] / 2) )
        self.window2.columnconfigure(1, minsize = (self.janela_principal.app_config['width'] / 4) )
        self.window2.columnconfigure(2, minsize = (self.janela_principal.app_config['width'] / 4) )
        
        '''
        self.window2.rowconfigure(0, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(1, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(2, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(3, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(4, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(5, minsize = (self.janela_principal.app_config['height'] /7  ) )
        self.window2.rowconfigure(6, minsize = (self.janela_principal.app_config['height'] /7  ) )
        '''
        

        self.labelComprimento = tk.Label(self.window2)
        self.labelComprimento.configure(text = "Comprimento:")
        self.labelComprimento.grid(row = 0, column = 1, sticky = "w")


        self.varComprimento = tk.IntVar()
        self.entryComprimento = tk.Entry(self.window2, background = "white", textvariable = self.varComprimento)
        self.entryComprimento.grid(row = 0, column = 2)


        self.labelCondInicial = tk.Label(self.window2)
        self.labelCondInicial.configure(text = "CondInicial:")
        self.labelCondInicial.grid(row = 1, column = 1, sticky = "w")

        self.varCondInicial = tk.IntVar()
        self.entryCondInicial = tk.Entry(self.window2, background = "white", textvariable = self.varCondInicial)
        self.entryCondInicial.grid(row = 1, column = 2)


        self.labelNpontos = tk.Label(self.window2)
        self.labelNpontos.configure(text = "N pontos:")
        self.labelNpontos.grid(row = 2, column = 1, sticky = "w")

        self.varNpontos = tk.IntVar()
        self.entryNpontos = tk.Entry(self.window2, background = "white", textvariable = self.varNpontos)
        self.entryNpontos.grid(row = 2, column = 2)




        self.labelAlfa = tk.Label(self.window2)
        self.labelAlfa.configure(text = "Alfa:")
        self.labelAlfa.grid(row = 3, column = 1,sticky = "w" )

        self.varAlfa = tk.IntVar()
        self.entryAlfa = tk.Entry(self.window2, background = "white", textvariable = self.varAlfa)
        self.entryAlfa.grid(row = 3, column = 2)


        self.labelTtotal = tk.Label(self.window2)
        self.labelTtotal.configure(text = "T Total:")
        self.labelTtotal.grid(row = 4, column = 1,sticky = "w")

        self.varTtotal = tk.IntVar()
        self.entryTtotal = tk.Entry(self.window2, background = "white", textvariable = self.varTtotal)
        self.entryTtotal.grid(row = 4, column = 2)



        self.labelDeltaT = tk.Label(self.window2)
        self.labelDeltaT.configure(text = "Delta T:")
        self.labelDeltaT.grid(row = 5, column = 1,sticky = "w")

        self.varDeltaT = tk.IntVar()
        self.entryDeltaT = tk.Entry(self.window2, background = "white", textvariable = self.varDeltaT)
        self.entryDeltaT.grid(row = 5, column = 2)

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
        
        
        self.window3.columnconfigure(0, minsize = (self.janela_principal.app_config['width'] / 2) )
        self.window3.columnconfigure(1, minsize = (self.janela_principal.app_config['width'] / 4) )
        self.window3.columnconfigure(2, minsize = (self.janela_principal.app_config['width'] / 4) )
        

        self.labelComprimento = tk.Label(self.window3)
        self.labelComprimento.configure(text = "Comprimento:")
        self.labelComprimento.grid(row = 0, column = 1, sticky = "w")


        self.varComprimento = tk.IntVar()
        self.entryComprimento = tk.Entry(self.window3, background = "white", textvariable = self.varComprimento)
        self.entryComprimento.grid(row = 0, column = 2)


        self.labelCondInicial = tk.Label(self.window3)
        self.labelCondInicial.configure(text = "CondInicial:")
        self.labelCondInicial.grid(row = 1, column = 1, sticky = "w")

        self.varCondInicial = tk.IntVar()
        self.entryCondInicial = tk.Entry(self.window3, background = "white", textvariable = self.varCondInicial)
        self.entryCondInicial.grid(row = 1, column = 2)


        self.labelNpontos = tk.Label(self.window3)
        self.labelNpontos.configure(text = "N pontos:")
        self.labelNpontos.grid(row = 2, column = 1, sticky = "w")

        self.varNpontos = tk.IntVar()
        self.entryNpontos = tk.Entry(self.window3, background = "white", textvariable = self.varNpontos)
        self.entryNpontos.grid(row = 2, column = 2)




        self.labelAlfa = tk.Label(self.window3)
        self.labelAlfa.configure(text = "Alfa:")
        self.labelAlfa.grid(row = 3, column = 1,sticky = "w" )

        self.varAlfa = tk.IntVar()
        self.entryAlfa = tk.Entry(self.window3, background = "white", textvariable = self.varAlfa)
        self.entryAlfa.grid(row = 3, column = 2)


        self.labelTtotal = tk.Label(self.window3)
        self.labelTtotal.configure(text = "T Total:")
        self.labelTtotal.grid(row = 4, column = 1,sticky = "w")

        self.varTtotal = tk.IntVar()
        self.entryTtotal = tk.Entry(self.window3, background = "white", textvariable = self.varTtotal)
        self.entryTtotal.grid(row = 4, column = 2)


        self.labelDeltaT = tk.Label(self.window3)
        self.labelDeltaT.configure(text = "Delta T:")
        self.labelDeltaT.grid(row = 5, column = 1,sticky = "w")

        self.varDeltaT = tk.IntVar()
        self.entryDeltaT = tk.Entry(self.window3, background = "white", textvariable = self.varDeltaT)
        self.entryDeltaT.grid(row = 5, column = 2)



        self.labelA1 = tk.Label(self.window3)
        self.labelA1.configure(text = "T A1:")
        self.labelA1.grid(row = 6, column = 1,sticky = "w")

        self.varA1 = tk.IntVar()
        self.entryA1 = tk.Entry(self.window3, background = "white", textvariable = self.varA1)
        self.entryA1.grid(row = 6, column = 2)

        self.labelA2 = tk.Label(self.window3)
        self.labelA2.configure(text = "T A2:")
        self.labelA2.grid(row = 7, column = 1,sticky = "w")

        self.varA2 = tk.IntVar()
        self.entryA2 = tk.Entry(self.window3, background = "white", textvariable = self.varA2)
        self.entryA2.grid(row = 7, column = 2)

        self.labelA3 = tk.Label(self.window3)
        self.labelA3.configure(text = "T A3:")
        self.labelA3.grid(row = 8, column = 1,sticky = "w")

        self.varA3 = tk.IntVar()
        self.entryA3 = tk.Entry(self.window3, background = "white", textvariable = self.varA3)
        self.entryA3.grid(row = 8, column = 2)

        self.labelA4 = tk.Label(self.window3)
        self.labelA4.configure(text = "T A4:")
        self.labelA4.grid(row = 9, column = 1,sticky = "w")

        self.varA4 = tk.IntVar()
        self.entryA4 = tk.Entry(self.window3, background = "white", textvariable = self.varA4)
        self.entryA4.grid(row = 9, column = 2)


        self.buttonConfimar = tk.Button(self.window3)
        self.buttonConfimar.configure(text = "Confirmar",command = self.confirmar)
        self.buttonConfimar.grid(row = 10, column  = 1, columnspan = 2, sticky = "nsew")



    def confirmar(self):
        self.janela_principal.alfa          = self.varAlfa.get()
        self.janela_principal.Npontos       = self.varNpontos.get()
        self.janela_principal.tTotal        = self.varTtotal.get()
        self.janela_principal.condInicial   = self.varCondInicial.get()
        self.janela_principal.comprimento   = self.varComprimento.get()
        self.janela_principal.deltaT        = self.varDeltaT.get()
        self.janela_principal.A1            = self.varA1.get()
        self.janela_principal.A2            = self.varA2.get()
        self.janela_principal.A3            = self.varA3.get()
        self.janela_principal.A4            = self.varA4.get()




        main.Main_2D(self.janela_principal.alfa, self.janela_principal.Npontos, 
                     self.janela_principal.tTotal, self.janela_principal.condInicial,
                     self.janela_principal.comprimento,self.janela_principal.deltaT)


    def mostrar(self):
        self.window3.tkraise()
      



app = Janela_Principal()
app.iniciar()