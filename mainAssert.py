import math, random

class Grafo(object):

    def __init__(self, vertices): 
        # Declara uma lista para cada característica do vértice onde um índice i da lista representa um vértice i do grafo
        self.vertices = vertices                            # Número de vértices
        self.adj = [[] for i in range(self.vertices)]       # Lista de Adjacências de cada vértice
        self.cor = [[] for i in range(self.vertices)]       # Lista de cores de cada vértice
        self.dist = [[] for i in range(self.vertices)]      # Lista de distância de cada vértice
        self.pai = [[] for i in range(self.vertices)]       # Lista de pai de cada vértice
        self.desc = [[] for i in range(self.vertices)]      # Lista de tempo de descoberta de cada vértice
        self.termino = [[] for i in range(self.vertices)]   # Lista de tempo de término de cada vértice
    
    def addAresta(self, u, v):
        # Adição de uma aresta entre o vértice u e o vértice v
        self.adj[u].append(v)   
        self.adj[v].append(u)   
    
    def mostraAdj(self):
        # Mostra lista de adjacências
        for i in range(self.vertices):
            print(f'{i} => ', end='')               
            for aresta in self.adj[i]:              
                print(f'[{aresta}] => ', end='')    
            print('/')                              

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
    q = [s]                                     # Fila 'q' onde o primeiro vértice será visitado e eliminado da fila e seus vértices filhos serão adicionados ao final da fila
    while q != []:                              
        u = q.pop(0)                            
        for v in g.adj[u]:                      
            if g.cor[v] == 'B':                 
                g.cor[v] = 'C'                  
                g.dist[v] = g.dist[u] + 1       # Vértices descobertos recebem a distância de seu pai + 1
                g.pai[v] = u                    
                q.append(v)                     
        g.cor[u] = 'P'                          # Define cor de u como PRETO


# Retorna True se o grafo é CÍCLICO e False se é ACÍCLICO
def isCyclic(g):
    arestas = 0
    for u in g.adj:                             # Soma todas as adjacências do grafo e as divide por 2, isto nos da o numero de arestas do grafo
        arestas += len(u)                       
    arestas = arestas/2
    if arestas > (g.vertices-1):                # Se o número de arestas do grafo é maior do que o número de vértices + 1, então o grafo é CÍCLICO, senão é ACÍCLICO
        return True
    else:
        return False


# Se o grafo é uma árvore retorna TRUE, senão retorna FALSE
def isTree(g):                              
    count = 0
    for u in range(g.vertices):                 # Se o número de vértices com pai = NULO for maior do que 1 após a execução do BFS, então o grafo NÃO É CONEXO
        if g.pai[u] == None:                    
            count += 1                         
    if not isCyclic(g) and count < 2:           # Retorna TRUE somente se g for CONEXO e ACÍCLICO
        return True                          
    else:                                       
        return False


# Calcula o diâmetro de uma árvore t
# O diâmetro de uma árvore é o caminho mais longo possível entre dois vértices
def diametro(t):
    s = random.randint(0, t.vertices-1)         
    BFS(t, s)                                  
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado porque o grafo não é uma árvore
        return -1
    a = t.dist.index(max(t.dist))               # A partir de qualquer vértice no grafo, aplicamos BFS e obtemos o vértice mais distante possível e damos a ele o nome de 'a'
    BFS(t, a)                                   # A distância de 'a' até o seu vértice mais distante nos da o diâmetro da árvore 
    return max(t.dist)                          


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
    assert len (g.desc) == 8
    assert len (g.termino) == 8
    
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
    BFS(g, 0)
    assert g.cor[0] == 'P'                      
    assert g.dist[7] == 4                 
    assert g.pai[4] == 0
    
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
    
    # Assert para isTree
    assert isTree(j) == True
    
    # Assert para diametro
    assert diametro(j) == 5

    # Exemplo de função que imprime lista de adjacência
    #j.mostraAdj()
    # Exemplo de função que mostra características com base no algoritimo BFS
    #j.mostraBFS()


if __name__== "__main__" :  
    main()