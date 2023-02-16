import math, random, time           #math é usado para valores infinitos; random para obter um vértice aleatório em BFS; time para cálculo de tempo
from collections import deque       #deque é uma implementação de fila que funciona em tempo constante

class Grafo(object):

    def __init__(self, vertices): 
        # Declara uma lista para cada característica do vértice onde um índice i da lista representa um vértice i do grafo
        self.vertices = vertices                            # Número de vértices
        self.adj = [[] for i in range(self.vertices)]       # Lista de Adjacências de cada vértice
        self.cor = [[] for i in range(self.vertices)]       # Lista de cores de cada vértice
        self.dist = [[] for i in range(self.vertices)]      # Lista de distância de cada vértice
        self.pai = [[] for i in range(self.vertices)]       # Lista de pai de cada vértice
        self.visitado = [[] for i in range(self.vertices)]  # Vértice i foi visitado True ou False
    
    def addAresta(self, u, v):
        # Adição de uma aresta entre o vértice u e o vértice v
        self.adj[u].append(v)   
        self.adj[v].append(u)                          

    def mostraBFS(self):
        # Mostra caracteristicas dos vértices baseado no algoritimo BFS (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}]')

    
# Busca em largura que define distância dos vértices com relação a um vértice inicial 's'
# Usada para cálculo do diâmetro de uma árvore
def BFS(g, s):                                  
    for u in range(g.vertices):                 # Reseta todos os vértices para BRANCO e dist = infinito
        if u != s:                              
            g.cor[u] = 'B'                      
            g.dist[u] = math.inf                
            g.pai[u] = None                    
    g.cor[s] = 'C'                              # Cor do vértice inicial = CINZA
    g.dist[s] = 0                               
    g.pai[s] = None                            
    q = deque()
    q.append(s)                                 # Fila 'q' onde o primeiro vértice será visitado e eliminado da fila e seus vértices filhos serão adicionados ao final da fila
    while q != deque([]):                             
        u = q.popleft()                            
        for v in g.adj[u]:                      
            if g.cor[v] == 'B':                 
                g.cor[v] = 'C'                  
                g.dist[v] = g.dist[u] + 1       # Vértices descobertos recebem a distância de seu pai + 1
                g.pai[v] = u                    
                q.append(v)                     
        g.cor[u] = 'P'                          # Define cor de u como PRETO


# Se o grafo é uma árvore retorna TRUE, senão retorna FALSE
# Retorna True se o grafo é CONEXO e ACÍCLICO
def isTree(g): 
    # Verifica se é CONEXO                             
    count = 0
    for u in range(g.vertices):                     # Se o número de vértices com pai = NULO for maior do que 1 após a execução do BFS, então o grafo NÃO É CONEXO
        if g.pai[u] == None:                    
            count += 1                         
    if count > 1:                                   # Retorna FALSE se o grafo é DESCONEXO
        return False
    # Se é CONEXO então verifica se é ACÍCLICO                          
    else:                                       
        arestas = 0
        for u in g.adj:                             # Soma todas as adjacências do grafo e as divide por 2, isto nos da o numero de arestas do grafo
            arestas += len(u)                       
        arestas = arestas/2
        if arestas > (g.vertices-1):                # Se o número de arestas do grafo é maior do que o número de vértices + 1, então o grafo é CÍCLICO, senão é ACÍCLICO
            return False
        else:
            return True


# Calcula o diâmetro de uma árvore t
# O diâmetro de uma árvore é o caminho mais longo possível entre dois vértices
def diametro(t):
    s = random.randint(0, t.vertices-1)     	# Gera um indice aleatório da lista de vértices
    BFS(t, s)                                  
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado porque o grafo não é uma árvore
        return -1
    a = t.dist.index(max(t.dist))               # A partir de qualquer vértice no grafo, aplicamos BFS e obtemos o vértice mais distante possível e damos a ele o nome de 'a'
    BFS(t, a)                                   # A distância de 'a' até o seu vértice mais distante nos da o diâmetro da árvore 
    return max(t.dist)


# Gera árvores aleatórias de n vértices
# Uma árvore é um grafo acíclico e conexo
def RandomTreeRandomWalk(n):
    g = Grafo(n)
    for u in range(n):                                                  # Inicializa todos vértices como não visitados
        g.visitado[u] = False
    u = random.randint(0, n-1)                                          # Gera um indice aleatório da lista de vértices                           
    g.visitado[u] = True
    count = 0
    while count < n-1:                                                  # Adiciona arestas válidas até que o número de arestas seja n - 1
        v = random.randint(0, n-1)
        if g.visitado[v] == False and v not in g.adj[u] and v != u:
            g.addAresta(u,v)
            g.visitado[v] = True
            count += 1
        u = v
    return g


