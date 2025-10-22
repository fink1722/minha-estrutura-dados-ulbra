class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class PilhaD:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def push(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1 
    
    def pop(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox


        self.quant -= 1

    def ver_topo(self):
        return self.prim.info
    
    def esta_vazia(self):
        return self.quant == 0
    
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox

    
    