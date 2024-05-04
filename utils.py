import psutil

def ler_valores_do_arquivo(nome_arquivo):
    valores = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            valor = linha.strip() 
            if valor.isdigit():  # Verifica se o valor é um número inteiro
                valores.append(int(valor))
    return valores

def medir_consumo_memoria():
    # Obtém o consumo de memória atual do processo em bytes
    consumo_memoria_bytes = psutil.Process().memory_info().rss
    # Converte para megabytes
    consumo_memoria_mb = consumo_memoria_bytes / (1024 * 1024)
    return consumo_memoria_mb