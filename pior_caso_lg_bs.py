import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria

#Uma forma de ser "parecida" com o struct do C. 
class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.prox = None

class Lista_Ligada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_dados(self, dado):
        novo_no = No(dado)
        if not self.inicio:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.prox = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def busca_sequencial_lg(self, valor):
        no_atual = self.inicio
        comparacoes = 0
        while no_atual:
            comparacoes += 1
            if no_atual.dado == valor:
                return comparacoes
            no_atual = no_atual.prox
        return comparacoes


def calcular_busca_sequencial_lista_ligada(lista, valor_procurado, num_execucoes=3):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for _ in range(num_execucoes):
        inicio_busca = time.time()
        time.sleep(0.001)
        comparacoes = lista.busca_sequencial_lg(valor_procurado)
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

    return media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao,media_consumo_memoria, desvio_padrao_consumo_memoria


if __name__ == "__main__":
    # Ler os valores do arquivo e criar a lista ligada
    nome_arquivo = os.path.join("elementos", "elementos_1000000.txt")
    valores = ler_valores_do_arquivo(nome_arquivo)
    lista_ligada = Lista_Ligada()
    
    # Valor a ser buscado no vetor > 2 milhões
    valor_procurado = 3000000

    inicio_criacao = time.time()
    for valor in valores:
        lista_ligada.inserir_dados(valor)
    fim_criacao = time.time()
    tempo_criacao = fim_criacao - inicio_criacao

    media_comparacoes, desvio_padrao_comparacoes, media_tempos_execucao, desvio_padrao_tempos_execucao,media_consumo_memoria, desvio_padrao_consumo_memoria = calcular_busca_sequencial_lista_ligada(lista_ligada, valor_procurado)

    # Exibir resultados com formatação de cinco casas decimais
    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")
    print(f"Tempo de criação da lista (segundos): {tempo_criacao:.4f}")