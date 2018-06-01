
class ArquivoTXT():

    def __init__(self, nome):
        self.alfa = 0
        self.Npontos = 0
        self.tTotal = 0
        self.condInicial = 0
        self.comprimento = 0
        self.deltaT = 0
        self.lerArquivo(nome)
        #self.status()
        
    def lerArquivo(self, nome):
        arquivo = open(nome, "r")
        tags = ["*ALFA","*NUMERO_PONTOS","*TEMPO_TOTAL","*CONDICAO_INICIAL",
                "*COMPRIMENTO","*DELTA_T"]

        flag = ""

        for linha in arquivo:
            linha = linha.replace('\n',"")
           
            if len(linha) > 0:
                
                if (linha[0] == "*"):
                    flag = linha
                
                else: 
                    if(flag == "*ALFA"):
                        self.alfa = int(linha)
                    
                    elif(flag == "*NUMERO_PONTOS"):
                        self.Npontos = int(linha)

                    elif(flag == "*TEMPO_TOTAL"):
                        self.tTotal = int(linha)

                    elif(flag == "*CONDICAO_INICIAL"):
                        self.condInicial = int(linha)
                    
                    elif(flag == "*COMPRIMENTO"):
                        self.comprimento = int(linha)
                    
                    elif(flag == "*DELTA_T"):
                        self.deltaT = int(linha)    

                    
        arquivo.close()

    def status(self):
        print("Alfa: {0} ".format(self.alfa))
        print("Numero de Pontos: {0}".format(self.Npontos))
        print("Tempo Total: {0}".format(self.tTotal))
        print("Condição Inicial: {0}".format(self.condInicial))
        print("Comprimento: {0}".format(self.comprimento))
