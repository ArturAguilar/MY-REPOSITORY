// operadores boleanos: comparações
// == igual
// != diferente
// > maior
// < menor
// >= maior ou igual
// <= menor ou igual
// === igual e do mesmo tipo
// !== diferente e do tipo diferente

const num1 = 10
const num2 = 12

console.log(num1 == num2) // false
console.log(num1 === num2) // false
console.log(num1 === "10") // true

console.log(num1 > num2)

// operadores lógicos:
// && e
// || ou
// ! negação

const idadePessoa1 = 18
const idadePessoa2 = 25

console.log(idadePessoa1 >= 18 && idadePessoa2 >= 18) // true
console.log(idadePessoa1 >= 18 || idadePessoa2 >= 18) // true

console.log(!true)

console.log(!(idadePessoa1 >= 18)) // false