# Curso de python voltado para data science e pandas básico.

[INSERIR TUDO QUE ESTÁ DISTRIBUIDO EM VÁRIAS PASTAS E PROJETOS AGORA]

### [Python built-in functions](https://docs.python.org/3.6/library/functions.html)

#### type()

Dá a definição do tipo de objeto passado no argumento.

#### zip(iterator1, iterator2, ... iteratorn)

A função zip retorna um objeto do tipo zip, que a cada iteravel passado como argumento, terá seus index unidos, sendo que o tamanho do iterador (zip) será decidido a partir do iterável com menor comprimento.

#### help(function)
A função help(function) é muito boa para entender alguma função do python, invocando ela do terminal, será mostrado a documentação com alguns exemplos relacionados a função, estrutura ou biblioteca passada, caso exista.

### Pandas

Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.

Dentre essas estruturas de dados, temos por exemplo as series, arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas de uma series são conhecidos como index, e temos abaixo a forma básica de criação dessa estrutura:

```python

```

```python
s = pd.Series(dados, index = index)
```

Aqui estamos chamando a biblioteca Pandas por meio de seu apelido pd seguido de Series(), para o qual passamos os dados e um index (quando necessário). Esse argumento dados pode ser um dicionário, uma lista, um array Numpy ou uma constante.

Também temos o Dataframe, uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Assim como as series, os dataframes são capazes de armazenar qualquer tipo de dado.

```python
df = pd.DataFrame(dados, index = index, columns = columns)
```

#### Criando dataframes e arrays numpy

A propriedade T é uma forma de acessar o método transpose() do DataFrame.
ndarray.T: Retorna o array transposto, isto é, converte linhas em colunas e vice versa.

```python
import pandas as pd

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })
    return result

carros = pd.DataFrame(km_media(dados, 2019)).T

            km          ano     km_media
Crossfox    35000.0     2005.0  2500.0
DS5         17000.0     2015.0  4250.0
Fusca       130000.0    1979.0  3250.0
Jetta       56000.0     2011.0  7000.0
Passat      62000.0     1999.0  3100.0
```

### Tipos de dados no pandas

Um DataFrame nada mais é que um conjunto de series agrupadas, para recebermos apenas um dos dados do dataframe sem recebê-lo como uma series, ou seja, ainda com os index agrupados, devemos utilizar o seguinte formato:


```python
ds[["Valor"]]

output:
                        Valor
Nome
Jetta Variant           88078.64
Passat                  106161.94
Crossfox                72832.16
DS5                     124549.07
Aston Martin DB4        92612.10
... ... ... ... ... ... ... ... 
Phantom 2013            51759.58
Cadillac Ciel concept   51667.06
Classe GLK              68934.03
Aston Martin DB5        122110.90
Macan                   90381.47
258 rows × 1 columns
```
