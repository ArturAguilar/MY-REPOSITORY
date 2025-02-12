// 1. array.prototype.foreach(): util para iterar sobre un array
//
//const numeros = [40, 34, 67, 89, 23, 10, 16]
//
//numeros.forEach((item, index, arraycompleto) => {
//    console.log(item, index, arraycompleto)
//})
//console.clear()

// 2. array.prototype.find(): util para buscar un elemento uma array

//const encontrado = numeros.find((numeros) => {
//    return numeros < 20 && numeros > 10
//})
//console.log(encontrado)
//console.clear()

const pessoas = [
    {
        nome: 'João',
        idade: 20,
        altura: 1.80,
    },
    {
        nome: 'Maria',
        idade: 30,
        altura: 1.60,
    },
    {
        nome: 'Pedro',
        idade: 40,
        altura: 1.90,
    },
]

const pessoaEncontrada = pessoas.find((pessoas) => {
    return pessoas.idade > 30 || pessoas.altura < 1.80
})
console.log(pessoaEncontrada)
console.clear()

// 3. array.prototype.findIndex(): util para buscar o index de um elemento numa array

const indiceDaPessoaEncontrada = pessoas.findIndex((pessoas) => {
    return pessoas.idade > 20 || pessoas.altura < 1.80
})
console.log(indiceDaPessoaEncontrada)
console.clear()