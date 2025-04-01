import random

def retorna_grau(LA, n, u):
    """
    Calcula o grau de entrada e de saída do vértice u em um grafo direcionado.

    Parâmetros:
      LA : lista de listas
           Representa a lista de adjacências do grafo, onde LA[i] contém os vértices adjacentes (destinos) de i.
      n : int
          Número total de vértices no grafo.
      u : int
          Vértice para o qual os graus serão calculados.

    Retorna:
      tuple (grau_entrada, grau_saida)
        - grau_entrada: número de vértices que possuem pelo menos uma aresta apontando para u.
        - grau_saida: número de arestas que saem do vértice u.
    """
    grau_saida = len(LA[u])
    grau_entrada = 0
    for i in range(n):
        if u in LA[i]:
            grau_entrada += 1
    return grau_entrada, grau_saida

def main():
    """
    Lê os casos de teste a partir do terminal. Cada caso de teste inicia com uma linha contendo
    n (número de vértices) e m (número de arestas). Em seguida, m linhas com as arestas no formato:
    u v
    (representando uma aresta de u para v). Ao final de cada caso, escolhe aleatoriamente um vértice
    e imprime: vértice, grau de entrada e grau de saída.
    """
    while True:
        try:
            linha = input().strip()
            if not linha:
                continue  
            n, m = map(int, linha.split())
        except EOFError:
            break
        except Exception as e:
            print("erro na leitura de n e m:", e)
            break

        LA = [[] for _ in range(n)]
        
        for _ in range(m):
            try:
                u, v = map(int, input().split())
            except Exception as e:
                print("erro na leitura das arestas:", e)
                return
            LA[u].append(v)
        
        vertice = random.randrange(n)
        grau_entrada, grau_saida = retorna_grau(LA, n, vertice)
        print(f"{vertice} {grau_entrada} {grau_saida}")

if __name__ == "__main__":
    main()
