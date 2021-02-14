from UrlArgExtractor import UrlArgExtractor
#   Desafio Capitulo1
url = 'www.bytebank.com.br/cambio?valor=1500&moedaOrigem=real&moedaDestino=dolar'

url_menor = 'cambio?moedaOrigem=moedaDestino&moedaDestino=dolar&valor=1500'

a = UrlArgExtractor(url_menor)
moeda_origem, moeda_destino, valor = a.arg_extract()
print('*' * 50)
print(moeda_origem, moeda_destino, valor)
print('*' * 50)
