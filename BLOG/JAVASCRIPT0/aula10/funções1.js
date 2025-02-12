const prompt = require('readline-sync');

// definição de função  
//const nome = prompt.question("Qual é o seu nome? ")
//const curso = prompt.question("Qual é o seu curso? ")
//
//function saudacao(nomeDoEstudante, curso) {
//   return `Olá, ${nomeDoEstudante}! Bem-vindo ao curso de ${curso}!`
//}
//
//if (curso == "" || nome == "") {
//    console.log("Por favor, preencha todos os campos!")
//} else {
//    console.log(saudacao(nome, curso))
//    }  // fim da função

console.clear()


// funções anonimas

//const dobroDoNumero = function (numero) {
//    return numero * 2
//}
//
//const dobro = dobroDoNumero(5)
//console.log(dobro)

console.clear()


//arrow functions: são funções mais concisas e modernas

const subtrair = (num1, num2) => {
    return num1 - num2
}

const multiplicar = (num1, num2) => num1 * num2

const triploDoNumero = (numero) => numero * 3
