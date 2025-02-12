// objects literal

const array = ["João", 27, 1.77, true]

const pessoa = {
    nome: "João",
    idade: 27,
    altura: 1.77,
    aprovado: true,
}

console.log(pessoa)
console.clear()

console.log(pessoa.nome)
console.log(pessoa.idade)
console.log(pessoa.altura)
console.log(pessoa.aprovado)
console.clear()

pessoa.nome = "Artur"
pessoa.idade = 18
pessoa.altura = 1.68
pessoa.aprovado = true
pessoa.profissao = "Desenvolvedor"

console.log(pessoa)
console.clear()

delete pessoa.aprovado

console.log(pessoa)
console.clear()

const idade = 18
const altura= 1.68

const objeto = {
    idade,
    altura
}
console.log(objeto)

