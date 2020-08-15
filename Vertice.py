class Vertice():
    def __init__(self,dato):
        self.dato=dato
        self.ListaAdyacentes=[]
        self.ListaIncidentes=[]

    def getDato(self):
        return self.dato

    def setDato(self,dato):
        self.dato=dato

    def getListaAdyacentes(self):
        return self.ListaAdyacentes

    def setListaAdyacentes(self, lista):
        self.ListaAdyacentes = lista

    def setListaIncidentes(self, lista):
        self.ListaIncidentes = lista

    def getListaIncidentes(self):
        return self.ListaIncidentes

    def gradoentrada(self):
        return len(self.ListaIncidentes)

    def gradosalida(self):
        return len(self.ListaAdyacentes)
