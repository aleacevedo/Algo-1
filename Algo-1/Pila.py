class _NewNodo:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

class Pila:
    def __init__(self):
        self.prim=None
        self.len=0
    def apila(self, dato):
        actual=self.prim
        if actual==None:
            self.prim=_NewNodo(dato)
        else:
            while !actual.prox:
                actual=actual.prox
            actual.prox=_NewNodo(dato)
            
