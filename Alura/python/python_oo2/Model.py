class ProducaoCinematografica:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
 
    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Filme(ProducaoCinematografica):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

     


class Serie(ProducaoCinematografica):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("vingadores-guerra infinita", 2018, 160)
demolidor = Serie("demolidor da netflix", 2015, 3)

vingadores.dar_like()
demolidor.dar_like() 


vingadores.nome = 'vingadores-guerra infinita parte 2'
print (vingadores.nome)

print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
print(f'{demolidor.nome} - {demolidor.temporadas}: {demolidor.likes}')
