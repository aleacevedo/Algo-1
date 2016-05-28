class _NewNodo:
    def __init__(self, dato=None, prox=None):
        self.dato=dato
        self.prox=prox

class ListaEnlazada:
    def __init__(self):
        self.primero=None
        self.len=0

    def __str__(self):
        datos="["
        actual=self.primero
        if(actual==None):
            datos="]"
        else:
            while(actual.prox!=None):
                datos=datos+str(actual.dato)+","
                actual=actual.prox
            datos=datos+str(actual.dato)+"]"
        return datos

    def append(self, ingreso):
        actual=self.primero
        if(actual==None):
            self.primero=_NewNodo(ingreso)
        else:
            while(actual.prox!=None):
                actual=actual.prox
            actual.prox=_NewNodo(ingreso)
        self.len=self.len+1

    def pop(self, index=None):
        anterior=self.primero
        if(index==None):
            index=self.len-1
        if(anterior==None):
            raise IndexError("pop from empty list")
        elif(index>=self.len or index<0):
            raise IndexError("pop index out of range")
        elif(index==0):
            anterior=self.primero
            actual=anterior.prox
            dato=anterior.dato
            self.primero=self.primero.prox
        else:
            anterior=self.primero
            actual=anterior.prox
            for i in range(1, index):
                anterior=actual
                actual=actual.prox
            dato=actual.dato
            anterior.prox=actual.prox
        self.len=self.len-1
        return dato

    def __len__(self):
        return self.len

    def __iter__(self):
        return _IteradorLista(self.primero)

class _IteradorLista:
    def __init__(self, primero):
        self.actual=primero

    def __next__(self):
        if self.actual==None:
            raise StopIteration()
        dato = self.actual.dato
        self.actual=self.actual.prox
        return dato