def main():
    '''
    Representação do grafo de exemplo 1:
    0---1   2---3 
    |   | ̷  | ̷  |
    4   5---6---7
     - Cíclico
     - Conexo
    '''
    # Contrução do grafo
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
    
    # Assert para __init__
    assert g.vertices == 8
    assert len(g.adj) == 8
    assert len(g.cor) == 8
    assert len(g.dist) == 8
    assert len (g.pai) == 8
    
    # Assert para addAresta e mostraAdj
    assert g.adj[0] == [1,4]
    assert g.adj[1] == [0,5] 
    assert g.adj[2] == [5,6,3] 
    assert g.adj[3] == [2,6,7] 
    assert g.adj[4] == [0] 
    assert g.adj[5] == [1,2,6] 
    assert g.adj[6] == [2,3,5,7] 
    assert g.adj[7] == [3,6]
    
    # Assert para BFS
    BFS(g, 1)
    ##g.mostraAdj()
    ##g.mostraBFS()
    for cor in g.cor:
        assert cor == 'P'
        assert g.dist[0] == 1 
        assert g.pai[0] == 1
        assert g.dist[1] == 0
        assert g.pai[1] == None
        assert g.dist[2] == 2 
        assert g.pai[2] == 5
        assert g.dist[3] == 3 
        assert g.pai[3] == 2
        assert g.dist[4] == 2 
        assert g.pai[4] == 0
        assert g.dist[5] == 1 
        assert g.pai[5] == 1
        assert g.dist[6] == 2 
        assert g.pai[6] == 5
        assert g.dist[7] == 3 
        assert g.pai[7] == 6

    # Assert para isTree
    assert isTree(g) == False
    
    #Assert para diametro
    assert diametro(g) == -1
    
    '''
    Representação do grafo de exemplo 2:
    0   1---2   3---4   5   6---7   
     - Acíclico
     - Desconexo
    '''
    # Contrução do grafo
    h = Grafo(8)
    h.addAresta(1,2)
    h.addAresta(3,4)
    h.addAresta(6,7)
    
    # Assert para __init__
    assert h.vertices == 8
    assert len(h.adj) == 8
    assert len(h.cor) == 8
    assert len(h.dist) == 8
    assert len (h.pai) == 8
    
    # Assert para addAresta e mostraAdj
    assert h.adj[0] == [ ]
    assert h.adj[1] == [2] 
    assert h.adj[2] == [1] 
    assert h.adj[3] == [4] 
    assert h.adj[4] == [3] 
    assert h.adj[5] == [ ] 
    assert h.adj[6] == [7] 
    assert h.adj[7] == [6]
    
    # Assert para BFS (primeira componente)
    BFS(h, 0)
    ##h.mostraAdj()
    ##h.mostraBFS()
    
    assert h.cor[0] == 'P'     
    assert h.dist[0] == 0 
    assert h.pai[0] == None
    assert h.cor[1] == 'B'
    assert h.dist[1] == math.inf
    assert h.pai[1] == None
    assert h.cor[2] == 'B'
    assert h.dist[2] == math.inf 
    assert h.pai[2] == None
    assert h.cor[3] == 'B'
    assert h.dist[3] == math.inf 
    assert h.pai[3] == None
    assert h.cor[4] == 'B'
    assert h.dist[4] == math.inf 
    assert h.pai[4] == None
    assert h.cor[5] == 'B'
    assert h.dist[5] == math.inf 
    assert h.pai[5] == None
    assert h.cor[6] == 'B'
    assert h.dist[6] == math.inf
    assert h.pai[6] == None
    assert h.cor[7] == 'B'
    assert h.dist[7] == math.inf 
    assert h.pai[7] == None
    
    # Assert para BFS (segunda componente)
    BFS(h, 1)
    ##h.mostraBFS()
    
    assert h.cor[0] == 'B'     
    assert h.dist[0] == math.inf
    assert h.pai[0] == None
    assert h.cor[1] == 'P'
    assert h.dist[1] == 0
    assert h.pai[1] == None
    assert h.cor[2] == 'P'
    assert h.dist[2] == 1 
    assert h.pai[2] == 1
    assert h.cor[3] == 'B'
    assert h.dist[3] == math.inf 
    assert h.pai[3] == None
    assert h.cor[4] == 'B'
    assert h.dist[4] == math.inf 
    assert h.pai[4] == None
    assert h.cor[5] == 'B'
    assert h.dist[5] == math.inf 
    assert h.pai[5] == None
    assert h.cor[6] == 'B'
    assert h.dist[6] == math.inf
    assert h.pai[6] == None
    assert h.cor[7] == 'B'
    assert h.dist[7] == math.inf 
    assert h.pai[7] == None
    
    # Assert para BFS (terceira componente)
    BFS(h, 3)
    ##h.mostraBFS()

    assert h.cor[0] == 'B'     
    assert h.dist[0] == math.inf
    assert h.pai[0] == None
    assert h.cor[1] == 'B'
    assert h.dist[1] == math.inf
    assert h.pai[1] == None
    assert h.cor[2] == 'B'
    assert h.dist[2] == math.inf 
    assert h.pai[2] == None
    assert h.cor[3] == 'P'
    assert h.dist[3] == 0 
    assert h.pai[3] == None
    assert h.cor[4] == 'P'
    assert h.dist[4] == 1 
    assert h.pai[4] == 3
    assert h.cor[5] == 'B'
    assert h.dist[5] == math.inf 
    assert h.pai[5] == None
    assert h.cor[6] == 'B'
    assert h.dist[6] == math.inf
    assert h.pai[6] == None
    assert h.cor[7] == 'B'
    assert h.dist[7] == math.inf 
    assert h.pai[7] == None

    # Assert para BFS (quarta componente)
    BFS(h, 5)
    ##h.mostraBFS()

    assert h.cor[0] == 'B'     
    assert h.dist[0] == math.inf
    assert h.pai[0] == None
    assert h.cor[1] == 'B'
    assert h.dist[1] == math.inf
    assert h.pai[1] == None
    assert h.cor[2] == 'B'
    assert h.dist[2] == math.inf 
    assert h.pai[2] == None
    assert h.cor[3] == 'B'
    assert h.dist[3] == math.inf 
    assert h.pai[3] == None
    assert h.cor[4] == 'B'
    assert h.dist[4] == math.inf 
    assert h.pai[4] == None
    assert h.cor[5] == 'P'
    assert h.dist[5] == 0 
    assert h.pai[5] == None
    assert h.cor[6] == 'B'
    assert h.dist[6] == math.inf
    assert h.pai[6] == None
    assert h.cor[7] == 'B'
    assert h.dist[7] == math.inf 
    assert h.pai[7] == None
    
    # Assert para BFS (quinta componente)
    BFS(h, 6)
    ##h.mostraBFS()
    
    assert h.cor[0] == 'B'     
    assert h.dist[0] == math.inf
    assert h.pai[0] == None
    assert h.cor[1] == 'B'
    assert h.dist[1] == math.inf
    assert h.pai[1] == None
    assert h.cor[2] == 'B'
    assert h.dist[2] == math.inf 
    assert h.pai[2] == None
    assert h.cor[3] == 'B'
    assert h.dist[3] == math.inf 
    assert h.pai[3] == None
    assert h.cor[4] == 'B'
    assert h.dist[4] == math.inf 
    assert h.pai[4] == None
    assert h.cor[5] == 'B'
    assert h.dist[5] == math.inf 
    assert h.pai[5] == None
    assert h.cor[6] == 'P'
    assert h.dist[6] == 0
    assert h.pai[6] == None
    assert h.cor[7] == 'P'
    assert h.dist[7] == 1 
    assert h.pai[7] == 6

    # Assert para isTree
    assert isTree(h) == False
    
    #Assert para diametro
    assert diametro(h) == -1
    
    '''
    Representação do grafo de exemplo 3:
    0---1   4---5
    |   |   |
    2---3   6
     - Cíclico
     - Desconexo
    '''
    # Contrução do grafo
    i = Grafo(7)
    i.addAresta(0,1)
    i.addAresta(0,2)
    i.addAresta(2,3)
    i.addAresta(1,3)
    i.addAresta(4,5)
    i.addAresta(4,6)
    
    # Assert para __init__
    assert i.vertices == 7
    assert len(i.adj) == 7
    assert len(i.cor) == 7
    assert len(i.dist) == 7
    assert len (i.pai) == 7
    
    # Assert para addAresta e mostraAdj
    assert i.adj[0] == [1,2]
    assert i.adj[1] == [0,3] 
    assert i.adj[2] == [0,3] 
    assert i.adj[3] == [2,1] 
    assert i.adj[4] == [5,6] 
    assert i.adj[5] == [4] 
    assert i.adj[6] == [4] 
    
    # Assert para BFS (primeira componente)
    BFS(i, 0)
    ##i.mostraAdj()
    
    ##i.mostraBFS()
    
    assert i.cor[0] == 'P'     
    assert i.dist[0] == 0 
    assert i.pai[0] == None
    assert i.cor[1] == 'P'
    assert i.dist[1] == 1
    assert i.pai[1] == 0
    assert i.cor[2] == 'P'
    assert i.dist[2] == 1 
    assert i.pai[2] == 0
    assert i.cor[3] == 'P'
    assert i.dist[3] == 2 
    assert i.pai[3] == 1
    assert i.cor[4] == 'B'
    assert i.dist[4] == math.inf 
    assert i.pai[4] == None
    assert i.cor[5] == 'B'
    assert i.dist[5] == math.inf 
    assert i.pai[5] == None
    assert i.cor[6] == 'B'
    assert i.dist[6] == math.inf
    assert i.pai[6] == None
    
    # Assert para BFS (segunda componente)
    BFS(i, 4)
    ##i.mostraBFS()
    
    assert i.cor[0] == 'B'     
    assert i.dist[0] == math.inf
    assert i.pai[0] == None
    assert i.cor[1] == 'B'
    assert i.dist[1] == math.inf
    assert i.pai[1] == None
    assert i.cor[2] == 'B'
    assert i.dist[2] == math.inf 
    assert i.pai[2] == None
    assert i.cor[3] == 'B'
    assert i.dist[3] == math.inf 
    assert i.pai[3] == None
    assert i.cor[4] == 'P'
    assert i.dist[4] == 0 
    assert i.pai[4] == None
    assert i.cor[5] == 'P'
    assert i.dist[5] == 1
    assert i.pai[5] == 4
    assert i.cor[6] == 'P'
    assert i.dist[6] == 1
    assert i.pai[6] == 4

    # Assert para isTree
    assert isTree(i) == False
    
    #Assert para diametro
    assert diametro(i) == -1
    
    '''
    Representação do grafo de exemplo 4:
    0---1---2---3---4
	      ̷  |
        8   5---6---7
     - Acíclico
     - Conexo
    '''
    # Contrução do grafo
    j = Grafo(9)
    j.addAresta(0,1)
    j.addAresta(1,2)
    j.addAresta(2,3)
    j.addAresta(2,5)
    j.addAresta(2,8)
    j.addAresta(3,4)
    j.addAresta(5,6)
    j.addAresta(6,7)
    
    # Assert para BFS
    BFS(j, 8)
    ##j.mostraAdj()
    ##j.mostraBFS()
    
    for cor in j.cor:
        assert cor == 'P'
        
    assert j.dist[0] == 3
    assert j.pai[0] == 1
    assert j.dist[1] == 2
    assert j.pai[1] == 2
    assert j.dist[2] == 1
    assert j.pai[2] == 8
    assert j.dist[3] == 2
    assert j.pai[3] == 2
    assert j.dist[4] == 3
    assert j.pai[4] == 3
    assert j.dist[5] == 2
    assert j.pai[5] == 2
    assert j.dist[6] == 3
    assert j.pai[6] == 5
    assert j.dist[7] == 4
    assert j.pai[7] == 6
    assert j.dist[8] == 0
    assert j.pai[8] == None
    
    # Assert para isTree
    assert isTree(j) == True
    
    # Assert para diametro
    assert diametro(j) == 5


    with open('randomwalk.txt', 'w') as arq:
        t = 0                                                           # Variavel para cálculo do tempo
        for n in range(250, 2001, 250):
            tempo, soma = 0, 0
            for j in range(500):
                inicio = time.time()                                    # Função para contagem do tempo de execução
                g = RandomTreeRandomWalk(n)                             # Gera 500 árvores com n vértices
                fim = time.time()
                soma += diametro(g)                                     # Calculo dos diâmetros
                tempo += (fim-inicio) 

            print(f'{n} {soma/500}\ttempo: %.2fs' % tempo)
            print(f'{n} {soma/500}', file=arq)                                    # Escreve os resutados no arquivo randomwalk.txt
            t += tempo
        print('tempo total: %.2fs' % t)

if __name__== "__main__" :  
    main()