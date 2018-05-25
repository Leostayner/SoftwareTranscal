import matplotlib.pyplot as plt
import numpy as np

alfa = 1

comprimento = 50 
nPontos = 10
delta_X = comprimento / nPontos

tTotal = 30
delta_T = 1

temperatura2 = np.zeros[nPontos]
temperatura = [0,20,20,20,20,20,20,20,20,0]
posicao = [5,10,15,20,25,30,35,40,45,50]

def numeroFourier():
    return (alfa * delta_T) / pow(delta_X, 2)

def main():
    fourier = numeroFourier()
    for i in range(tTotal):
        
        for j in range(1, nPontos - 1):
            temperatura2[i] =( fourier * (temperatura[j + 1] + temperatura[j - 1]) + (1 - (2 * fourier) ) * temperatura[j])    
    
        temperatura = temperatura2[:]
        temperatura2 = np.zeros[nPontos]
    
    plt.plot(posicao, temperatura)
    plt.xlabel("Posição")
    plt.ylabel("Temperatura")
    plt.title("{} segundos".format(i) )
    plt.show()

main()
