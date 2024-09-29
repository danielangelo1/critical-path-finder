import csv
from collections import defaultdict

def carregar_grafo(arquivo):
    """
    Carrega o grafo a partir de um arquivo CSV.

    :param arquivo: Caminho do arquivo CSV.
    :return: Um grafo, durações, dependências e nomes das tarefas.
    """
    grafo = defaultdict(list)
    duracoes = {}
    dependencias = {}
    nomes = {}

    # Lê o arquivo CSV e constrói o grafo
    with open(arquivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            tarefa = linha['Código']
            duracao = int(linha['Duração'])
            dependencia = linha['Dependências'].split(';') if linha['Dependências'] else []
            duracoes[tarefa] = duracao
            dependencias[tarefa] = dependencia
            nomes[tarefa] = linha['Nome']  # Armazena o nome da tarefa

            # Adiciona arestas no grafo
            for dep in dependencia:
                grafo[dep].append(tarefa)

    return grafo, duracoes, dependencias, nomes
