import csv
from collections import defaultdict

def carregar_grafo(arquivo):
    """
    Carrega o grafo a partir de um arquivo CSV.

    :param arquivo: Caminho do arquivo CSV.
    :return: Um grafo, durações, dependências e nomes das materias.
    """
    grafo = defaultdict(list)
    duracoes = {}
    dependencias = {}
    nomes = {}

    # Lê o arquivo CSV e constrói o grafo
    with open(arquivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            materia = linha['Código']
            duracao = int(linha['Duração'])
            dependencia = linha['Dependências'].split(';') if linha['Dependências'] else []
            duracoes[materia] = duracao
            dependencias[materia] = dependencia
            nomes[materia] = linha['Nome'] 

            # Adiciona arestas no grafo
            for dep in dependencia:
                grafo[dep].append(materia)

    return grafo, duracoes, dependencias, nomes
