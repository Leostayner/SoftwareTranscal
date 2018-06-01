class ArquivoTXT():

    def __init__(self, alfa, Npontos, tTotal, condInicial, comprimento, filename):
        self.alfa = alfa
        self.Npontos = Npontos
        self.tTotal = tTotal
        self.condInicial = condInicial
        self.comprimento = comprimento
        self.criarTXT(filename)

    def criarTXT(self,nome):
        
        arq = open(nome, 'w')

        arq.write("*ALFA\n")
        arq.write(str(self.alfa) + "\n")
        
        arq.write("\n*NUMERO_PONTOS\n")
        arq.write(str(self.Npontos) + "\n")
            
        arq.write("\n*TEMPO_TOTAL\n")
        arq.write(str(self.tTotal) + "\n")
            
        arq.write("\n*CONDICAO_INICIAL\n")
        arq.write(str(self.condInicial) + "\n")
        
        arq.write("\n*COMPRIMENTO\n")
        arq.write(str(self.comprimento) + "\n")
        
        arq.close()