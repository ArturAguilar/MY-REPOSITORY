//map: cria um novo objeto com as chaves e valores passados 

const numeros = [40, 34, 67, 89, 23, 10, 16]

const novoArrey = numeros.map((elemento) => {
    return elemento * 2
})
console.log(novoArrey)
console.clear()

// elevando ao quadrado

const valores = [27, 24, 10 ,25, 18, 75, 85, 31]

const quadrado = valores.map((elemento) => {
    return elemento ** 2
})
console.log(quadrado)
console.clear()

// adicionando propriedade aos objetos da array

const carrinho = [
    {produto: "feijão", preco: 5.00, quantidade: 2},
    {produto: "arroz", preco: 3.00, quantidade: 1},
    {produto: "macarrão", preco: 2.00, quantidade: 3},
    {produto: "queijo", preco: 8.00, quantidade: 1},
]

const total = carrinho.map((elemento) => {
    return{
        ...elemento,
        total: elemento.preco * elemento.quantidade
    }
})
console.log(total)
console.clear()

// calculando o imc

const pessoas = [
    {nome: "João", altura: 1.80, peso: 70},
    {nome: "Maria", altura: 1.60, peso: 50},
    {nome: "Pedro", altura: 1.90, peso: 80},
    {nome: "Ana", altura: 1.70, peso: 60},
]

const imc = pessoas.map((elemento) => {
    return{
        ...elemento,
        imc: elemento.peso / (elemento.altura ** 2)
    }
})
console.log(imc)