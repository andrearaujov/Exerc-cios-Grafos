from collections import deque

def bfs(grafo, origem, destino, pai):
    """
    Implementa BFS para encontrar um caminho de aumento no grafo residual.
    """
    n = len(grafo)
    visitado = [False] * n
    
    fila = deque([origem])
    visitado[origem] = True
    
    while fila:
        u = fila.popleft()
        
        for v in range(n):
            if not visitado[v] and grafo[u][v] > 0:
                fila.append(v)
                visitado[v] = True
                pai[v] = u
    
    return visitado[destino]

def edmonds_karp(grafo, origem, destino):
    n = len(grafo)
    pai = [-1] * n
    fluxo_maximo = 0
    
    # Criar uma cópia do grafo para trabalhar com o grafo residual
    grafo_residual = [row[:] for row in grafo]
    
    # Enquanto existir um caminho de aumento
    while bfs(grafo_residual, origem, destino, pai):
        # Encontrar a capacidade residual mínima ao longo do caminho
        caminho_fluxo = float('inf')
        s = destino
        while s != origem:
            caminho_fluxo = min(caminho_fluxo, grafo_residual[pai[s]][s])
            s = pai[s]
        
        # Atualizar as capacidades residuais
        fluxo_maximo += caminho_fluxo
        v = destino
        while v != origem:
            u = pai[v]
            grafo_residual[u][v] -= caminho_fluxo
            grafo_residual[v][u] += caminho_fluxo
            v = pai[v]
    
    return fluxo_maximo

def construir_grafo_com_divisao_nos(num_controladores, capacidades_controladores, ligacoes, sucessores_origem, predecessores_destino):
   
    n = 2 * num_controladores + 2
    grafo = [[0] * n for _ in range(n)]
    
    for i in range(1, num_controladores + 1):
      
        grafo[2*i - 1][2*i] = capacidades_controladores[i - 1]
    
    for u, v, p in ligacoes:
        grafo[2*u][2*v - 1] = p
    
    for u in sucessores_origem:
        grafo[0][2*u - 1] = float('inf')  # Capacidade infinita da origem para os sucessores
    
    for u in predecessores_destino:
        grafo[2*u][2*num_controladores + 1] = float('inf')  # Capacidade infinita dos predecessores para o destino
    
    return grafo

def main():
  
    try:
        while True:
            linha = input().strip()
            if linha == "-1":
                break
            
            num_controladores = int(linha)
            
            capacidades_controladores = list(map(int, input().split()))
            
            num_ligacoes = int(input())
            
            ligacoes = []
            for _ in range(num_ligacoes):
                u, v, p = map(int, input().split())
                ligacoes.append((u, v, p))
            
            e, s = map(int, input().split())
            
            controladores = list(map(int, input().split()))
            sucessores_origem = controladores[:e]
            predecessores_destino = controladores[e:]
            
            grafo = construir_grafo_com_divisao_nos(num_controladores, capacidades_controladores, ligacoes, sucessores_origem, predecessores_destino)
            
            # Calcular fluxo máximo
            origem = 0
            destino = 2 * num_controladores + 1
            fluxo_maximo = edmonds_karp(grafo, origem, destino)
            
            # Imprimir resultado
            print(fluxo_maximo)
    except EOFError:
        pass 

if __name__ == "__main__":
    main()
