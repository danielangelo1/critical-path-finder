from grafo import carregar_grafo
from caminho_critico import encontrar_caminho_critico_bellman_ford, exibir_resultado

def main():
    """
    Função principal que gerencia a interação com o usuário e o processamento do caminho crítico.
    """
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':  
            break
        if not arquivo.endswith('.csv'):
            print("Arquivo inválido. Informe um arquivo CSV.")
            continue

        print("Processando ...")
        grafo, duracoes, dependencias, nomes = carregar_grafo(arquivo)  # Carrega dados do arquivo

        # Prepara o grafo para o algoritmo de Bellman-Ford
        materias = list(duracoes.keys()) + ['s', 't']  # Adiciona nós 's' (início) e 't' (fim)
        grafo['s'] = [materia for materia in duracoes if not dependencias[materia]]  # 's' se conecta a matérias sem dependências
        for materia in duracoes:
            if materia in grafo:
                grafo[materia].append('t')  # Conecta todas as matérias a 't'
        duracoes['t'] = 0  # 't' tem duração zero

        # Calcula o caminho crítico
        caminho_critico, tempo_minimo = encontrar_caminho_critico_bellman_ford(grafo, duracoes, materias)

        # Exibe o resultado
        exibir_resultado(caminho_critico, nomes, tempo_minimo)

if __name__ == "__main__":
    main()