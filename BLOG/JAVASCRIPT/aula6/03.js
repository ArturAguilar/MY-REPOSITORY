const prompt = require('readline-sync'); // biblioteca para leitura de entrada do usuário

const idade = prompt.question(" Qual a sua idade?")

const idadeNumber = Number(idade)

console.log(idadeNumber, typeof idadeNumber)

// coerção explicita (converção manual)

console.log(Number("x")) // NaN (Not a Number)
console.log(String(123), typeof String(123))
console.log(Boolean(1), typeof Boolean(1))

// coerção implícita (converção automática)

console.log(1 + "1")
console.log(10 - "5")
console.log(10 * "2")
console.log(10 / "2")