import math, random

# Classe que define um objeto do tipo Grafo
class Grafo(object):

    def __init__(self, vertices): 
        # Construtor/Inicializador do grafo
        # Declara uma lista para cada característica do vértice onde um índice i da lista representa um vértice i do grafo
        self.vertices = vertices                            # Número de vértices
        self.ciclico = False                                # Inicializa Grafo como acíclico
        self.adj = [[] for i in range(self.vertices)]       # Lista de Adjacências de cada vértice
        self.cor = [[] for i in range(self.vertices)]       # Lista de cores de cada vértice
        self.dist = [[] for i in range(self.vertices)]      # Lista de distância de cada vértice
        self.pai = [[] for i in range(self.vertices)]       # Lista de pai de cada vértice
        self.desc = [[] for i in range(self.vertices)]      # Lista de tempo de descoberta de cada vértice
        self.termino = [[] for i in range(self.vertices)]   # Lista de tempo de término de cada vértice
    
    def addAresta(self, u, v):
        # Adição de uma aresta entre o vértice u e o vértice v
        self.adj[u].append(v)   # Adiciona v na lista de adjacências de u
        self.adj[v].append(u)   # Adiciona u na lista de adjacências de v
    
    def mostraAdj(self):
        # Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i} => ', end='')               # Mostra vértice i
            for aresta in self.adj[i]:              # Mostra adjacências do vértice i
                print(f'[{aresta}] => ', end='')    
            print('/')                              # Pula Linha

    def mostraBFS(self):
        # Mostra caracteristicas dos vértices baseado no algoritimo BFS (cor, distancia, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, distância = {self.dist[i]}, pai = {self.pai[i]}]')
    
    def mostraDFS(self):
        # Mostra caracteristicas dos vértices baseado no algoritimo DFS (cor, tempo descoberta/término, pai)
        for i in range(self.vertices):
            print(f'vértice {i} : [cor = {self.cor[i]}, descoberta/término = {self.desc[i]}/{self.termino[i]}, pai = {self.pai[i]}]')


def BFS(g, s):                                  # Recebe Grafo g e vértice inicial s
    for u in range(g.vertices):                 # Percorre os vértices do grafo g
        if u != s:                              # Se u é diferente de s, inicializa cor = BRANCO, distância = INFINITO e pai = NULO
            g.cor[u] = 'B'                      
            g.dist[u] = math.inf                
            g.pai[u] = None                    
    g.cor[s] = 'C'                              
    g.dist[s] = 0                               # Inicializa vértice s com cor CINZA, distância 0 e pai NULO
    g.pai[s] = None                            
    q = [s]                                     # Declara uma fila q e insere s
    while q != []:                              # Enquanto fila q não for vazia
        u = q.pop(-1)                           # Retira vértice da fila e guarda ele em u
        for v in g.adj[u]:                      # Para cada v adjacente de u
            if g.cor[v] == 'B':                 # Se v for BRANCO
                g.cor[v] = 'C'                  # Define v como CINZA
                g.dist[v] = g.dist[u] + 1       # Define distancia de v como distancia de u + 1
                g.pai[v] = u                    # Pai de v recebe u
                q.append(v)                     # Adiciona vértice v na fila q
        g.cor[u] = 'P'                          # Define cor de u como PRETO


# Algoritimo de busca em profundidade usado para verificar se um grafo é uma árvore
def DFS(g):                                     # Recebe o grafo g
    for u in range(g.vertices):                 # Para cada vértice u de g defina cor = BRANCO e pai = NULO
        g.cor[u] = 'B'
        g.pai[u] = None
    tempo = 0                                   # Inicializa contagem de tempo em zero
    for u in range(g.vertices):                 # Visita cada vértice branco restante no grafo
        if g.cor[u] == 'B':
            tempo = DFSVisit(g, u, tempo)
