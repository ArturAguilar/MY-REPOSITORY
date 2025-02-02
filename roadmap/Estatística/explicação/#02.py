"""
O que é uma variável aleatória?
    Uma variável aleatória é um conceito usado principalmente em estatística e probabilidade. Ela representa uma quantidade cujo valor depende do resultado de um experimento aleatório. Ou seja, o valor de uma variável aleatória é incerto até que o experimento seja realizado.

    Existem dois tipos principais de variáveis aleatórias:
        Variável Aleatória Discreta
            Descrição: Assume valores específicos e contáveis (inteiros).
            Exemplos: Número de vezes que um dado cai em "6" em 10 lançamentos, número de chamadas recebidas em um call center em 1 hora.

        Variável Aleatória Contínua
            Descrição: Pode assumir qualquer valor em um intervalo contínuo.
            Exemplos: Tempo que um cliente espera na fila, altura de uma pessoa selecionada aleatoriamente.
"""

"""
Evento e Espaço Amostral
    Evento (A): Um ou mais resultados que nos interessam (exemplo: tirar um número par ao lançar um dado).
    Espaço amostral (S): O conjunto de todos os resultados possíveis (exemplo: {1, 2, 3, 4, 5, 6} para um dado de 6 faces).
"""

"""
Probabilidade Simples
    Se lançarmos um dado comum (6 lados), qual a probabilidade de sair um número 4?

    Evento favorável: {4} (1 resultado favorável).
    Espaço amostral: {1, 2, 3, 4, 5, 6} (6 resultados possíveis).

    p(4) = 1/6 = 0.1667 = 16.67%
"""

"""
Probabilidade de Múltiplos Eventos
    Se lançarmos um dado, qual a probabilidade de sair um número par?

    Evento favorável: {2, 4, 6} (3 resultados favoráveis).
    Espaço amostral: {1, 2, 3, 4, 5, 6}.

    p(par) = 3/6 = 0.5 = 50%
"""

"""
Probabilidade Condicional
    Se sabemos que um evento já ocorreu, usamos a probabilidade condicional para calcular as chances de outro evento.

    p(A | B) = p(A e B) / p(B)

    Exemplo: Em uma turma de 20 alunos, 12 gostam de matemática e 8 gostam de estatística. Se sabemos que um aluno gosta de matemática, qual a probabilidade de ele também gostar de estatística?

    p(matemática) = 12/20
    p(estatística) = 8/20
    p(matemática e estatística) = 5/20
    p(estatística | matemática) = p(estatística e matemática) / p(matemática) = 5/20 / 12/20 = 5/12 = 0.4167 = 41.67%
"""

# Exemplo 1: Probabilidade de sair um número par ao lançar um dado
espaco_amostral = [1, 2, 3, 4, 5, 6]  # Espaço amostral
eventos_favoraveis = [2, 4, 6]         # Eventos favoráveis (números pares)

probabilidade = len(eventos_favoraveis) / len(espaco_amostral)
print(f"Probabilidade de sair um número par: {probabilidade:.2f}")

# Exemplo 2: Probabilidade condicional
alunos = 20
gostam_matematica = 12
gostam_estatistica = 8
gostam_ambos = 5

prob_condicional = gostam_ambos / gostam_matematica
print(f"Probabilidade de gostar de estatística dado que gosta de matemática: {prob_condicional:.2f}")

"""
Probabilidade de Eventos Independentes
    Dois eventos são independentes quando a ocorrência de um não afeta a probabilidade do outro.

    Exemplo: Se lançarmos dois dados, qual a probabilidade de ambos saírem com o número 6?
        Probabilidade de um dado sair com 6: p(6) = 1/6
        Probabilidade de dois dados saírem com 6: p(6) * p(6) = 1/6 * 1/6 = 1/36 = 0.0278 = 2.78%
"""

"""
Probabilidade de Eventos Mutuamente Exclusivos
    Dois eventos são mutuamente exclusivos se não podem acontecer ao mesmo tempo.

    Exemplo: Qual a probabilidade de sair um número 2 ou 5 ao lançar um dado?
        Eventos: {2} e {5} (não podem ocorrer juntos).
        Soma das probabilidades: p(2) + p(5) = 1/6 + 1/6 = 2/6 = 1/3 = 0.3333 = 33.33%
