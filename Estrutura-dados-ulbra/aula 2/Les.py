class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0


    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print()
        
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
        
    def esta_cheia(self):
        return self.quant == self.tam
        
        
    def esta_vazia():
        return self.quant == 0 


    def remover_fim(self):
        self.quant -= 1

    def inserir_inicio(self, valor):
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i-1]
        self.vetor[0] = valor
        self.quant += 1
    

    def remover_inicio(self):
        for i in range(self.quant -1):
            self.vetor[i] = self.vetor[i+1]
        self.quant -= 1

     #def remover_inicio(self):
        #for i in range(1, self.quant):
            #self.vetor[i-1] = self.vetor[i]
        #self.quant -= 1
    

    def remover(self, valor):
        #remove valor de lista
        #considera que não há valores repetidos
        for i in range(self.quant):
            if valor == self.vetor[i]:
                for i in range(i,self.quant):
                    self.vetor[i] = self.vetor[i+1]
                self.quant -= 1
                break
            else:
                print("valor nao encontrado ")


    def removerTF(self, valor):
        #remove valor da lista
        #retorna True se houve remoção
        #e False caso contrário
        #considere que não há valores repetidos 
        for i in range(self.quant):
            if valor == self.vetor[i]:
                for i in range(i,self.quant):
                    self.vetor[i] = self.vetor[i+1]
                self.quant -= 1
                return True
        return False
                
        

    def remove_e_contar(self, valor):
        y = 0
        for i in range(self.quant):
            if valor == self.vetor[i]:
                for i in range(i, self.quant -1):
                    self.vetor[i] = self.vetor[i+1]
                self.quant -= 1
                y += 1
                
        return y
        
        #remove valor da lista e retorna
        #quantas remoções foram feitas 
        #considere que pode haver valores repetidos '''



        
    
   
     


