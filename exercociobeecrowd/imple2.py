"""
Delta City - Solução para o problema de pedágios
Implementação do algoritmo para encontrar o maior pedágio em um caminho
da origem ao destino, respeitando o limite de custo total.
"""
from collections import deque

def construir_grafo(n, arestas):
  
    grafo = [[] for _ in range(n + 1)]  # +1 porque os nós são numerados de 1 a n
    
    for u, v, w in arestas:
        grafo[u].append((v, w))  # Adiciona aresta direcionada (u -> v) com custo w
        
    return grafo

def encontrar_maior_pedagio(grafo, origem, destino, custo_max):
    
    fila = deque([(origem, 0, 0)])  # (nó, custo_acumulado, maior_pedagio)
    visitados = set()
    maior_pedagio_encontrado = -1
    
    while fila:
        no_atual, custo_atual, maior_pedagio_atual = fila.popleft()
        
        if no_atual == destino:
            maior_pedagio_encontrado = max(maior_pedagio_encontrado, maior_pedagio_atual)
            continue
            
        estado = (no_atual, maior_pedagio_atual)
        if estado in visitados:
            continue
            
        visitados.add(estado)
        
        for vizinho, pedagio in grafo[no_atual]:
            novo_custo_total = custo_atual + pedagio
            
            if novo_custo_total <= custo_max:
                novo_maior_pedagio = max(maior_pedagio_atual, pedagio)
                fila.append((vizinho, novo_custo_total, novo_maior_pedagio))
    
    return maior_pedagio_encontrado

def resolver_caso(n, m, s, t, c, arestas):
   
    grafo = construir_grafo(n, arestas)
    
    # Encontra o maior pedágio no caminho escolhido
    resultado = encontrar_maior_pedagio(grafo, s, t, c)
    
    return resultado

def principal():
   
    num_casos = int(input().strip())
    
    for _ in range(num_casos):
        n, m, s, t, c = map(int, input().strip().split())
        
        arestas = []
        for _ in range(m):
            u, v, w = map(int, input().strip().split())
            arestas.append((u, v, w))
        
        resultado = resolver_caso(n, m, s, t, c, arestas)
        print(resultado)

if __name__ == "__main__":
    principal()
