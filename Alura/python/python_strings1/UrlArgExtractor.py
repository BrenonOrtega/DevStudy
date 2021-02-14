#Refatorando a classe UrlArgExtrator com find e replace
class UrlArgExtractor:
    def __init__(self, url):
        if self.is_url_valid(url): 
            self.url = url.lower()
        else:
            raise LookupError('String Inválida!')

    @staticmethod
    def is_url_valid(url):
        return True if url else False
    
    def arg_extract(self):
        moeda_origem = self.get_moeda_origem()

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            moeda_origem = self.get_moeda_origem()

        moeda_destino = self.get_moeda_destino()

        return moeda_origem, moeda_destino, self.extract_value()

    def get_initial_index(self, moeda_buscada):
         return self.url.find(moeda_buscada) + len(moeda_buscada) 

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", 'real',1)

    def get_moeda_origem(self):
        moeda_origem = 'moedaOrigem='.lower()
        origin_initial_index = self.get_initial_index(moeda_origem)
        origin_final_index = self.url.find('&', origin_initial_index)
        return self.url[origin_initial_index : origin_final_index]
    
    def get_moeda_destino(self):
        moeda_destino = "moedaDestino=".lower()
        destiny_initial_index = self.get_initial_index(moeda_destino)
        destiny_final_index = self.url.find("&", destiny_initial_index)
        return self.url[destiny_initial_index : destiny_final_index]

    def extract_value(self):
        valor = "valor=".lower()
        valor_initial_index = self.url.find(valor) + len(valor)
        return self.url[valor_initial_index : ]
