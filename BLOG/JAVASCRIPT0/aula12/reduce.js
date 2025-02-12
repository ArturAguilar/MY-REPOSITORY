// reduce: e usado para reduzir um array para um valor único

const numeros =  [1, 2, 3, 4, 5]

const soma = numeros.reduce((acumulador, elemento) => {
    return acumulador + elemento
})
console.log(soma) // 15
console.clear()

const media = numeros.reduce((acumulador, elemento, indice, array) => {
    return elemento / array.lengh + acumulador
}, 0)
console.log(media) // 3
console.clear()

const somaDosPares = numeros.reduce((acumulador, numero) => {
    if (numero % 2 === 0) {
        return acumulador + numero
    } else {
        return acumulador
    }
} , 0)
console.log(somaDosPares) // 6
console.clear()

const carrinho = [
    {produto: "feijão", preco: 5.00, quantidade: 27},
    {produto: "arroz", preco: 3.00, quantidade: 150},
    {produto: "macarrão", preco: 2.00, quantidade: 55},
    {produto: "queijo", preco: 8.00, quantidade: 90},
]

const total = carrinho.reduce((acumulador, item) => {
    return item.preco * item.quantidade + acumulador
} , 10)
console.log(total) // 10 * 2 + 10 * 1 + 10 * 3 + 10 * 1 = 60