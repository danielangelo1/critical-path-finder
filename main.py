from grafo import carregar_grafo
from caminho_critico import encontrar_caminho_critico_bellman_ford

def main():
    """
    Função principal que gerencia a interação com o usuário.
    """
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        print("Processando ...")
        grafo, duracoes, dependencias, nomes = carregar_grafo(arquivo)
        
        # Adiciona o nó inicial 's' e o nó final 't'
        tarefas = list(duracoes.keys()) + ['s', 't']
        grafo['s'] = [tarefa for tarefa in duracoes if not dependencias[tarefa]]  # Conecta 's' às tarefas sem dependências
        
        # Conecta todas as tarefas ao nó 't'
        for tarefa in duracoes:
            if tarefa in grafo:
                grafo[tarefa].append('t')  # Conecta todas as tarefas a 't'

        duracoes['t'] = 0  # Duração zero para o nó 't'

        # Encontra o caminho crítico
        caminho_critico, tempo_minimo = encontrar_caminho_critico_bellman_ford(grafo, duracoes, tarefas)

        # Exibe o caminho crítico e o tempo mínimo
        print("Caminho Crítico:")
        for tarefa in caminho_critico:
            if tarefa in nomes:  # Apenas imprime as tarefas com nomes
                print(f"- {nomes[tarefa]} ({tarefa})")  
        print(f"Tempo Mínimo: {tempo_minimo}")

if __name__ == "__main__":
    main()
