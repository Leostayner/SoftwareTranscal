from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import numpy as np
import readTXT
from tkinter import messagebox

class Main_1D():

    def __init__(self, alfa, Npontos, tTotal, condInicial, comprimento,delta_T):
        self.alfa = alfa
        self.Npontos = Npontos
        self.tTotal = tTotal
        self.condInicial = condInicial
        self.comprimento = comprimento

        self.delta_X = self.comprimento / self.Npontos
        self.delta_T = delta_T

        self.temperaturaTemp = [0]
        self.posicao = self.criar_vetor_P()
        self.fourier = self.numeroFourier()

        self.main()

    def calcular(self):
        self.temperatura = self.criar_vetor_T()
        

        if (self.fourier > 0.5):
            messagebox.showerror("Error","Sistema Sem Solução")
            return 1

        for i in range(self.tTotal):
            
            for j in range(1, self.Npontos - 1):
                temp =( self.fourier * (self.temperatura[j + 1] + self.temperatura[j - 1]) + (1 - (2 * self.fourier) ) * self.temperatura[j])
                self.temperaturaTemp.append(temp)
            
            self.temperaturaTemp.append(0)
            self.temperatura  = self.temperaturaTemp[:]
            self.temperaturaTemp = [0]
            

    def criar_vetor_T(self):
        temperatura = []
        temperatura.append(0)
        for i in range(self.Npontos-2):
            temperatura.append(self.condInicial)
        temperatura.append(0)
        return temperatura

    def criar_vetor_P(self):
        posicao = []
        pos = self.comprimento/self.Npontos
        temp = pos
        for i in range(self.Npontos):
            posicao.append(pos)
            pos+=temp
        return posicao

    def numeroFourier(self):
        return (self.alfa * self.delta_T) / pow(self.delta_X, 2)


    def faixaTemperatura(self):
        self.temperaturaMin = 10000
        self.temperaturaMax = 0
        
        for i in(self.temperatura):
            if(i < self.temperaturaMin):
                self.min = i 
            
            if(i > self.temperaturaMax):
                self.max = i

    def myplot(self):        
        self.fig,self.ax = plt.subplots()
        
        plt.subplots_adjust(left=0.25, bottom=0.25)
        self.plotLabel, = plt.plot(self.posicao, self.temperatura, lw=2, color='red')
        plt.ylim((0,self.condInicial + 20))
        pos = plt.axes([0.25, 0.15, 0.65, 0.03])
        mySlider = Slider(pos, 'Tempo', 1, self.tTotal, valinit = self.tTotal, valstep = 1, valfmt='%1d')        
    
        mySlider.on_changed(self.update)
        plt.show()


    def update(self, value):
        intValue = int(value)
        self.tTotal = intValue  
        self.calcular()
        self.plotLabel.set_data(self.posicao,self.temperatura)
        self.fig.canvas.draw_idle()

    def main(self):
        if(self.calcular()):
            return
        self.myplot()
        
