from collections import defaultdict

class Grafo(object):
    #Implementação do grafo
    def __init__(self, vertices): 
        #Construtor/Inicializador do grafo
        self.vertices = vertices    #Número de vértices
        self.grafo = [[] for i in range(self.vertices)]     #Lista de Adjacências de cada vértice
    
    def addAresta(self, u, v, peso):
        #Adição de arestas
        self.grafo[u-1].append([v, peso])   #Adiciona v na lista de adjacências de u
        self.grafo[v-1].append([u, peso])   #Adiciona u na lista de adjacências de v
    
    def mostraAdj(self):
        #Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i+1} : {self.grafo[i]}')

def main():
    g = Grafo(9)

    g.addAresta(1, 2, 4)
    g.addAresta(2, 3, 8)
    g.addAresta(3, 4, 7)
    g.addAresta(3, 9, 2)
    g.addAresta(3, 6, 4)
    g.addAresta(4, 5, 9)
    g.addAresta(6, 7, 2)
    g.addAresta(7, 8, 1)

    g.mostraAdj()

if __name__== "__main__" :  
    main()