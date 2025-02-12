// Utilize sempre o camel Case para nomes de variáveis e funções 

// javascript possui tipagem dinamica: infere os tipos de dados
// javascript possui uma tipagem fraca

var nomeDoProfessor = "Artur"; // string (texto): utilize sempre aspas duplas para strings
    console.log(nomeDoProfessor, typeof nomeDoProfessor) // tipo da variável

var idade = 18; // number
    console.log(idade, typeof idade)

var altura = 1.68; // number
    console.log(altura, typeof altura)

var estaAprovado = true; // boolean
    console.log(estaAprovado, typeof estaAprovado)

var semConteudo; // declarando uma variável sem conteúdo
    console.log(semConteudo, typeof semConteudo)

var curso = 'front end em react', 
    topico = 'javascript basico 1'
    console.log(curso, topico)


// ! Não utilize o var , utilize let ou const

let notaDoAluno = 10
const mediaDoAluno = 8

notaDoAluno = 9
// ! não é possível alterar a const

console.log(notaDoAluno)
console.log(mediaDoAluno)