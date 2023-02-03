import math

class Grafo(object):
    #Implementação do grafo
    def __init__(self, vertices): 
        #Construtor/Inicializador do grafo
        self.vertices = vertices    #Número de vértices
        self.grafo = [[] for i in range(self.vertices)]     #Lista de Adjacências de cada vértice
        self.cor = [[] for i in range(self.vertices)]       #Lista de cores de cada vértice
        self.dist = [[] for i in range(self.vertices)]      #Lista de distância de cada vértice
        self.pai = [[] for i in range(self.vertices)]       #Lista de pai de cada vértice
    
    def addAresta(self, u, v):
        #Adição de arestas
        self.grafo[u].append(v)   #Adiciona v na lista de adjacências de u
        self.grafo[v].append(u)   #Adiciona u na lista de adjacências de v
    
    def mostraAdj(self):
        #Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i} : ', end='')   #Mostra vértice i
            for aresta in self.grafo[i]:    #Mostra adjacências do vértice i
                print(f'[{aresta}] => ', end='')    
            print('/')  #Pula Linha

    def mostraVertices(self):
        #Mostra caracteristicas dos vértices (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'{i} : cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}')


def BFS(g, s):
    for u in range(g.vertices):
        if u != s:
            g.cor[u] = 'B'
            g.dist[u] = math.inf
            g.pai[u] = None
    g.cor[s] = 'C'
    g.dist[s] = 0
    g.pai[s] = None
    q = []
    q.append(s)
    while q != []:
        print(q)
        u = q.pop(-1)
        for v in g.grafo[u]:
            if g.cor[v] == 'B':
                g.cor[v] = 'C'
                g.dist[v] = g.dist[u] + 1
                g.pai[v] = u
                q.append(v)
        g.cor[u] = 'P'


def main():
    g = Grafo(8)

    g.addAresta(0,1)
    g.addAresta(0,4)
    g.addAresta(1,5)
    g.addAresta(2,5)
    g.addAresta(2,6)
    g.addAresta(2,3)
    g.addAresta(3,6)
    g.addAresta(3,7)

    g.mostraAdj()
    print('BFS')
    #g.mostraVertices()

    BFS(g, 0)
    g.mostraVertices()

if __name__== "__main__" :  
    main()