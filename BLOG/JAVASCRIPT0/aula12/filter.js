// filter: utilizado para filtrar os dados 
// map: utilizado para criar um novo array com os dados transformados 

const numeros = [40, 34, 67, 89, 23, 10, 16]

const numerosPar = numeros.filter((elemento) => {
    return elemento % 2 === 0
})
console.log(`esses são os nossos numeros pares: ${numerosPar}`)

const numerosImpar = numeros.filter((elemento) => {
    return elemento % 2 !== 0
})
console.log(`esses são os nossos numeros impares: ${numerosImpar}`)
console.clear()



// dados de alunos
const alunos = [
    {nome: "João", media: 96},
    {nome: 'Maria', media: 90},
    {nome: 'Pedro', media: 80},
    {nome: 'Ana', media: 70},
    {nome: 'Gustavo', media: 60},
    {nome: 'Luis', media: 50},
    {nome: 'Rafael', media: 40},
    {nome: 'Lucas', media: 30},
    {nome: 'Mateus', media: 20},
    {nome: 'Gabriel', media: 10},
]
console.log("Essa é a lista completa:", alunos , "\n")

const passouOuNao = alunos.map((elemento) => {
    return{
        ...elemento,
        passou: elemento.media >= 60
    }
})

const passou = passouOuNao.filter((elemento) => {
    return elemento.passou
})
console.log("Esses passaram:" , passou ,"\n")

const naoPassou = passouOuNao.filter((elemento) => {
    return !elemento.passou
})
console.log("Esses não passaram:", naoPassou)  // não passou é o contrário de passou
console.clear()


// dados de produtos

const produtos = [
    {nome: "suco de laranja", preco: 10.0, tipo: "bebida"},
    {nome: "pão", preco: 3.00, tipo: "comida"},
    {nome: "queijo", preco: 29.00, tipo: "comida"},
    {nome: "leite", preco: 5.00, tipo: "bebida"},
    {nome: "arroz", preco: 30.00, tipo: "comida"},
    {nome: "feijão", preco: 10.00, tipo: "comida"},
    {nome: "macarrão", preco: 5.00, tipo: "comida"},
    {nome: "sorvete", preco: 40.00, tipo: "sobremesa"},
]

const analise = produtos.filter((produto) => {
    return produto.preco < 50 && produto.tipo !== "bebida"
})
console.log("Esses produtos são menores que 10 e não são bebidas:", analise)