import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria
from pior_caso_bb import busca_binaria, ordenar_valores

def caso_aleatorio_busca_binaria(valores_ordenados, valores_aleatorios):
    # Listas para armazenar os resultados de cada execução
    todas_comparacoes = []
    todos_tempos_execucao = []
    todos_consumo_memoria = []

    for v in valores_aleatorios:
        inicio = time.time()
        time.sleep(0.001)
        indice_encontrado, comparacoes = busca_binaria(valores_ordenados, v)
        fim = time.time()
        tempo_execucao = fim - inicio
        todas_comparacoes.append(comparacoes)
        todos_tempos_execucao.append(tempo_execucao)

        # Medir consumo de memória após cada execução
        consumo_memoria_mb = medir_consumo_memoria()
        todos_consumo_memoria.append(consumo_memoria_mb)

    media_comparacoes = statistics.mean(todas_comparacoes)
    desvio_padrao_comparacoes = statistics.stdev(todas_comparacoes)

    media_tempos_execucao = statistics.mean(todos_tempos_execucao)
    desvio_padrao_tempos_execucao = statistics.stdev(todos_tempos_execucao)

    media_consumo_memoria = statistics.mean(todos_consumo_memoria)
    desvio_padrao_consumo_memoria = statistics.stdev(todos_consumo_memoria)

    return media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao, media_consumo_memoria,desvio_padrao_consumo_memoria


if __name__ == "__main__":
    nome_arquivo_aleatorio= os.path.join("casos_aleatorios_elementos", "elementos_Casos_aleatorios_1000000.txt")
    valores_aleatorios = ler_valores_do_arquivo(nome_arquivo_aleatorio)

    nome_arquivo_original= os.path.join("elementos", "elementos_1000000.txt")
    valores_original = ler_valores_do_arquivo(nome_arquivo_original)

    tempo_ordenacao, valores_ordenados = ordenar_valores(valores_original)

    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao, media_consumo_memoria,desvio_padrao_consumo_memoria = caso_aleatorio_busca_binaria(valores_ordenados, valores_aleatorios)
    
    print(f"Tempo de execução da ordenação (segundos): {tempo_ordenacao:.4f}")
    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes:.4f}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")