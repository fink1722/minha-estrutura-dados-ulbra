class Filad:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1


    def remover_inicio(self):
        for i in range(self.quant -1):
            self.vetor[i] = self.vetor[i+1]
        self.quant -= 1

    def esta_vazia():
        return self.quant == 0 

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print()
