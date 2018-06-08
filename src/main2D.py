import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import tkinter as tk
from tkinter import messagebox

class Main_2D():

    def __init__(self, alfa, Npontos, tTotal, condInicial, comprimento, deltaT, A1, A2, A3, A4, tolerancia):
        self.alfa = alfa
        self.Npontos = Npontos
        self. tTotal = tTotal
        self.condInicial = condInicial
        self.comprimento = comprimento

        self.delta_X = self.comprimento / self.Npontos
        self.delta_T = deltaT

        self.temperatura2 = [0]
        #alfa = condutividade termica/(calor especifico * massa especifica)
        self.fourier = 0

        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.intValue = 0
    
        self.tolerancia = tolerancia

        self.temperatura2 = self.criar_matriz_T(self.A1, self.A2, self.A3, self.A4)
        self.temperatura = self.criar_matriz_T(self.A1, self.A2, self.A3, self.A4)
        self.fourier = self.numeroFourier()

        self.main()


    def numeroFourier(self):
        return (self.alfa * self.delta_T) / pow(self.delta_X, 2)

    def criar_matriz_T(self, n, s, l, o):
        temperatura = np.zeros((self.Npontos, self.Npontos)).tolist()

        for i in range(self.Npontos):
            temperatura[i][0] = o
            temperatura[i][self.Npontos-1] = l
            temperatura[self.Npontos-1][i] = s
            temperatura[0][i] = n

        return temperatura

    def calcular(self):
        self.temperatura = self.criar_matriz_T(self.A1, self.A2, self.A3, self.A4)
        max = 0

        # Verifica Se há solução para o sistema
        if (self.fourier > 0.5):
            messagebox.showerror("Error","Sistema Sem Solução")
            return 1

        for t in range(self.tTotal):
            for i in range(0, self.Npontos - 1):
                for j in range(0, self.Npontos - 1):

                    #Condição de Borda
                    if j==0 and i!=0 and (i!=(self.Npontos - 1)):
                        temp = ( self.fourier * (self.temperatura[i + 1][j] + self.temperatura[i-1][j] + self.temperatura[i][j+1]) + (1 - (4 * self.fourier) ) * self.temperatura[i][j])
                        self.temperatura2[i][j]= (temp)
                    
                    if i!=0 and j!=0:
                        temp = ( self.fourier * (self.temperatura[i + 1][j] + self.temperatura[i-1][j] + self.temperatura[i][j+1] + self.temperatura[i][j - 1]) + (1 - (4 * self.fourier) ) * self.temperatura[i][j])
                        self.temperatura2[i][j]= (temp)

                    #Verificação da Tolerancia

                    if(self.temperatura2[i][j] == 0):
                        erro = 0
                    
                    else:
                        erro = (self.temperatura2[i][j] - self.temperatura[i][j]) / self.temperatura2[i][j]
                          
                    if(erro > max):
                        max = erro


                        
            self.temperatura = self.temperatura2[:][:]
            self.temperatura2 = self.criar_matriz_T(self.A1, self.A2, self.A3, self.A4)
            if( (max < self.tolerancia) and (max != 0) ):
                if(self.intValue == 0):
                    messagebox.showwarning("Warning","Sistema Convergiu")
                break
    def myplot(self):
        self.fig, self.ax = plt.subplots()

        plt.subplots_adjust(left=0.25, bottom=0.25)
        self.plotLabel = plt.imshow(self.temperatura)

        pos = plt.axes([0.25, 0.15, 0.65, 0.03])
        mySlider = Slider(pos, 'Tempo', 1, self.tTotal, valinit = self.tTotal, valstep = 1, valfmt='%1d')

        mySlider.on_changed(self.update)
        plt.show()


    def update(self, value):
        self.intValue = int(value)
        self.tTotal = self.intValue
        self.calcular()
        self.plotLabel.set_data(self.temperatura)

        self.fig.canvas.draw_idle()

    def main(self):
        if(self.calcular()):
            return
        self.myplot()
