import matplotlib.pyplot as plt
import numpy as np

alfa = 1
Npontos = 10
tTotal = 100

comprimento = 50 #cm

delta_X = comprimento / Npontos
delta_T = 1

temperatura2 = [0]
temperatura = [0,20,20,20,20,20,20,20,20,0]
posicao = [5,10,15,20,25,30,35,40,45,50]

fourier = 0

difusidadeTermica = 1 #cm2/s


def numeroFourier():
    return (alfa * delta_T) / pow(delta_X, 2)

def main():
    temperatura2 = [0]
    temperatura = [0,20,20,20,20,20,20,20,20,0]
    fourier = numeroFourier()
    for i in range(tTotal):
        
        for j in range(1, Npontos - 1):
            temp =( fourier * (temperatura[j + 1] + temperatura[j - 1]) + (1 - (2 * fourier) ) * temperatura[j])
            temperatura2.append(temp)
        temperatura2.append(0)
        temperatura = temperatura2[:]
        temperatura2=[0]
    plt.plot(posicao, temperatura)
    plt.xlabel("Posição")
    plt.ylabel("Temperatura")
    plt.title("{} segundos".format(i) )
    plt.show()

main()
