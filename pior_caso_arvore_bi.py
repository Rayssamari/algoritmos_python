import time
import statistics
import psutil
import os
from utils import ler_valores_do_arquivo, medir_consumo_memoria

#arvore binaria um no tem o seu valor e pode ter um filho a esquerda (menor que o valor) e outro a direita (maior que o valor)
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    #inserir um nó na árvore, de forma recursiva. 
    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

def executar_buscas(arvore, valor_procurado,num_execucoes=3):
    comparacoes_lista = []
    tempos_execucao_lista = []
    consumo_memoria_lista = []

    for _ in range(num_execucoes):
        inicio = time.time()
        resultado = arvore.buscar(valor_procurado)
        time.sleep(0.001)
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
        consumo_memoria_mb = psutil.Process().memory_info().rss / 1024 / 1024  # em MB

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

def imprimir_arvore(no_atual, indent="", last=True):
    """ Função recursiva para imprimir a árvore binária de forma visual. """
    if no_atual is not None:
        print(indent, end="")
        if last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        # Imprime o valor do nó atual
        print(no_atual.valor)

        # Imprime a subárvore direita
        imprimir_arvore(no_atual.direita, indent, False)

        # Imprime a subárvore esquerda
        imprimir_arvore(no_atual.esquerda, indent, True)


if __name__ == "__main__":
    nome_arquivo = os.path.join("elementos", "elementos_1000000.txt")
    valores = ler_valores_do_arquivo(nome_arquivo)

    arvore_busca = ArvoreBinariaBusca()
    for valor in valores:
        arvore_busca.inserir(valor)

    valor_procurado = 3000000 

    (media_comparacoes, desvio_padrao_comparacoes,
     media_tempos_execucao, desvio_padrao_tempos_execucao,
     media_consumo_memoria, desvio_padrao_consumo_memoria) = executar_buscas(arvore_busca, valor_procurado)


    print(f"Média de comparações: {media_comparacoes}")
    print(f"Desvio padrão das comparações: {desvio_padrao_comparacoes}")
    print(f"Média de tempo de execução (segundos): {media_tempos_execucao:.4f}")
    print(f"Desvio padrão dos tempos de execução (segundos): {desvio_padrao_tempos_execucao:.4f}")
    print(f"Média de consumo de memória (MB): {media_consumo_memoria:.4f}")
    print(f"Desvio padrão do consumo de memória (MB): {desvio_padrao_consumo_memoria:.4f}")
