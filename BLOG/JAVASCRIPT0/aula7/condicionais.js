const prompt = require('readline-sync')

const idade = Number(prompt.question('Qual é a sua idade? '))

//estrutura condicionais

if (idade >= 65) {
    console.log('Você é um idoso!')
} else if (idade >= 18 && idade <= 64) {
    console.log('Você é um adulto!')
} else {
    console.log('Você é um jovem!')
    }  //fim da estrutura condicional
