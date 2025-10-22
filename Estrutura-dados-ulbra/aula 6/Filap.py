from fila_dinamica import fila_dinamica

class fila_prioridade:
    def __init__(self):
        self.fila1 = fila_dinamica()
        self.fila2 = fila_dinamica()
        self.fila3 = fila_dinamica()
        self.fila4 = fila_dinamica()

    def inserir(self, valor, prioridade):
        if prioridade == "P1":
            self.fila4.inserir(valor)
        elif prioridade == "P2":
            self.fila3.inserir(valor)
        elif prioridade == "P3":
            self.fila2.inserir(valor)
        elif prioridade == "P4":
            self.fila1.inserir(valor)

    
    def ver_primeiro(self):
        if  self.fila4.esta_vazia()== False:
            return self.fila4.ver_primeiro()
        elif not self.fila3.esta_vazia()== False:
            return self.fila3.ver_primeiro()
        elif not self.fila2.esta_vazia()== False:
            return self.fila2.ver_primeiro()
        elif not self.fila1.esta_vazia()== False:
            return self.fila1.ver_primeiro()
            
        return None 



    def esta_vazia(self):
        
        return (self.fila1.esta_vazia() and
                self.fila2.esta_vazia() and
                self.fila3.esta_vazia() and
                self.fila4.esta_vazia())


    def show(self):
       ("************************************")
