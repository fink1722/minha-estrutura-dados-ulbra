class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0


    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1 


    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox


        self.quant -= 1


    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox 

    def inserir_fim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def ver_primeiro(self):
        return self.prim.info

    def ver_ultimo(self):
        return self.ult.info

    def ver_quantidad(self):
        return self.quant

    def esta_vazia(self):
        return self.quant == 0


    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox

            self.ult = aux
            self.ult.prox = None

        self.quant -= 1

    
    def remover(self, valor):
        aux = self.prim
        ant = None
        while aux !=None and aux.info != valor:
            ant = aux
            aux = aux.prox
        if aux != None:
            if aux == self.prim:
                self.prim = self.prim.prox
            else:
                ant.prox = aux.prox
            if aux == self.ult:
                self.ult = ant 
            self.quant -= 1



    def removerTf(self, valor):
        aux = self.prim
        ant = None
        while aux !=None and aux.info != valor:
            ant = aux
            aux = aux.prox
        if aux != None:
            if aux == self.prim:
                self.prim = self.prim.prox
            else:
                ant.prox = aux.prox
            if aux == self.ult:
                self.ult = ant 
            self.quant -= 1

        
                    
            
                






        
    
