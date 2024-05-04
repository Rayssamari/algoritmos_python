import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria


# função para ordenar o vetor e medir o tempo de execução da ordenação
def ordenar_valores(valores):
    inicio_ordenacao = time.time()
    valores_ordenados = sorted(valores)  
    fim_ordenacao = time.time()
    tempo_ordenacao = fim_ordenacao - inicio_ordenacao
    return tempo_ordenacao, valores_ordenados

def busca_binaria(vetor, valor):
    comparacoes = 0
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if vetor[meio] == valor:
            return meio, comparacoes
        elif vetor[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None, comparacoes

def calcular_busca_binaria(valores_ordenados, valor_procurado, num_execucoes=3):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for _ in range(num_execucoes):
        inicio_busca = time.time()
        time.sleep(0.001)
        indice_encontrado, comparacoes = busca_binaria(valores_ordenados, valor_procurado)
        fim_busca = time.time()
        tempo_execucao = fim_busca - inicio_busca

        comparacoes_lista.append(comparacoes)
        tempos_execucao_lista.append(tempo_execucao)

        # Medir consumo de memória após cada execução
        consumo_memoria_mb = medir_consumo_memoria()
        consumo_memoria_lista.append(consumo_memoria_mb)

    # Calcular média e desvio padrão das comparações, tempos de execução e consumo de memória
    media_comparacoes = statistics.mean(comparacoes_lista)
    desvio_padrao_comparacoes = statistics.stdev(comparacoes_lista)
    media_tempos_execucao = statistics.mean(tempos_execucao_lista)
    desvio_padrao_tempos_execucao = statistics.stdev(tempos_execucao_lista)
    media_consumo_memoria = statistics.mean(consumo_memoria_lista)
    desvio_padrao_consumo_memoria = statistics.stdev(consumo_memoria_lista)

    return media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao, media_consumo_memoria,desvio_padrao_consumo_memoria

if __name__ == "__main__":
    nome_arquivo = os.path.join("elementos", "elementos_1000000.txt")
    valores = ler_valores_do_arquivo(nome_arquivo)

    # Valor a ser buscado no vetor > 2 milhões
    valor_procurado = 3000000

    tempo_ordenacao, valores_ordenados = ordenar_valores(valores)

    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao, media_consumo_memoria,desvio_padrao_consumo_memoria = calcular_busca_binaria(valores_ordenados, valor_procurado)

    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes:.4f}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")
    print(f"Tempo de execução da ordenação (segundos): {tempo_ordenacao:.4f}")