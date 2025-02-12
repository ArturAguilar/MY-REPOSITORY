// 4. array.prototype.every(): util para verificar se todos os elementos de uma array satisfazem uma condição 

const numeros = [40, 34, 67, 89, 23, 10, 16]

const pessoas = [
    {
        nome: 'João',
        idade: 20,
        altura: 1.80,
    },
    {
        nome: 'Maria',
        idade: 30,
        altura: 1.60,
    },
    {
        nome: 'Pedro',
        idade: 40,
        altura: 1.90,
    },
]

const todosPositivos = numeros.every((elemento) => {
    return elemento > 0
})

console.log(todosPositivos)
console.clear()

const todosMaioresDeIdade = pessoas.every((pessoas) => {
    return pessoas.idade > 18 && pessoas.altura >1.50
})
console.log(todosMaioresDeIdade)
console.clear()

// 5. arrayprototype.some(): verifica se algum elemento da array torna verdadeira uma determinada condição retornada pela função

const numeros2 = [-1, 3, 7, -3, 5]

const retorno = numeros2.some((numeros) => {
    numeros > 0
})
console.log(retorno)