"""

"""
Probabilidade de Eventos Não Mutuamente Exclusivos
    Se os eventos podem ocorrer ao mesmo tempo, usamos a fórmula: p(A ou B) = p(A) + p(B) - p(A e B)

    Exemplo: Em um baralho de 52 cartas, qual a probabilidade de tirar uma carta que seja rei ou de naipe copas?
        p(Rei) = 4/52
        p(Copas) = 13/52
        p(Rei e Copas) = 1/52
        p(Rei ou Copas) = p(Rei) + p(Copas) - p(Rei e Copas) 
        p(Rei ou Copas) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13 = 0.3077 = 30.77%
"""

"""
Probabilidade Total
    Se um evento pode acontecer de diferentes formas, usamos a probabilidade total.

    Exemplo: Um aluno tem 60% de chance de estudar e 40% de chance de não estudar para uma prova. Se ele estuda, tem 90% de chance de passar; se não estuda, tem apenas 30%. Qual é a probabilidade total de ele passar?
        p(Passar) = p(Estudar) * p(Passar|Estudar) + p(Não estudar) * p(Passar|Não estudar)
        p(Passar) = 0.60 * 0.90 + 0.40 * 0.30 = 0.54 + 0.12 = 0.66 = 66%
"""

"""
Probabilidade Bayesiana
    A probabilidade bayesiana é usada para atualizar a probabilidade de um evento com base em novas informações. A fórmula é:
    p(A|B) = p(B|A) * p(A) / p(B)

    Exemplo: Suponha que 1% de uma população tem uma doença. Um teste detecta corretamente a doença em 95% dos casos positivos, mas dá um falso positivo em 5% dos casos negativos. Qual a probabilidade de uma pessoa estar realmente doente se o teste for positivo?

        p(Doente) = 0.01
        p(Não doente) = 0.99
        p(Positivo|Doente) = 0.95
        p(Negativo|Não doente) = 0.95

    A probabilidade total de o teste ser positivo é:

        p(Positivo) = p(Positivo|Doente) * p(Doente) + p(Positivo|Não doente) * p(Não doente)
        p(Positivo) = 0.95 * 0.01 + 0.05 * 0.99 = 0.0595 + 0.0495 = 0.059

    Agora, usamos a fórmula de Bayes:

        p(Doente|Positivo) = p(Positivo|Doente) * p(Doente) / p(Positivo)
        p(Doente|Positivo) = 0.95 * 0.01 / 0.059 = 0.0161 = 1.61%
"""

# Exemplo 1: Probabilidade de dois números 6 (eventos independentes)
p_6 = 1/6
prob_6_e_6 = p_6 * p_6
print(f"Probabilidade de dois 6: {prob_6_e_6:.4f}")

# Exemplo 2: Probabilidade de rei ou copas
p_rei = 4/52
p_copas = 13/52
p_rei_e_copas = 1/52
p_rei_ou_copas = p_rei + p_copas - p_rei_e_copas
print(f"Probabilidade de rei ou copas: {p_rei_ou_copas:.4f}")

# Exemplo 3: Probabilidade total
p_estudar = 0.6
p_nao_estudar = 0.4
p_passar_estudar = 0.9
p_passar_nao_estudar = 0.3
p_passar = p_estudar * p_passar_estudar + p_nao_estudar * p_passar_nao_estudar
print(f"Probabilidade de passar na prova: {p_passar:.2f}")

# Exemplo 4: Probabilidade Bayesiana
p_doente = 0.01
p_nao_doente = 0.99
p_teste_pos_doente = 0.95
p_teste_pos_nao_doente = 0.05
p_teste_pos = (p_teste_pos_doente * p_doente) + (p_teste_pos_nao_doente * p_nao_doente)
p_doente_teste_pos = (p_teste_pos_doente * p_doente) / p_teste_pos
print(f"Probabilidade de estar doente dado teste positivo: {p_doente_teste_pos:.4f}")