lista=[2,3,0,1]
lista2=[2,3,0,1]
lista3=[1,4,3,2]

class Polinomios:
    def __init__(self,coeficiente):
        self.cof=""
        self.coeficiente=coeficiente
        for y, x in enumerate (coeficiente):
            if(x!=0):
                if(y!=0):
                    self.cof="{}X^{} + ".format(x,y) +self.cof
                else:
                    self.cof="{} ".format(x) +self.cof
    def __str__(self):
        return  self.cof

    def eq(self,coeficiente2):
        if(self.coeficiente==coeficiente2.coeficiente):
            return True
        else:
            return False



    def derivar(self):
        self.cof=""
        for y,x in enumerate(self.coeficiente):
            newcof = int(x) * int(y)
            newpot = y - 1
            if(newcof!=0):
                if(newpot>0):
                    self.cof="{}X^{} + ".format(newcof,newpot) +self.cof
                elif(newpot==0):
                    self.cof="{}".format(newcof) +self.cof
        return self.cof

p=Polinomios(lista)
q=Polinomios(lista2)
r=Polinomios(lista3)

print(p)
print(q)
print(r)
print(q.eq(p))
print(q.eq(r))
print(q.derivar())
print(r.derivar())
