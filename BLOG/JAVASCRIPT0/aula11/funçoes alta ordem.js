const prompt = require('readline-sync');

// 1. funçao que retorna outa funçao como parametro 

function welcome(courseName) {
    return (studentName) => {
        console.log(`Bem vindo ao curso de ${courseName}! Seja bem vindo, ${studentName}!`)
    }
}
const welcomeToCourse = welcome('JavaScript')
welcomeToCourse('João') // Bem vindo ao curso de JavaScript! Seja bem vindo, João!
console.clear()

// 2. funçao que recebe outra funçao como parametro
const soma = (a, b) => a + b
const subtrair = (a, b) => a - b
const multiplicar = (a, b) => a * b
const dividir = (a, b) => a / b

const calcular = (a, b, operacao) => {
    return operacao(a, b)
}

const retorno = calcular(10, 2, soma) // 12
calcular(10, 2, subtrair) // 8
calcular(10, 2, multiplicar) // 20
calcular(10, 2, dividir) // 5

console.log(retorno);

const resultado = calcular(
    10, 
    5, 
    (a, b) => (a * b) + 2 * (a * b)
);
console.log(resultado); // 82