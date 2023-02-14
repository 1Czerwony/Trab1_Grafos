import math, random, time           #math é usado para valores infinitos; random para obter um vértice aleatório em BFS
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
    s = random.randint(0, t.vertices-1)         
    BFS(t, s)                                  
    if not isTree(t):                           # Se isTree(t) é falso então o algoritimo não é executado porque o grafo não é uma árvore
        raise ValueError('Not tree')
    a = t.dist.index(max(t.dist))               # A partir de qualquer vértice no grafo, aplicamos BFS e obtemos o vértice mais distante possível e damos a ele o nome de 'a'
    BFS(t, a)                                   # A distância de 'a' até o seu vértice mais distante nos da o diâmetro da árvore 
    return max(t.dist)


def RandomTreeRandomWalk(n):
    g = Grafo(n)
    for u in range(n):
        g.visitado[u] = False
    u = random.randint(0, n-1)
    g.visitado[u] = True
    count = 0
    while count < n-1:
        v = random.randint(0, n-1)
        if g.visitado[v] == False and v not in g.adj[u] and v != u:
            g.addAresta(u,v)
            g.visitado[v] = True
            count += 1
        u = v
    return g

def main():
    with open('randomwalk.txt', 'w') as arq:
        n = 250
        soma = 0
        for i in range(8):
            inicio = time.time()
            for j in range(500):
                g = RandomTreeRandomWalk(n)
                soma += diametro(g)
            fim = time.time()
            print(f'{n} {soma/500}\ttempo: %.2fs' % (fim-inicio))
            print(f'{n} {soma/500}', file=arq)
            n += 250



if __name__== "__main__" :  
    main()