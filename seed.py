import random
import os

def gerador_de_numeros(quant_valores, valor_min, valor_max):
    # Gera os dados para o arquivo
    valores_unicos = random.sample(range(valor_min, valor_max + 1), quant_valores)
    return valores_unicos

def escrever_arquivo(valores, arquivo):
    # Abre o arquivo em modo de escrita
    with open(arquivo, 'w') as file:
        # Escreve cada valor em uma linha do arquivo
        for valor in valores:
            file.write(f"{valor}\n")

# Parâmetros para gerar os valores únicos
quant_valores = 100
valor_min = 1
valor_max = 2000000
caso = 1000000

# Gera os valores únicos aleatórios
v_unico_radom = gerador_de_numeros(quant_valores , valor_min, valor_max)

if quant_valores > 1000:
    # Salva o arquivo na pasta 'elementos'
    nome_arquivo = (f"elementos_{quant_valores}.txt")
    caminho_arquivo = os.path.join("elementos", nome_arquivo)
else:
    # Salva o arquivo na pasta 'casos_aleatorios_elementos'
    nome_arquivo = (f"elementos_Casos_aleatorios_{caso}.txt")
    caminho_arquivo = os.path.join("casos_aleatorios_elementos", nome_arquivo)

# Escreve os valores no arquivo
escrever_arquivo(v_unico_radom, caminho_arquivo)

print("valores únicos foram gerados e salvos no arquivo.")
