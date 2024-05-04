import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria
from pior_caso_bs import busca_sequencial

def casos_aleatorios_bs(valores_aleatorios, valores_original, num_execucoes=100):
    # Listas para armazenar os resultados de cada execução
    todas_comparacoes = []
    todos_tempos_execucao = []
    todos_consumo_memoria = []

    for v in valores_aleatorios:
        inicio = time.time()
        time.sleep(0.001)
        indice_encontrado, comparacoes = busca_sequencial(valores_original, v)
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

    # Exibir os resultados finais
    print("Resultados finais para 100 execuções:")
    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao, media_consumo_memoria,desvio_padrao_consumo_memoria = casos_aleatorios_bs(valores_aleatorios, valores_original, 100)
    print(f"Média de comparações: {media_comparacoes:.2f}")
    print(f"Desvio padrão de comparações: {desvio_padrao_comparacoes:.2f}")
    print(f"Média de tempo de execução: {media_tempos_execucao:.4f}")
    print(f"Desvio padrão de tempo de execução: {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória: {media_consumo_memoria:.4f}") 
    print(f"Desvio padrão de consumo de memória: {desvio_padrao_consumo_memoria:.4f}")