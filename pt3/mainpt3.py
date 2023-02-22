import math, random, time           #math é usado para valores infinitos; random para obter um vértice aleatório em BFS; time para cálculo de tempo
from collections import deque       #deque é uma implementação de fila que funciona em tempo constante

class Grafo(object):
    def __init__(self, vertices): 
        # Declara a matriz de adjacências do grafo e uma lista de arestas
        self.vertices = vertices                                                            # Número de vértices
        self.edges = []                                                                     # Lista de arestas do grafo
        
    def initBFS(self):
        # Inicializa listas para o algoritmo BFS
        self.cor = ['B' for i in range(self.vertices)]                                      # Lista de cores de cada vértice
        self.dist = [math.inf for i in range(self.vertices)]                                # Lista de distância de cada vértice
        self.pai = [None for i in range(self.vertices)]                                     # Lista de pai de cada vértice
    
    def initRandom(self):
        # Inicializa uma lista para os algoritmos de geração de grafos
        self.visitado = [False for i in range(self.vertices)]                               # Vértice i foi visitado True ou False
        
    def MakeSet(self):
        # Essencialmente cria uma árvore unitária para cada vértice do grafo
        self.pai = [i for i in range(self.vertices)]                                        # Cada vértice se torna pai de si mesmo
        self.rank = [0 for i in range(self.vertices)]                                       # rank se refere ao posto em que o vértice da árvore está
    
    # Método para teste de BFS
    def mostraBFS(self):
        # Mostra caracteristicas dos vértices baseado no algoritimo BFS (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}]')

