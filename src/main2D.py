import matplotlib.pyplot as plt
import numpy as np

alfa = 1
Npontos = 10
tTotal = 100
condInicial = 0
comprimento = 50 #cm

delta_X = comprimento / Npontos
delta_T = 1

temperatura2 = [0]

fourier = 0

#difusidadeTermica = 1 #cm2/s


def numeroFourier():
    return (alfa * delta_T) / pow(delta_X, 2)

def criar_matriz_T(n, s, l, o):
    temperatura = np.zeros((Npontos, Npontos)).tolist()

    for i in range(Npontos):
        temperatura[i][0] = o
        temperatura[i][Npontos-1] = l
        temperatura[Npontos-1][i] = s
        temperatura[0][i] = n

#    print(temperatura)
    return temperatura


def main():
    temperatura2 = criar_matriz_T(100, 0, 50, 75)
    temperatura = criar_matriz_T(100, 0, 50, 75)
    fourier = numeroFourier()
    print(fourier)
    if (fourier > 0.5):
        print("Sem solucao para o sistema")
        return
    for t in range(tTotal):
        for i in range(1, Npontos - 1):
            for j in range(1, Npontos - 1):
                temp = ( fourier * (temperatura[i + 1][j] + temperatura[i-1][j] + temperatura[i][j+1] + temperatura[i][j - 1]) + (1 - (4 * fourier) ) * temperatura[i][j])
                temperatura2[i][j]= (temp)
            
        temperatura = temperatura2[:][:]
            
    plt.imshow(temperatura)
    plt.show()

main()
