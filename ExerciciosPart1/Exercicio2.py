def retorna_transposto(MA, n):
    LA = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if MA[u][v]:
                LA[v].append(u)
    return LA

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        print("Nenhuma entrada lida")
        return

    dados = list(map(int, input_data))
    idx = 0
    while idx < len(dados):
        n = dados[idx]
        idx += 1
        m = dados[idx]
        idx += 1
        MA = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u = dados[idx]
            v = dados[idx + 1]
            idx += 2
            MA[u][v] = 1
        LA = retorna_transposto(MA, n)
        for u in range(n):
            print(f"{u}:", end=" ")
            for v in LA[u]:
                print(v, end=" ")
            print()
        print()
        
if __name__ == "__main__":
    main()
