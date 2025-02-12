const fs = require('fs')

//// 1. callbacks
//console.log("Antes de ler o arquivo")
//
//// função assicrona para ler o arquivo
//fs.readFile("aula13/arquivo.txt", (erro, conteudoDoArquivo) => {
//    if (erro) {
//        console.log(erro)
//    } else {
//        console.log(conteudoDoArquivo.toString())
//    }
//})
//
//console.log("Depois de ler o arquivo")
//console.clear()
//
//
// 2. promises 
function lerArquivoComPromisse() {
    return new Promise((resolve, reject) => {
            fs.readFile("aula13/arquivo.txt", (erro, conteudoDoArquivo) => {
            if (erro) {
                reject(erro)
            } else {
               resolve(conteudoDoArquivo.toString())
            }
        })
    }) 
}
//
//
// foco aqui
lerArquivoComPromisse()
.then((retornoDoResolve) => {
    console.log(retornoDoResolve)
})
.catch((erro) => {
    console.log(erro)
})
.finally(() => {
    console.log("Fim da execução")

})


// 3. async/await
async function leituraDeDados() {
    console.log("Isso é antes de ler o arquivo")

    try {
        const retornoDaPromessa = await lerArquivoComPromisse()

    console.log(retornoDaPromessa)
    console.log("Isso é depois de ler o arquivo")
    } catch (erro) {
        console.log(erro)
        console.log("Isso é depois de ler o arquivo")
    } finally {
        console.log("Fim da execução")
    }
}
leituraDeDados()