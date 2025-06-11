"""
Solução para o problema dos presentes do Papai Noel.
O programa calcula quantos presentes distintos o Papai Noel terá que entregar
no caminho entre duas casas escolhidas.
"""
from collections import deque

def encontrar_caminho(grafo, inicio, fim):
    visitados = [False] * len(grafo)
    pai = [-1] * len(grafo)
    
    # BFS para encontrar o caminho
    fila = deque([inicio])
    visitados[inicio] = True
    
    while fila:
        no_atual = fila.popleft()
        
        if no_atual == fim:
            break
            
        for vizinho in grafo[no_atual]:
            if not visitados[vizinho]:
                visitados[vizinho] = True
                pai[vizinho] = no_atual
                fila.append(vizinho)
    
    caminho = []
    no_atual = fim
    
    while no_atual != -1:
        caminho.append(no_atual)
        no_atual = pai[no_atual]
        
    return caminho[::-1]  # Inverter para obter o caminho de inicio até fim

def contar_presentes_distintos(caminho, presentes):
   
    presentes_distintos = set()
    
    for casa in caminho:
        presentes_distintos.add(presentes[casa - 1])  
    return len(presentes_distintos)

def main():
    """
    Função principal que lê a entrada e processa as consultas.
    """
    n, m = map(int, input().split())
    presentes = input().split()
    
    grafo = [[] for _ in range(n + 1)] 
    for _ in range(n - 1):
        a, b = map(int, input().split())
        grafo[a].append(b)
        grafo[b].append(a) 
        
    for _ in range(m):
        a, b = map(int, input().split())
        caminho = encontrar_caminho(grafo, a, b)
        resultado = contar_presentes_distintos(caminho, presentes)
        print(resultado)

if __name__ == "__main__":
    main()
