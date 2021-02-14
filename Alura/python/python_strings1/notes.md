# Curso Python3 - Manipulando Strings

## Notas de Aula

### Objetivo :rocket:

O curso de manipulação de strings da [Alura](www.alura.com.br) tem como objetivo, utilizando a linguagem python ensinar os principios de manipulação de strings, um conhecimento imprescíndivel para se trabalhar com dados, visto que é necessário saber desestruturar, encontrar, separar, formatar, alterar, substituir e muitas outras ações possíveis dentro de uma string.

### indice de uma string e fatiamento(slice)

Strings tem alguns comportamentos analogos a lists, cada um dos caractéres dentro de uma string pode ser acessado através de seu índice e são tipos iteraveis também.
Uma string não é modificada quando fazemos qualquer fatiamento nela, e além disso o segundo índice é exclusor.

```python
a = "teste de strings"
print(a[2])
#   's'

print(a[1])
#   'e'
```

E podemos definir também pontos iniciais, finais ou um range dentro da nossa string utilizando o ':' dentro dos colchetes.
o ':' antes número de índice, indica "caractéres até..."

```python
a[:5]
'teste'
```

o ':' depois de número de índice, indica "caractéres a partir de..."

```python
a[5:]
' de strings'
```

e ':' entre dois números de índice, indica uma faixa, "caractéres entre... e ..."

```python
a[5:9]
' de '
```

* Importante ressaltar que espaços em branco (' ') também são tratados como um caracter e são avaliados dentro da função.

### Método find()
O método find(string_buscada) procura dentro da string, um caracter ou sequencia de caracteres que corresponda ao argumento passado e retorna o seu indíce e no caso de não encontrar, retorna o valor: -1.

```python
a = "teste de strings"
a.find("d")
6

a.find(" d")
5

a.find(" s")
8

a.find("str")
9
```

O método find() também pode receber um parametro secundária que será o "ponto de partida" para iniciar a busca pela combinação de caractéres.

```python
a = "teste de strings"

a.find('st',3)
9
```
Ele pula o primeiro "st" na palavra "teSTe" devido a estarmos passando para ele buscar "st" a partir do indíce 3 da string, que é o caracter "t" portanto ele só encontrará a combinação em "STring", no indíce 9

### Método split()

O metódo split(string_separadora) busca dentro da string TODAS as correspondencias ao argumento passado e devolve um vetor, separando cada conjunto de caracteres entre a "string separadora" dentro deste vetor.

```python
#   Utilizando o espaço como separador.
a = "teste de strings"
a.split(' ')
['teste', 'de', 'strings']

a.split('st')
['te', 'e de ', 'rings']
```

Ambos os métodos find() e split() RETORNAM valores, então podemos designá-los a outras variáveis.

```python
#   Utilizando o espaço como separador.
a = "teste de strings"
a.split(' ')
['teste', 'de', 'strings']

indice = a.find(' ')
print(indice)
5
```

## Para saber mais


A URL ( Uniform Resource Locator ) é o endereço de rede onde se encontra um recurso de alguma aplicação WEB. Como vimos nessa aula, a URL pode conter algumas informações de grande importância para que nossos programas funcionem corretamente. Vejamos a url de exemplo abaixo:

https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500

Essa string pode ser divida em duas partes: "endereço"?"argumentos", sendo que a “?” é o divisor entre essas duas partes e é essa caractere que determina que os argumentos começarão a ser passados para uma aplicação.

Vamos dar um zoom no lado dos argumentos da url: "nomeArgumento1"="valorArgumento1"&"nomeArgumento2"="valorArgumento2". Aqui nós percebemos que pode ser passado mais de 1 (um) argumento e que eles são separados pelo caractere especial “&”. Além disso o argumento possui um nome e um valor que são separados pelo caractere “=”.

* [Para saber mais - capitulo 1](https://cursos.alura.com.br/course/python-manipulando-strings/task/52586)]

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

### Referências
[w3School - Strings in Python](https://www.w3schools.com/python/python_strings.asp)

[DevFuria - O básico sobre string](http://devfuria.com.br/python/strings/)

[Caelum - Python Orientação a objetos](https://www.caelum.com.br/apostila/apostila-python-orientacao-a-objetos.pdf)
