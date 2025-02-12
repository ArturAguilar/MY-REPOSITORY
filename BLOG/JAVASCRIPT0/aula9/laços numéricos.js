const prompt = require('readline-sync');

//for (let i = 0; i < 10; i++) {
//    console.log(i);
//}
//
//console.clear()
//
//let maiorNumero = 0
//let numeroInformado
//
//for (let i = 0; i < 5; i++) {
//    numeroInformado = Number(prompt.question('Digite um número: '))
//    if (numeroInformado > maiorNumero) {
//        maiorNumero = numeroInformado
//    }
//}
//console.log(`O maior número informado foi: ${maiorNumero}`)

// percorrendo strings com for

//const nome = 'João'
//
//for (let i = 0; i < nome.length; i++) {
//    console.log(nome[i])
//}

// * arrays

const notasDoAluno = [10, 8, 5]
const pessoa = ['João', 19, 1.77, true]

console.log(notasDoAluno)
console.log(pessoa)
console.log(pessoa[0])

pessoa[3] = false

console.log(pessoa)

console.clear()
console.log(notasDoAluno.length)
console.log(pessoa.length)

console.clear()

// fatiamento de arrays

const notas = [10, 8, 5, 9, 7, 8]

console.log(notas.slice(0, 2))
console.log(notas.slice(2))

console.clear()

// adicionando elementos no final da array
notas.push(0)
console.log(notas)

console.clear()
// adicionando elemento no inicio da array
notas.unshift(20)
console.log(notas)

console.clear()

// pop: remove o último elemento da array
notas.pop()
console.log(notas)

console.clear()

// shift: remove o primeiro elemento da array
notas.shift()
console.log(notas)

console.clear()

// sera que o numero 3 está na array?
console.log(notas.includes(3))


// indexof: busca o índice de um elemento na array
const index = notas.indexOf(8)
console.log(index)

// lastindexof: busca o índice do último elemento da array
const lastIndex = notas.lastIndexOf(8)
console.log(lastIndex)

console.clear()


// percorendo uma array com o for

const arr = [45, 36, 90, 76, 32, 7]

for (let i = 0; i < arr.length; i++) {
    console.log(i, '=', arr[i])
}

console.clear()

// for-of

for (const elemento of arr){
    console.log(elemento)
}


//for-in

for (const indice in arr){
    console.log(indice)
}