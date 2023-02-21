import math, random, time           #math é usado para valores infinitos; random para obter um vértice aleatório em BFS; time para cálculo de tempo
from collections import deque       #deque é uma implementação de fila que funciona em tempo constante

class Grafo(object):
    def __init__(self, vertices): 
        # Declara a matriz de adjacências do grafo e uma lista de arestas
        self.vertices = vertices                                                            # Número de vértices
        self.adj = [[0 for i in range(self.vertices)] for j in range(self.vertices)]        # Matriz de Adjacências de cada vértice
        self.edges = []                                                                     # Lista de arestas do grafo
        
    def initBFS(self):
        # Inicializa listas para o algoritmo BFS
        self.cor = ['B' for i in range(self.vertices)]                                      # Lista de cores de cada vértice
        self.dist = [math.inf for i in range(self.vertices)]                                # Lista de distância de cada vértice
        self.pai = [None for i in range(self.vertices)]                                     # Lista de pai de cada vértice
    
    def initRandomTree(self):
        # Inicializa uma lista para os algoritmos de geração de grafos
        self.visitado = [False for i in range(self.vertices)]                               # Vértice i foi visitado True ou False
        
    def MakeSet(self):
        # Essencialmente cria uma árvore unitária para cada vértice do grafo
        self.pai = [i for i in range(self.vertices)]                                        # Cada vértice se torna pai de si mesmo
        self.rank = [0 for i in range(self.vertices)]                                       # inicializa o limite superior de todos os vértices para 0
    
    def addAresta(self, u, v, w):
        # Adição de uma aresta entre o vértice u e o vértice v
        self.adj[u][v] = 1  
        self.adj[v][u] = 1
        self.edges.append([w, u, v,])

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

    def mostraBFS(self):
        # Mostra caracteristicas dos vértices baseado no algoritimo BFS (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}]')

    
# Busca em largura que define distância dos vértices com relação a um vértice inicial 's'
# Usada para cálculo do diâmetro de uma árvore
def BFS(g, s):                                  
    g.initBFS()               
    g.cor[s] = 'C'                              # Cor do vértice inicial = CINZA
    g.dist[s] = 0                               
    g.pai[s] = None                            
    q = deque()
    q.append(s)                                 # Fila 'q' onde o primeiro vértice será visitado e eliminado da fila e seus vértices filhos serão adicionados ao final da fila
    while q != deque([]):                             
        u = q.popleft()                            
        for v in range(g.vertices):
            if g.adj[u][v] == 1 and g.cor[v] == 'B':                                      
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
    BFS(t, s)                                  
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado porque o grafo não é uma árvore
        raise RuntimeError('not tree')
    a = t.dist.index(max(t.dist))               # A partir de qualquer vértice no grafo, aplicamos BFS e obtemos o vértice mais distante possível e damos a ele o nome de 'a'
    BFS(t, a)                                   # A distância de 'a' até o seu vértice mais distante nos da o diâmetro da árvore 
    return max(t.dist)


# Gera árvores aleatórias de n vértices
# Uma árvore é um grafo acíclico e conexo
def RandomTreeRandomWalk(n):
    g = Grafo(n)
    g.initRandomTree()
    u = random.randint(0, n-1)                                          # Gera um indice aleatório da lista de vértices                           
    g.visitado[u] = True
    count = 0
    while count < n-1:                                                  # Adiciona arestas válidas até que o número de arestas seja n - 1
        v = random.randint(0, n-1)
        if g.visitado[v] == False and g.adj[u][v] == 0 and v != u:
            g.addAresta(u,v,0)
            g.visitado[v] = True
            count += 1
        u = v
    return g


# Cria um grafo CONEXO aleatório de n vértices
def RandomGraph(n):
    g = Grafo(n)
    g.initRandomTree()
    u = random.randint(0, n-1)                                                                     
    g.visitado[u] = True
    while not all(g.visitado):                                                 
        v = random.randint(0, n-1)
        if g.adj[u][v] == 0 and v != u:
            g.addAresta(u,v,0)
            g.visitado[v] = True
        u = v
    return g
    

def Link(g, x, y):
    if g.rank[x] > g.rank[y]:
        g.pai[y] = x
    else:
        g.pai[x] = y
        if g.rank[x] == g.rank[y]:
            g.rank[y] += 1

def FindSet(g, x):
    if x != g.pai[x]:
        g.pai[x] = FindSet(g, g.pai[x])
    return g.pai[x]

def Union(g, x, y):
    Link(g, FindSet(g, x), FindSet(g, y))

def MSTKruskal(g):
    A = []
    g.MakeSet()
    g.edges.sort()
    for e in g.edges:
        if FindSet(g, e[1]) != FindSet(g, e[2]):
            A.append(e)
            Union(g, e[1], e[2])
    return A
    
def RandomTreeKruskal(n):
    g = RandomGraph(n)
    for e in g.edges:
        e[0] = random.random()
    A = MSTKruskal(g)
    h = Grafo(n)
    for edge in A:
        h.addAresta(edge[1], edge[2], edge[0])
    return h
                

def main():
    with open('kruskal.txt', 'w') as arq:
        t = 0                                                           # Variavel para cálculo do tempo
        for n in range(250, 2001, 250):
            tempo, soma = 0, 0
            for j in range(500):
                inicio = time.time()                                    # Função para contagem do tempo de execução
                g = RandomTreeKruskal(n)                             # Gera 500 árvores com n vértices
                fim = time.time()
                soma += diametro(g)                                     # Calculo dos diâmetros
                tempo += (fim-inicio) 

            print(f'{n} {soma/500}\ttempo: %.2fs' % tempo)
            print(f'{n} {soma/500}', file=arq)                          # Escreve os resultados no arquivo randomwalk.txt
            t += tempo
        print('tempo total: %.2fs\t%.2fmin' % (t, t/60))
    

if __name__== "__main__" :  
    main()