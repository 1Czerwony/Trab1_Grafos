import math, random

class Grafo(object):
    #Implementação do grafo
    def __init__(self, vertices): 
        #Construtor/Inicializador do grafo
        self.vertices = vertices    #Número de vértices
        self.ciclico = False
        self.adj = [[] for i in range(self.vertices)]       #Lista de Adjacências de cada vértice
        self.cor = [[] for i in range(self.vertices)]       #Lista de cores de cada vértice
        self.dist = [[] for i in range(self.vertices)]      #Lista de distância de cada vértice
        self.pai = [[] for i in range(self.vertices)]       #Lista de pai de cada vértice
        self.desc = [[] for i in range(self.vertices)]      #Lista de tempo de descoberta de cada vértice
        self.termino = [[] for i in range(self.vertices)]   #Lista de tempo de término de cada vértice

    
    def addAresta(self, u, v):
        #Adição de arestas
        self.adj[u].append(v)   #Adiciona v na lista de adjacências de u
        self.adj[v].append(u)   #Adiciona u na lista de adjacências de v
    
    def mostraAdj(self):
        #Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i} => ', end='')   #Mostra vértice i
            for aresta in self.adj[i]:    #Mostra adjacências do vértice i
                print(f'[{aresta}] => ', end='')    
            print('/')  #Pula Linha

    def mostraBFS(self):
        #Mostra caracteristicas dos vértices baseado no algoritimo BFS (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}]')
    
    def mostraDFS(self):
        #Mostra caracteristicas dos vértices baseado no algoritimo DFS (cor, tempo descoberta/término, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, tempo de descoberta/término = {self.desc[i]}/{self.termino[i]}, pai = {self.pai[i]}]')


def BFS(g, s):      #Recebe Grafo g e vértice inicial s
    for u in range(g.vertices):     #Percorre os vértices do grafo g
        if u != s:                  #Pula o vértice s
            g.cor[u] = 'B'          #Define cor como BRANCO
            g.dist[u] = math.inf    #Define distancia como infinito
            g.pai[u] = None         #Define pai como NULO
    g.cor[s] = 'C'      #Define cor de s como CINZA
    g.dist[s] = 0       #Define distância de s como 0
    g.pai[s] = None     #Define pai de s como NULO
    q = [s]             #Declara fila q e insere s
    while q != []:                              #Enquanto fila q não for vazia
        u = q.pop(-1)                           #Vértice u recebe último vértice da fila q
        for v in g.adj[u]:                      #Para cada v adjacente de u
            if g.cor[v] == 'B':                 #Se v for BRANCO
                g.cor[v] = 'C'                  #Define v como CINZA
                g.dist[v] = g.dist[u] + 1       #Define distancia de v como distancia de u + 1
                g.pai[v] = u                    #Define pai de v como u
                q.append(v)                     #Adiciona vértice v na fila q
        g.cor[u] = 'P'      #Define cor de u como PRETO


def DFS(g):
    for u in range(g.vertices):
        g.cor[u] = 'B'
        g.pai[u] = None
    tempo = 0
    for u in range(g.vertices):
        if g.cor[u] == 'B':
            tempo = DFSVisit(g, u, tempo)
def DFSVisit(g, u, tempo):
    tempo += 1
    g.desc[u] = tempo
    g.cor[u] = 'C'
    for v in g.adj[u]:
        if g.cor[v] == 'B':
            g.pai[v] = u
            tempo = DFSVisit(g, v, tempo)
        elif v != g.pai[u]:
            g.ciclico = True
    g.cor[u] = 'P'
    tempo += 1
    g.termino[u] = tempo
    return tempo


def isTree(g):
    DFS(g)
    count = 0
    for u in range(g.vertices):
        if g.pai[u] == None:
            count += 1
    if g.ciclico == False and count < 2:
        return True
    else:
        return False


def diametro(t):
    if not isTree(t):
        print('**NÃO É ÁRVORE**')
        return 0
    s = random.randint(0, t.vertices-1)
    BFS(t, s)
    a = t.dist.index(max(t.dist))
    BFS(t, a)
    b = t.dist.index(max(t.dist))
    return t.dist[b]


def main():
    '''
    Representação do grafo de exemplo:
    0---1   2---3 
    |   | ̷  | ̷  |
    4   5---6---7
    '''
    g = Grafo(8)

    g.addAresta(0,1)
    g.addAresta(0,4)
    g.addAresta(1,5)
    g.addAresta(2,5)
    g.addAresta(2,6)
    g.addAresta(2,3)
    g.addAresta(3,6)
    g.addAresta(3,7)
    g.addAresta(5,6)
    g.addAresta(6,7)

    #g.mostraAdj()
    #DFS(g)
    #g.mostraDFS()
    #print(isTree(g))
    #diametro(g)
    ##################

    h = Grafo(9)
    
    h.addAresta(0,1)
    h.addAresta(1,2)
    h.addAresta(2,3)
    h.addAresta(2,5)
    h.addAresta(2,8)
    h.addAresta(3,4)
    h.addAresta(5,6)
    h.addAresta(6,7)

    h.mostraAdj()
    print(isTree(h))
    print(diametro(h))
    ##################

if __name__== "__main__" :  
    main()