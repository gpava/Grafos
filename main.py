from Grafos.Grafo import *

def main():
    G=Grafo()
    """G.ingresarvertice('A')
    G.ingresarvertice('B')
    G.ingresarvertice('C')
    G.ingresarvertice('D')
    G.ingresarvertice('E')
    G.ingresararista('A', 'B', 3, False)
    G.ingresararista('A', 'C', 1, False)
    G.ingresararista('C', 'B', 7, False)
    G.ingresararista('C', 'D', 2, False)
    G.ingresararista('D', 'B', 5, False)
    G.ingresararista('D', 'E', 7, False)
    G.ingresararista('B', 'E', 1, False)"""
    G.ingresarvertice("Silvestre")
    G.ingresarvertice("Tazmania")
    G.ingresarvertice("Yayita")
    G.ingresarvertice("Coyote")
    G.ingresarvertice("Piolin")
    G.ingresarvertice("Bunny")
    G.ingresarvertice("Popeye")
    G.ingresarvertice("Marvin")
    G.ingresarvertice("Correcaminos")
    G.ingresararista("Silvestre","Piolin",10,False)
    G.ingresararista("Silvestre", "Tazmania", 15, False)
    G.ingresararista("Piolin", "Popeye", 30, False)
    G.ingresararista("Yayita", "Piolin", 25, False)
    G.ingresararista("Yayita", "Tazmania", 16, False)
    G.ingresararista("Yayita", "Bunny", 22, False)
    G.ingresararista("Bunny", "Tazmania", 33, False)
    G.ingresararista("Coyote", "Tazmania", 21, False)
    G.ingresararista("Coyote", "Marvin", 58, False)
    G.ingresararista("Bunny", "Marvin", 2, False)
    G.ingresararista("Marvin", "Correcaminos", 44, False)
    G.ingresararista("Correcaminos", "Bunny", 60, False)
    G.ingresararista("Correcaminos", "Popeye", 5, False)
    G.caminoMasCorto("Silvestre","Popeye")



main()
