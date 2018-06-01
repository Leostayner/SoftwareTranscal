class ArquivoTXT():

    def __init__(self, nome):
        self.alfa = 0
        self.Npontos = 0
        self.tTotal = 0
        self.condInicial = 0
        self.comprimento = 0
        self.deltaT = 0
        self.tA1 = 0
        self.tA2 = 0
        self.tA3 = 0
        self.tA4 = 0
        
        self.lerArquivo(nome)
        self.status()
        
    def lerArquivo(self, nome):
        arquivo = open(nome, "r")
        tags = ["*TIPO","*ALFA","*NUMERO_PONTOS","*TEMPO_TOTAL","*CONDICAO_INICIAL",
                "*COMPRIMENTO","*DELTA_T","*TEMPERATURA_A1","*TEMPERATURA_A2","*TEMPERATURA_A3","*TEMPERATURA_A4"]


        for linha in arquivo:
            linha = linha.replace('\n',"")
           
            if len(linha) > 0:
                
                if (linha[0] == "*"):
                    flag = linha
                
                else:
                    if(flag == "*TIPO"):
                        self.tipo = int(linha)
                     
                    elif(flag == "*ALFA"):
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

                    
                    elif(self.tipo == 2):
                        
                        if(flag == "*TEMPERATURA_A1"):
                           self.tA1 = int(linha)
                           
                        elif(flag == "*TEMPERATURA_A2"):
                            self.tA2 = int(linha)
                        
                        elif(flag == "*TEMPERATURA_A3"):
                            self.tA3 = int(linha)

                        elif(flag == "*TEMPERATURA_A4"):
                            self.tA4 = int(linha)                    
                
        arquivo.close()

    def status(self):
        print("Tipo: {0}".format(self.tipo))
        print("Alfa: {0} ".format(self.alfa))
        print("Numero de Pontos: {0}".format(self.Npontos))
        print("Tempo Total: {0}".format(self.tTotal))
        print("Condição Inicial: {0}".format(self.condInicial))
        print("Comprimento: {0}".format(self.comprimento))
        print("DeltaT: {0}".format(self.deltaT))

        if(self.tipo == 2):
        
            print("Temperatura A1: {0}".format(self.tA1))
            print("Temperatura A2: {0}".format(self.tA2))
            print("Temperatura A3: {0}".format(self.tA3))
            print("Temperatura A4: {0}".format(self.tA4))

            
