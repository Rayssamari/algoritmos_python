import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria


def busca_sequencial(vetor, valor):
    comparacoes = 0
    for indice, elemento in enumerate(vetor):
        comparacoes += 1
        if elemento == valor:
            return indice, comparacoes  
    return None, comparacoes 


# Função para executar a busca sequencial e calcular os valores pedidos
def executar_busca_sequencial_e_medir(vetor, valor_busca, num_execucoes=3):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for _ in range(num_execucoes):
        inicio = time.time()
        time.sleep(0.001)
        indice_encontrado, comparacoes = busca_sequencial(vetor, valor_busca)
        fim = time.time()
        tempo_execucao = fim - inicio
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

    # Executar busca sequencial e obter os resultados
    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao,media_consumo_memoria, desvio_padrao_consumo_memoria = executar_busca_sequencial_e_medir(valores, valor_procurado)


    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")