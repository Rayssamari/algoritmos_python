import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria
from pior_caso_arvore_bi import No, ArvoreBinariaBusca


def casos_aleatorios_arvore_bi_busca(arvore, valores_aleatorios):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for v in valores_aleatorios:
        inicio = time.time()
        time.sleep(0.001)
        resultado = arvore.buscar(v)
        fim = time.time()

        comparacoes = 0
        no_atual = arvore.raiz
        while no_atual is not None:
            comparacoes += 1
            if valor == no_atual.valor:
                break
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        
        tempo_execucao = fim - inicio
        consumo_memoria_mb = medir_consumo_memoria()

        comparacoes_lista.append(comparacoes)
        tempos_execucao_lista.append(tempo_execucao)
        consumo_memoria_lista.append(consumo_memoria_mb)
    
    media_comparacoes = statistics.mean(comparacoes_lista)
    desvio_padrao_comparacoes = statistics.stdev(comparacoes_lista)
    media_tempos_execucao = statistics.mean(tempos_execucao_lista)
    desvio_padrao_tempos_execucao = statistics.stdev(tempos_execucao_lista)
    media_consumo_memoria = statistics.mean(consumo_memoria_lista)
    desvio_padrao_consumo_memoria = statistics.stdev(consumo_memoria_lista)

    return (media_comparacoes, desvio_padrao_comparacoes,
            media_tempos_execucao, desvio_padrao_tempos_execucao,
            media_consumo_memoria, desvio_padrao_consumo_memoria)

if __name__ == "__main__":
    nome_arquivo_aleatorio= os.path.join("casos_aleatorios_elementos", "elementos_Casos_aleatorios_1000000.txt")
    valores_aleatorios = ler_valores_do_arquivo(nome_arquivo_aleatorio)

    nome_arquivo_original= os.path.join("elementos", "elementos_1000000.txt")
    valores_original = ler_valores_do_arquivo(nome_arquivo_original)

    arvore_busca = ArvoreBinariaBusca()

    for valor in valores_original:
        arvore_busca.inserir(valor)

    (media_comparacoes, desvio_padrao_comparacoes,
     media_tempos_execucao, desvio_padrao_tempos_execucao,
     media_consumo_memoria, desvio_padrao_consumo_memoria) = casos_aleatorios_arvore_bi_busca(arvore_busca, valores_aleatorios)

    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")