# Subclasse de Grafo que executa com lista de adjacências
class Lista(Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.adj = [[] for i in range(vertices)]            # Lista de Adjacências de cada vértice
    
    # Busca em largura que define distância dos vértices com relação a um vértice inicial 's'
    # Usada para cálculo do diâmetro de uma árvore
    def BFS(self, s):
        self.initBFS()                                      # Inicializa os atributos para que o algoritmo funcione               
        self.cor[s] = 'C'                                   # Cor do vértice inicial = CINZA
        self.dist[s] = 0                               
        self.pai[s] = None                            
        q = deque()
        q.append(s)                                         # Fila 'q' onde o primeiro vértice será visitado e eliminado da fila e seus vértices filhos serão adicionados ao final da fila
        while q != deque([]):                             
            u = q.popleft()                            
            for v in self.adj[u]:
                if self.cor[v] == 'B':                                      
                    self.cor[v] = 'C'                  
                    self.dist[v] = self.dist[u] + 1         # Vértices descobertos recebem a distância de seu pai + 1
                    self.pai[v] = u                    
                    q.append(v)                     
            self.cor[u] = 'P'                               # Define cor de u como PRETO
            
    def addAresta(self, u, v, w):
        # Adição de uma aresta entre o vértice u e o vértice v, com peso w
        self.adj[u].append(v)  
        self.adj[v].append(u)
        self.edges.append([w, u, v,])                       # Cada aresta do grafo é representada por uma lista da forma [peso, u, v]
    
    # Método para teste de lista de adjacências
    def mostraAdj(self):
        # Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i} => ', end='')               
            for aresta in self.adj[i]:            
                print(f'[{aresta}] => ', end='')    
            print('/')                              

# Subclasse de Grafo que executa com matriz de adjacências
class Matriz(Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.adj = [[0 for i in range(self.vertices)] for j in range(self.vertices)]        # Matriz de Adjacências de cada vértice
    
    # Busca em largura que define distância dos vértices com relação a um vértice inicial 's'
    # Usada para cálculo do diâmetro de uma árvore
    def BFS(self, s):
        self.initBFS()                                      # Inicializa os atributos para que o algoritmo funcione 
        self.cor[s] = 'C'                                   # Cor do vértice inicial = CINZA
        self.dist[s] = 0                               
        self.pai[s] = None                            
        q = deque()
        q.append(s)                                         # Fila 'q' onde o primeiro vértice será visitado e eliminado da fila e seus vértices filhos serão adicionados ao final da fila
        while q != deque([]):                             
            u = q.popleft()                            
            for v in range(self.vertices):
                if self.adj[u][v] == 1 and self.cor[v] == 'B':                                      
                    self.cor[v] = 'C'                  
                    self.dist[v] = self.dist[u] + 1         # Vértices descobertos recebem a distância de seu pai + 1
                    self.pai[v] = u                    
                    q.append(v)                     
            self.cor[u] = 'P'                               # Define cor de u como PRETO
            
    def addAresta(self, u, v, w):
        # Adição de uma aresta entre o vértice u e o vértice v, com peso w
        self.adj[u][v] = 1 
        self.adj[v][u] = 1
        self.edges.append([w, u, v,])                       # Cada aresta do grafo é representada por uma lista da forma [peso, u, v]
    
    # \/\/\/\/ Método para teste de matriz de adjacências \/\/\/\/
    def mostraAdj(self):
        # Mostra matriz de adjacências
        print('    ', end='')
        for i in range(self.vertices):
            print(f'{i}  ', end='')
        print('\n')
        for i in range(self.vertices):
            print(f'{i}   ', end='')               
            for j in range(self.vertices):              
                print(f'{self.adj[i][j]}  ', end='')    
            print()     
        
# Se o grafo é uma árvore retorna TRUE, senão retorna FALSE
# Retorna True se o grafo é CONEXO e ACÍCLICO
def isTree(g): 
    # Verifica se é CONEXO                             
    count = 0
    for u in range(g.vertices):                         # Se o número de vértices com pai = NULO for maior do que 1 após a execução do BFS, então o grafo NÃO É CONEXO
        if g.pai[u] == None:                    
            count += 1                         
        if count > 1:                                   # Retorna FALSE se o grafo é DESCONEXO
            return False
    # Se é CONEXO então verifica se é ACÍCLICO                                                
    if len(g.edges) > (g.vertices-1):                   # Se o número de arestas do grafo é maior do que o número de vértices + 1, então o grafo é CÍCLICO, senão é ACÍCLICO
        return False
    else:
        return True


# Calcula o diâmetro de uma árvore t
# O diâmetro de uma árvore é o caminho mais longo possível entre dois vértices
def diametro(t):
    s = random.randint(0, t.vertices-1)     	# Gera um indice aleatório da lista de vértices
    t.BFS(s)                                  
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado porque o grafo não é uma árvore
        return -1
    a = t.dist.index(max(t.dist))               # A partir de qualquer vértice no grafo, aplicamos BFS e obtemos o vértice mais distante possível e damos a ele o nome de 'a'
    t.BFS(a)                                   # A distância de 'a' até o seu vértice mais distante nos da o diâmetro da árvore 
    return max(t.dist)


# Gera árvores aleatórias de n vértices
# Uma árvore é um grafo acíclico e conexo
def RandomTreeRandomWalk(n):
    g = Lista(n)
    g.initRandom()
    u = random.randint(0, n-1)                                          # Gera um indice aleatório da lista de vértices                           
    g.visitado[u] = True
    count = 0
    while count < n-1:                                                  # Adiciona arestas válidas até que o número de arestas seja n - 1
        v = random.randint(0, n-1)
        if g.visitado[v] == False and v not in g.adj[u] and v != u:
            g.addAresta(u,v,0)
            g.visitado[v] = True
            count += 1
        u = v
    return g


# Cria um grafo CONEXO aleatório de n vértices
def RandomGraph(n):
    g = Matriz(n)
    g.initRandom()
    u = random.randint(0, n-1)                                                                     
    g.visitado[u] = True
    while not all(g.visitado):                                                 
        v = random.randint(0, n-1)
        if g.adj[u][v] == 0 and v != u:
            g.addAresta(u,v,0)
            g.visitado[v] = True
        u = v
    return g
    
    
# Insere a árvore com raiz de menor rank na árvore com raiz de maior rank
# Se a raiz das 2 árvores possuírem o mesmo valor de rank, uma delas é arbitrariamente escolhida para ser pai da outra
def Link(g, x, y):
    if g.rank[x] > g.rank[y]:
        g.pai[y] = x
    else:
        g.pai[x] = y
        if g.rank[x] == g.rank[y]:  
            g.rank[y] += 1
            
# Localiza a raiz de uma árvore a partir de um nó x
def FindSet(g, x):
    if x != g.pai[x]:
        g.pai[x] = FindSet(g, g.pai[x])
    return g.pai[x]

# União de duas árvores encontrando a raiz de cada uma
def Union(g, x, y):
    Link(g, FindSet(g, x), FindSet(g, y))

# Retorna uma lista arestas que compõem a árvore geradora mínima de um grafo g
def MSTKruskal(g):
    A = []
    g.MakeSet()                                     # Atribui uma árvore unitária para cada vértice
    g.edges.sort()                                  # Ordena as arestas do grafo em ordem crescente de peso
    for e in g.edges:
        if FindSet(g, e[1]) != FindSet(g, e[2]):
            A.append(e)
            Union(g, e[1], e[2])
    return A

# Gera um grafo aleatório e devolve a árvore geradora mínima deste grafo obtida a partir do algoritmo de Kruskal
def RandomTreeKruskal(n):
    g = RandomGraph(n)                              
    for e in g.edges:
        e[0] = random.random()                      # Gera um valor de peso aleatório entre 1 e 0 para cada uma das arestas do grafo
    A = MSTKruskal(g)
    h = Matriz(n)
    for edge in A:                                  # Monta um grafo h usando a lista de arestas obtidas do algoritmo de Kruskal
        h.addAresta(edge[1], edge[2], edge[0])
    return h
                

def main():
    '''
    Representação do grafo de exemplo 1:
    0---1   2---3 
    |   | ̷  | ̷  |
    4   5---6---7
     - Cíclico
     - Conexo
    '''
    # Construção do grafo com MATRIZ
    g = Matriz(8)
    g.addAresta(0,1,0)
    g.addAresta(0,4,0)
    g.addAresta(1,5,0)
    g.addAresta(2,5,0)
    g.addAresta(2,6,0)
    g.addAresta(2,3,0)
    g.addAresta(3,6,0)
    g.addAresta(3,7,0)
    g.addAresta(5,6,0)
    g.addAresta(6,7,0)
    
    # Assert para __init__
    assert g.vertices == 8
    assert len(g.adj) == 8
    assert len(g.edges) == 10

    #Assert para addAresta
    assert g.adj == [[0,1,0,0,1,0,0,0],
                     [1,0,0,0,0,1,0,0],
                     [0,0,0,1,0,1,1,0],
                     [0,0,1,0,0,0,1,1],
                     [1,0,0,0,0,0,0,0],
                     [0,1,1,0,0,0,1,0],
                     [0,0,1,1,0,1,0,1],
                     [0,0,0,1,0,0,1,0]]
    for e in g.edges:
        assert e[0] == 0
    
    # Assert para BFS
    g.BFS(1)
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
    # Construção do grafo com MATRIZ
    h = Matriz(8)
    h.addAresta(1,2,1)
    h.addAresta(3,4,1)
    h.addAresta(6,7,1)
    
    # Assert para __init__
    assert h.vertices == 8
    assert len(h.adj) == 8
    assert len(h.edges) == 3
    
    # Assert para addAresta
    assert h.adj == [[0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,0,0,0],
                     [0,1,0,0,0,0,0,0],
                     [0,0,0,0,1,0,0,0],
                     [0,0,0,1,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,1],
                     [0,0,0,0,0,0,1,0]]
    for e in h.edges:
        assert e[0] == 1
    
    # Assert para BFS
    h.BFS(0) 
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
    
    # Assert para isTree
    assert isTree(g) == False
    
    #Assert para diametro
    assert diametro(g) == -1
    
    '''
    Representação do grafo de exemplo 4:
    0---1---2---3---4
	      ̷  |
        8   5---6---7
     - Acíclico
     - Conexo
    '''
    # Construção do grafo com LISTA
    j = Lista(9)
    j.addAresta(0,1,2)
    j.addAresta(1,2,2)
    j.addAresta(2,3,2)
    j.addAresta(2,5,2)
    j.addAresta(2,8,2)
    j.addAresta(3,4,2)
    j.addAresta(5,6,2)
    j.addAresta(6,7,2)
    
    # Assert para __init__
    assert j.adj[0] == [1]
    assert j.adj[1] == [0,2]
    assert j.adj[2] == [1,3,5,8]
    assert j.adj[3] == [2,4]
    assert j.adj[4] == [3]
    assert j.adj[5] == [2,6]
    assert j.adj[6] == [5,7]
    assert j.adj[7] == [6]
    assert j.adj[8] == [2]
    for e in j.edges:
        assert e[0] == 2
    
    # Assert para BFS
    j.BFS(8)
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
    
    # \/\/\/\/\/ Testes \/\/\/\/\/
    
    print("\/\/\/\/\/ Teste RandomTreeRandomWalk \/\/\/\/\/")
    with open('randomwalk.txt', 'w') as arq:
        t = 0                                                           # Variavel para cálculo do tempo total
        for n in range(250, 2001, 250):
            tempo, soma = 0, 0                                          # tempo = variavel de cálculo do tempo de geração de cada árvore
            for j in range(500):                                        # Gera 500 árvores com n vértices até n = 2000
                inicio = time.time()                                    # Função para contagem do tempo de execução
                g = RandomTreeRandomWalk(n)                             
                g.BFS(0)
                assert isTree(g) == True
                fim = time.time()
                soma += diametro(g)                                     # Calculo dos diâmetros
                tempo += (fim-inicio) 

            print(f'{n} {soma/500}\ttempo: %.2fs' % tempo)
            print(f'{n} {soma/500}', file=arq)                          # Escreve os resultados no arquivo randomwalk.txt
            t += tempo
        print('tempo total: %.2fs' % t)
    
    print()
    print("\/\/\/\/\/ Teste RandomTreeKruskal \/\/\/\/\/")
    with open('kruskal.txt', 'w') as arq:
        t = 0                                                           # Variavel para cálculo do tempo total
        for n in range(250, 2001, 250):                                 
            tempo, soma = 0, 0                                          # tempo = variavel de cálculo do tempo de geração de cada árvore
            for j in range(500):                                        # Gera 500 árvores com n vértices até n = 2000
                inicio = time.time()                                    # Função para contagem do tempo de execução
                g = RandomTreeKruskal(n)                              
                g.BFS(0)
                assert isTree(g) == True
                fim = time.time()
                soma += diametro(g)                                     # Calculo dos diâmetros
                tempo += (fim-inicio) 

            print(f'{n} {soma/500}\ttempo: %.2fs' % tempo)
            print(f'{n} {soma/500}', file=arq)                          # Escreve os resultados no arquivo kruskal.txt
            t += tempo
        print('tempo total: %.2fs\t%.2fmin' % (t, t/60))
    

if __name__== "__main__" :  
    main()