class No:
    def __init__(self, ant, info, prox):
        self.ant  = ant
        self.info = info
        self.prox = prox


class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    # ---------------- inserções ----------------
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    # --------------- remoção por intervalo ---------------
    def remover_intervalo(self, inicio, fim):
        if inicio < 0 or fim >= self.quant or fim < inicio:
            print('erro')
        else:
            aux_inicio = self.prim
            for i in range(inicio):
                aux_inicio = aux_inicio.prox

            aux_fim = self.prim
            for i in range(fim):
                aux_fim = aux_fim.prox

            if aux_inicio == self.prim:
                self.prim = aux_fim.prox
                
            else:
                aux_inicio.ant.prox = aux_fim.prox
            if aux_fim == self.ult:
                self.ult = aux_incial.ant
            else:
                aux_fim.prox.ant = aux_inicio.ant
            self.quant -= (fim - inicio) + 1
  
    # ---------------- exibição ----------------
    def show(self):
        aux = self.prim
        while aux:
            print(aux.info, end='')
            aux = aux.prox
        print()

    def show_reverso(self):
        aux = self.ult
        while aux:
            print(aux.info, end='')
            aux = aux.ant
        print()


    def remover_antes(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

        
        




