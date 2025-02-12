const prompt = require('readline-sync')

const permicao = prompt.question('Qual é sua posição na escola? ')

//estrutura condicionais

switch (permicao) {
    case 'aluno':
        console.log('Você só pode visualizar as aulas.')
        break;
    case 'professor':
        console.log('Você pode alterar as aulas e adicionar novas.')
        break;
    case 'admin':
        console.log('Você pode fazer tudo.')
        break;
    default:
        console.log('Pessoa não reconhecida')
        break;
    }  //fim do switch
