const prompt = require('readline-sync')

let saldo = Number(prompt.question("Qual é o seu saldo? "))


while (saldo < 0) {
   saldo = Number(
        prompt.question('Saldo inválido! Por favor, informe novamente: ')
    )
}

console.log(saldo)

/////////////////////////////////////////////////////////////////////////////////
let notaDoAluno = Number(prompt.question('Informe a nota do aluno: '))

let somaDasnotas = 0 // acumulador
let qtdNotasvalidas = 0

while (notaDoAluno >= 0) {
    somaDasnotas += notaDoAluno // incrementando o acumulador
    qtdNotasvalidas++ // pós-incremento

    notaDoAluno = Number(prompt.question('Informe a prôxima nota'))
}

console.log(somaDasnotas)
console.log(qtdNotasvalidas)

console.log('Media das notas: ' + somaDasnotas / qtdNotasvalidas) // media das notas

/////////////////////////////////////////////////////////////////////////////////////////////////
//math.random() gera um número aleatório entre 0 e 1
const numeroAleatorio = Math.round(Math.random() * 10)

let numeroDoUsuario = Number(prompt.question(`Informe um número entre 0 e 10: `))

console.log(numeroAleatorio)

while (numeroDoUsuario !== numeroAleatorio) {
    console.log(`Você errou o número! tente novamente...`)
    numeroDoUsuario = Number(prompt.question(`Informe um número entre 0 e 10: `))
}

    console.log(`Parabéns você acertou o número! O número era:`, numeroAleatorio) // concatenando strings

///////////////////////////////////////////////////////////////////////////////////////////////////////////
let contador = 0

while (contador < 10) {
    console.log(contador)
    contador++

    if (contador === 2) {
        continue
    }

    console.log('Depois do if...')
    
} // incrementando o contador

//////////////////////////////////////////////////////////////////////////////////////////////////////////////
// do-while

do{
    saldo = Number(
        prompt.question('Saldo inválido! Por favor, informe novamente: ')
    )
} while (saldo < 0)

console.log(saldo)