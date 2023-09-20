
from datetime import datetime

def diferenca_date_console():
    entrada = input("Digite as datas no formato 'dia de mês de ano': ")
    
    data1_str, data2_str = entrada.split(" - ")

    data1 = datetime.strptime(data1_str, "%d de %B de %Y")
    data2 = datetime.strptime(data2_str, "%d de %B de %Y")
    
    diferenca = abs((data2 - data1).days)
    
    return diferenca

def diferenca_date_arquivo(datas_arquivo):
    with open(datas_arquivo, "r", encoding="utf-8") as file:
        conteudo = file.read()
        data1_str, data2_str = conteudo.split(" - ")
        
        data1 = datetime.strptime(data1_str, "%d de %B de %Y")
        data2 = datetime.strptime(data2_str, "%d de %B de %Y")
        
        diferenca = abs((data2 - data1).days)
    
    return diferenca
