class Frac:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador
    def show(self):
        #print(self.num, '/', self.den)
        print(f"{self.num}/{self.den}")
        #print(str(self.num)+'/'+str(self.den))
    def mult(self,outra):
        n = self.num * outra.num
        d = self.den * outra.den 
        return Frac(n,d)
    def div(self,outra):
        n = self.num * outra.den
        d = self.den * outra.num
        return Frac(n,d)
    def divsom(self,outra):
        n = (self.num * outra.den) + (outra.num * self.den)
        d = self.den * outra.den
        return Frac(n,d)
    def divsub(self,outra):
        n = (self.num * outra.den) - (outra.num * self.den)
        d = self.den * outra.den
        return Frac(n,d)
