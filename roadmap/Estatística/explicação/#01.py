"""
Variáveis Qualitativas (ou Categóricas)
    Estas variáveis descrevem qualidades ou categorias e não possuem valores numéricos que façam sentido matematicamente.

    Subtipos:
        Nominais: Não possuem ordem lógica entre as categorias.
        Exemplos: Cor dos olhos (azul, verde, castanho), estado civil (solteiro, casado).

        Ordinais: Possuem uma ordem ou hierarquia lógica entre as categorias.
        Exemplos: Grau de escolaridade (fundamental, médio, superior), nível de satisfação (ruim, bom, excelente).
"""

"""
Variáveis Quantitativas
    Estas variáveis representam valores numéricos e permitem operações matemáticas.

    Subtipos:
        Discretas: Assumem valores inteiros ou contáveis.
        Exemplos: Número de filhos, quantidade de livros em uma biblioteca.
        
        Contínuas: Assumem qualquer valor dentro de um intervalo, incluindo frações.
        Exemplos: Peso (70,5 kg), altura (1,73 m), temperatura (37,2 °C).
"""

"""
Variáveis de Escala
    São classificadas com base nas operações matemáticas que podem ser aplicadas.

    Nominal: Apenas categorização (cores, gêneros, tipos de animais).
    Ordinal: Categorização e ordem (posição em um ranking).

    Intervalar: Mede diferenças entre valores, mas não possui um zero absoluto.
    Exemplo: Temperatura em Celsius ou Fahrenheit.

    Razão: Mede diferenças e possui um zero absoluto.
    Exemplo: Altura, peso, tempo (zero significa ausência).
"""

# Variáveis Qualitativas
cor_olhos = ["azul", "verde", "castanho"]  # Nominal
nivel_satisfacao = ["ruim", "bom", "ótimo"]  # Ordinal

# Variáveis Quantitativas
num_filhos = [0, 1, 2, 3]  # Discreta
peso = [55.5, 62.3, 70.2, 80.0]  # Contínua

# Classificação e análise
print("Cores dos olhos:", cor_olhos)
print("Nível de satisfação:", nivel_satisfacao)
print("Número de filhos:", num_filhos)
print("Pesos registrados:", peso)

"""
Variáveis Constantes
    Descrição: Representam valores fixos que não podem ser alterados durante a execução do programa.
    Exemplo em Python: PI = 3.14159
"""

""" 
Variáveis Compostas
    Estas variáveis podem armazenar coleções de dados. Elas são muito úteis para organizar informações complexas.

    Listas (ou Arrays):
        Descrição: Armazenam uma sequência de elementos.
        Exemplo: lista_de_frutas = ["maçã", "banana", "laranja"]

    Tuplas:
        Descrição: Similar às listas, mas imutáveis.
        Exemplo: coordenadas = (10, 20)

    Dicionários (ou Mapas):
        Descrição: Armazenam pares de chave-valor.
        Exemplo: pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

    Conjuntos (Sets):
        Descrição: Armazenam valores únicos e não ordenados.
        Exemplo: numeros_unicos = {1, 2, 3, 4, 5}
"""

"""
Variáveis Dinâmicas
    Descrição: Em linguagens com tipagem dinâmica (como Python e JavaScript), o tipo da variável pode mudar em tempo de execução.
    Exemplo: x = 10  # x é um inteiro
             x = "Olá"  # x agora é uma string
"""

"""
Variáveis Globais e Locais

    Globais:
        Descrição: Acessíveis de qualquer lugar no programa.
        Exemplo: variavel_global = "global"
                 def funcao():
                     print(variavel_global)

    Locais:
        Descrição: Só existem dentro de um escopo específico (ex.: dentro de uma função).
        Exemplo: def funcao():
                     variavel_local = "local"
                     print(variavel_local)
"""

"""
Variáveis Mutáveis e Imutáveis

    Mutáveis:
        Descrição: Pode ser alterado após a sua criação.
        Exemplo: lista_mutavel = [1, 2, 3]
                 lista_mutavel.append(4)

    Imutáveis:
    Descrição: Não pode ser alterado após a sua criação.
    Exemplo: texto_imutavel = "Python"
             texto_imutavel += " é uma linguagem de programação"
"""

"""
Variáveis de Referência
    Descrição: Armazenam referências para objetos em vez de valores diretos.
    Exemplo: lista1 = [1, 2, 3]
             lista2 = lista1
             lista2.append(4)
             print(lista2) # Output: [1, 2, 3, 4]  
"""

"""
Variáveis Estáticas
    Descrição: São associadas a uma classe (não a instâncias) e mantêm o mesmo valor em todas as instâncias.
    Exemplo em Python (com classes): class Pessoa:
                                     populacao = 0  # Variável estática

                                        def __init__(self, nome):
                                            self.nome = nome
                                            Pessoa.populacao += 1

                                     pessoa1 = Pessoa("Artur")
                                     pessoa2 = Pessoa("Maria")
                                     print(Pessoa.populacao)  # Resultado: 2
"""

"""
Variáveis Envolvendo Outros Tipos de Dados
    Data e Hora:
        Descrição: Armazenam informações de tempo.
        Exemplo: from datetime import datetime
                 agora = datetime.now()
                 print(agora)
"""