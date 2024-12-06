grafo = {
    "A": {"B": 4, "C": 2, "D": 7},
    "B": {"A": 4, "C": 1, "E": 1},
    "C": {"A": 2, "B": 1, "D": 3, "E": 3},
    "D": {"A": 7, "C": 3, "E": 2},
    "E": {"B": 1, "C": 3, "D": 2},
}

def dijkstra(grafo, inicio):
    distancias = {no: float("inf") for no in grafo}
    distancias[inicio] = 0
    visitados = set()
    caminhos = {no: None for no in grafo}
    
    while len(visitados) < len(grafo):
        menor_no = None
        menor_distancia = float("inf")
        for no in grafo:
            if no not in visitados and distancias[no] < menor_distancia:
                menor_no = no
                menor_distancia = distancias[no]
        
        if menor_no is None:
            break
        
        visitados.add(menor_no)
        
        for vizinho, peso in grafo[menor_no].items():
            if vizinho not in visitados:
                nova_distancia = distancias[menor_no] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    caminhos[vizinho] = menor_no
    
    return distancias, caminhos

def reconstruir_caminho(caminhos, destino):
    caminho = []
    atual = destino
    while atual:
        caminho.insert(0, atual)
        atual = caminhos[atual]
    return caminho

distancias, caminhos = dijkstra(grafo, "A")

resultado_E = {
    "menor_tempo": distancias["E"],
    "caminho": reconstruir_caminho(caminhos, "E"),
}
resultado_D = {
    "menor_tempo": distancias["D"],
    "caminho": reconstruir_caminho(caminhos, "D"),
}

print("Para a cidade E:")
print("Menor tempo:", resultado_E["menor_tempo"], "horas")
print("Caminho:", " → ".join(resultado_E["caminho"]))

print("\nPara a cidade D:")
print("Menor tempo:", resultado_D["menor_tempo"], "horas")
print("Caminho:", " → ".join(resultado_D["caminho"]))
