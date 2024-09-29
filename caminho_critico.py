def encontrar_caminho_critico_bellman_ford(grafo, duracoes, materias):
    """
    Encontra o caminho crítico utilizando o algoritmo de Bellman-Ford.

    :param grafo: O grafo de materias, onde cada chave é uma matéria e o valor é uma lista de matérias que dependem dela.
    :param duracoes: Dicionário com a duração de cada materia.
    :param materias: Lista de todas as materias.
    :return: Caminho crítico (lista de matérias) e o tempo mínimo para completar o projeto.
    """

    # Inicializa distâncias e predecessores
    distancias = {materia: float('-inf') for materia in materias}  # Distância máxima até cada matéria (inicialmente -infinito)
    predecessores = {materia: None for materia in materias}  # Predecessor de cada matéria no caminho crítico

    # Define a distância inicial (s) como 0 (representando o início do projeto)
    distancias['s'] = 0

    # Relaxamento das arestas (itera |V|-1 vezes para garantir a convergência)
    for _ in range(len(materias) - 1):
        for materia in materias:
            if materia not in grafo:  # Ignora matérias sem dependências
                continue
            for proxima in grafo[materia]:  # Para cada matéria dependente da matéria atual
                if proxima in duracoes:  # Verifica se a próxima matéria tem duração definida
                    if distancias[materia] + duracoes[proxima] > distancias[proxima]:
                        distancias[proxima] = distancias[materia] + duracoes[proxima]  # Atualiza a distância máxima
                        predecessores[proxima] = materia  # Atualiza o predecessor no caminho crítico

    # Encontra a maior distância e reconstrói o caminho crítico
    max_dist = float('-inf')
    materia_final = None

    for materia, distancia in distancias.items():
        if distancia > max_dist:
            max_dist = distancia  # Encontra a maior distância (duração do caminho crítico)
            materia_final = materia  # Encontra a matéria final do projeto

    # Reconstrói o caminho crítico a partir da matéria final
    caminho_critico = []
    while materia_final:
        caminho_critico.append(materia_final)
        materia_final = predecessores[materia_final]

    caminho_critico.reverse()  # Inverte para ter a ordem correta (do início ao fim)
    return caminho_critico, max_dist

def exibir_resultado(caminho_critico, nomes, tempo_minimo):
    """
    Exibe o resultado do caminho crítico.

    """
    print("Caminho Crítico:")
    for materia in caminho_critico:
        if materia in nomes:  # Imprime apenas matérias com nomes definidos
            print(f"- {nomes[materia]} ({materia})") 
    print(f"Tempo Mínimo: {tempo_minimo}")