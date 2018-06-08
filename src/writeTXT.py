class ArquivoTXT():

    def __init__(self, tipo, alfa, Npontos, tTotal, condInicial, comprimento,deltaT, tA1, tA2, tA3, tA4, filename,tolerancia):
        self.tipo = tipo
        self.alfa = alfa
        self.Npontos = Npontos
        self.tTotal = tTotal
        self.condInicial = condInicial
        self.comprimento = comprimento
        self.deltaT = deltaT
        self.tA1 = tA1
        self.tA2 = tA2
        self.tA3 = tA3
        self.tA4 = tA4
        self.tolerancia = tolerancia
        
        
        self.criarTXT(filename)

    def criarTXT(self,nome):
        
        arq = open(nome, 'w')

        arq.write("*TIPO\n")
        arq.write(str(self.tipo) + "\n")
        
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
        
        arq.write("\n*DELTA_T\n")
        arq.write(str(self.deltaT) + "\n")
        
        if(self.tipo == 2):
            arq.write("\n*TEMPERATURA_A1\n")
            arq.write(str(self.tA1) + "\n")
        
            arq.write("\n*TEMPERATURA_A2\n")
            arq.write(str(self.tA2) + "\n")
        
            arq.write("\n*TEMPERATURA_A3\n")
            arq.write(str(self.tA3) + "\n")
        
            arq.write("\n*TEMPERATURA_A4\n")
            arq.write(str(self.tA4) + "\n")

            arq.write("\n*TOLERANCIA\n")
            arq.write(str(self.tolerancia) + "\n")
        
        arq.close()