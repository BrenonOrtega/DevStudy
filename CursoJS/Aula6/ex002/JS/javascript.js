//Inserção de dados nas variáveis.
window.alert("dahora, olá mundo!")

window.confirm("Está gostando de fazer programação?")

//guarda o resultado do prompt na variavel nome.
//poderia criar a variável usando var, let ou const mas altera o escopo da variável.
var nome = window.prompt("Qual é seu nome?")

//Exemplo fzd o alert concatenando
alert("olá " + nome + " isso foi escrito com concatenação.")

//exemplo utilizando o template string.
alert(`alo srº ${nome} como está? isso foi escrito utilizando template string`)

//Será pedido dois números e feito a soma dos dois.
//comando parseInt() transforma o que naturalmente vem como string do prompt em númeral, é feita a soma e então apresentado no alert
var n1 = parseInt(window.prompt("Insira um número por favor."))

var n2 = parseInt(window.prompt("Insira um número por favor."))

var s = n1+n2

alert(`A soma dos número é ${s}`)

//Agora mostrarei um valor monetário em dolar, euro e real, utilizando o conversor Number.
var valor = Number(window.prompt("Conversor de Moeda.", "Insira um valor, por favor"))

//converte o valor para dolar adicionando o cifrão.
var cotDolar = valor.toLocaleString('en', {style: 'currency', currency: "USD"})

var cotEuro = valor.toLocaleString("EN", {style: "currency", currency: "EUR"})

//lb para quebra de linha
var lb = '\n'

//coloca na variavel msg as frases e os valores inseridos pelo usuário convertidos.
msg = `O valor no formato dolar é ${cotDolar} ${lb}O valor no formato euro é: ${cotEuro}.`

alert(msg)

this.Document.getElementById("myp2").innerHTML = msg

function myfunction(){
    document.getElementById("demo").innerHTML= "Voi-lá, um clique magistral com toda a certeza."
}


