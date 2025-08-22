grafo = {'inicio' : {'A' : 6, 'B' : 2},'A' : {'final' : 1},'final' : {}, 'B' : {'final' : 5,'A' : 3}}

infinito = float('inf')
pesos = {'A' : 6, 'B' : 2, 'final' : infinito}
pais = {'A' : 'inicio', 'B' : 'inicio', 'final' : None}
processados = []

def custo_mais_baixo(pesos):
    menor = float('inf')
    escolha = None
    for chave,item in pesos.items():
        if item < menor and chave not in processados:
            menor = item
            escolha = chave
    return escolha

no = custo_mais_baixo(pesos)
while no is not None:
    peso = pesos[no]
    vizinhos = grafo[no]
    for item in vizinhos.keys():
        novo_peso = peso + vizinhos[item]
        if pesos[item] > novo_peso:
            pesos[item] = novo_peso
            pais[item] = no
    processados.append(no)
    no = custo_mais_baixo(pesos)

caminho = sorted(pais.values(),reverse=True)
print(caminho)

