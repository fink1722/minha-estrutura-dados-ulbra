class PilhaE:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0

    
    def push(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def pop(self):
        self.quant -= 1

    def ver_topo(self):
        return self.vetor[self.quant]
    
    def esta_cheia(self):
        return self.quant == self.tam
        
        
    def esta_vazia(self):
        return self.quant == 0 
   
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print()