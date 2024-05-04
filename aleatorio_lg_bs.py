import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria
from pior_caso_lg_bs import Lista_Ligada, No


def caso_aleatorio_listaLigada_sequencial(lista, valores_aleatorios):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for v in valores_aleatorios:
        inicio_busca = time.time()
        time.sleep(0.001)
        comparacoes = lista.busca_sequencial_lg(v)
        fim_busca = time.time()
        tempo_execucao = fim_busca - inicio_busca

        comparacoes_lista.append(comparacoes)
        tempos_execucao_lista.append(tempo_execucao)

        consumo_memoria_mb = medir_consumo_memoria()
        consumo_memoria_lista.append(consumo_memoria_mb)

    # Calcular média e desvio padrão das comparações, tempos de execução e consumo de memória
    media_comparacoes = statistics.mean(comparacoes_lista)
    desvio_padrao_comparacoes = statistics.stdev(comparacoes_lista)

    media_tempos_execucao = statistics.mean(tempos_execucao_lista)
    desvio_padrao_tempos_execucao = statistics.stdev(tempos_execucao_lista)

    media_consumo_memoria = statistics.mean(consumo_memoria_lista)
    desvio_padrao_consumo_memoria = statistics.stdev(consumo_memoria_lista)

    return media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao,media_consumo_memoria, desvio_padrao_consumo_memoria



if __name__ == "__main__":
    # Ler os valores do arquivo e criar a lista ligada
    nome_arquivo_aleatorio= os.path.join("casos_aleatorios_elementos", "elementos_Casos_aleatorios_1000000.txt")
    valores_aleatorios = ler_valores_do_arquivo(nome_arquivo_aleatorio)

    nome_arquivo_original= os.path.join("elementos", "elementos_1000000.txt")
    valores_original = ler_valores_do_arquivo(nome_arquivo_original)

    lista_ligada = Lista_Ligada()

    inicio_criacao = time.time()
    for valor in valores_original:
        lista_ligada.inserir_dados(valor)
    fim_criacao = time.time()
    tempo_criacao = fim_criacao - inicio_criacao
    

    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao,media_consumo_memoria, desvio_padrao_consumo_memoria = caso_aleatorio_listaLigada_sequencial(lista_ligada, valores_aleatorios)

    # Exibir resultados com formatação de cinco casas decimais
    print(f"Média de comparações: {media_comparacoes:.2f}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes:.2f}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")
    print(f"Tempo de criação da lista (segundos): {tempo_criacao:.4f}")