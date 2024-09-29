def encontrar_caminho_critico_bellman_ford(grafo, duracoes, tarefas):
    """
    Encontra o caminho crítico utilizando o algoritmo de Bellman-Ford.

    :param grafo: O grafo de tarefas.
    :param duracoes: Durações de cada tarefa.
    :param tarefas: Lista de todas as tarefas.
    :return: Caminho crítico e o tempo mínimo.
    """
    # Inicializa distâncias e predecessores
    distancias = {tarefa: float('-inf') for tarefa in tarefas}  # Usar -infinito para caminhos máximos
    predecessores = {tarefa: None for tarefa in tarefas}

    # Define a distância inicial (s) como 0
    distancias['s'] = 0

    # Atualiza as distâncias para cada tarefa
    for _ in range(len(tarefas) - 1):
        for tarefa in tarefas:
            if tarefa not in grafo:  # Ignora tarefas que não têm saídas
                continue
            for proxima in grafo[tarefa]:
                if proxima in duracoes:  # Verifica se a próxima tarefa tem duração
                    if distancias[tarefa] + duracoes[proxima] > distancias[proxima]:
                        distancias[proxima] = distancias[tarefa] + duracoes[proxima]
                        predecessores[proxima] = tarefa

    # Encontra a maior distância e reconstrói o caminho crítico
    max_dist = float('-inf')
    tarefa_final = None

    for tarefa, distancia in distancias.items():
        if distancia > max_dist:
            max_dist = distancia
            tarefa_final = tarefa

    # Reconstrói o caminho crítico
    caminho_critico = []
    while tarefa_final:
        caminho_critico.append(tarefa_final)
        tarefa_final = predecessores[tarefa_final]

    caminho_critico.reverse()  # Inverte para ter a ordem correta
    return caminho_critico, max_dist
