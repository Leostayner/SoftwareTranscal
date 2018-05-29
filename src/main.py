import matplotlib.pyplot as plt
import numpy as np

alfa = 1
Npontos = 35
tTotal = 100
condInicial = 20
comprimento = 50 #cm

delta_X = comprimento / Npontos
delta_T = 1

temperatura2 = [0]


fourier = 0

#difusidadeTermica = 1 #cm2/s


def numeroFourier():
    return (alfa * delta_T) / pow(delta_X, 2)

def criar_vetor_T():
    temperatura = []
    temperatura.append(0)
    for i in range(Npontos-2):
        temperatura.append(condInicial)
    temperatura.append(0)
    print(len(temperatura))
    return temperatura

def criar_vetor_P():
    posicao = []
    pos = comprimento/Npontos
    temp = pos
    for i in range(Npontos):
        posicao.append(pos)
        pos+=temp
    print(len(posicao))
    return posicao

def main():
    temperatura2 = [0]
    temperatura = criar_vetor_T()
    posicao = criar_vetor_P()
    fourier = numeroFourier()
    print(fourier)
    if (fourier > 0.5):
        print("Sem solucao para o sistema")
        return
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