def DFSVisit(g, u, tempo):
    tempo += 1
    g.desc[u] = tempo                           # Tempo de descoberta do vértice visitado u recebe tempo
    g.cor[u] = 'C'                              # Cor do vértice visitado u recebe CINZA
    for v in g.adj[u]:                          # Para cada v adjacente de u:
        if g.cor[v] == 'B':                     # Se v é BRANCO defina pai como u e visite v
            g.pai[v] = u
            tempo = DFSVisit(g, v, tempo)
        elif v != g.pai[u]:                     # Se v não é BRANCO e v não é pai de u, então o grafo é cíclico
            g.ciclico = True
    g.cor[u] = 'P'                              # Cor de u recebe PRETO
    tempo += 1
    g.termino[u] = tempo                        # Tempo de término de u recebe tempo
    return tempo                                # Retorna tempo para que a variavel tempo seja atualizada na função anterior


# Algoritimo que verifica se um grafo g é uma árvore ou não
# Se o número de vértices com pai = NULO for maior do que 1 após a execução do DFS, então o grafo NÃO É CONEXO
# Um grafo só é considerado árvore se for CONEXO e ACÍCLICO
def isTree(g):
    DFS(g)                                      # Aplica DFS em g
    count = 0                                   # Inicializa um contador em 0
    for u in range(g.vertices):                 # Para cada vértice u de g:
        if g.pai[u] == None:                    
            count += 1                          # Se pai de u for igual a NULO, adiciona 1 ao contador
    if g.ciclico == False and count < 2:        # Se g é acíclico e contador de vértices com pai = NULO é menor que 2: retorna verdadeiro
        return True                          
    else:                                       
        return False


# Algoritimo para cálculo do diâmetro de uma árvore
def diametro(t):
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado e retorna -1
        return -1
    s = random.randint(0, t.vertices-1)         # s recebe um vértice aleatório de t
    BFS(t, s)                                   # Aplica BFS em t com vértice inicial s
    a = t.dist.index(max(t.dist))               # a recebe o vértice com o máximo valor de distância
    BFS(t, a)                                   # Aplica BFS em t com vértice inicial a
    return max(t.dist)                          # Retorna a distância do vértice mais distante de a


def main():
    '''
    Representação do grafo de exemplo 1:
    0---1   2---3 
    |   |  ̷  |  ̷  |
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
    assert len (g.desc) == 8
    assert len (g.termino) == 8
    
    # Assert para addAresta e mostraAdj
    assert g.adj[0] == [1,4] #pode ser outra lista, depende da ordem em que as arestas foram adicionadas
    assert g.adj[1] == [0,5] 
    assert g.adj[2] == [5,6,3] 
    assert g.adj[3] == [2,6,7] 
    assert g.adj[4] == [0] 
    assert g.adj[5] == [1,2,6] 
    assert g.adj[6] == [2,3,5,7] 
    assert g.adj[7] == [3,6]
    
    # Assert para BFS
    BFS(g, 0)
    assert g.cor[0] == 'P'                      
    assert g.dist[7] == 4                 
    assert g.pai[4] == 0
    
    # Assert para DFS e DFSVisit
    DFS(g)
    assert g.cor[7] == 'P'
    assert g.pai[5] == 1
    assert g.desc[4] == 14 #pode ser 2, mas depende da ordem em que as arestas foram adicionadas
    assert g.termino[3] == 9 #pode ser 6 ou 7, mas depende da ordem em que as arestas foram adicionadas
    assert g.ciclico == True
    
    # Assert para isTree
    assert isTree(g) == False
    
    #Assert para diametro
    assert diametro(g) == -1
    
    '''
    Representação do grafo de exemplo 2:
    0   1---2   3---4   5   6---7   8
     - Acíclico
     - Desconexo
    '''
    # Contrução do grafo
    h = Grafo(9)
    h.addAresta(1,2)
    h.addAresta(3,4)
    h.addAresta(6,7)
    
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
    i.addAresta(2,3)
    i.addAresta(4,5)
    i.addAresta(4,6)
    
    '''
    Representação do grafo de exemplo 4:
    0---1---2---3---4
	    |
            5---6---7
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
    
    # Assert para isTree
    assert isTree(j) == True
    
    # Assert para diametro
    assert diametro(j) == 5

    # Exemplo de função que imprime lista de adjacência
    j.mostraAdj()
    # Exemplo de função que mostra características com base no algoritimo BFS
    j.mostraBFS()
    print()
    DFS(j)
    # Exemplo de função que mostra características com base no algoritimo DFS
    j.mostraDFS()


if __name__== "__main__" :  
    main()
