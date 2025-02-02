import numpy as np  # Biblioteca NumPy para operações matemáticas em vetores/matrizes
import math  # Biblioteca math para funções trigonométricas e conversão de ângulos

# Função para transladar um vetor (movê-lo)
def translacao(vetor, deslocamento):
    """
    Aplica uma translação (movimento) ao vetor.
    A translação é feita somando o vetor de deslocamento ao vetor original.
    """
    return vetor + deslocamento

# Exemplo de vetor em R^2
vetor = np.array([1, 2])  # Vetor original

# Deslocamento (movimento) desejado
deslocamento = np.array([3, 4])  # Vetor de deslocamento

# Aplicando a translação
vetor_transladado = translacao(vetor, deslocamento)

# Exibindo os vetores
print("Vetor original:", vetor)
print("Vetor após translação:", vetor_transladado)


# Função para rotacionar um vetor
def rotacao(vetor, angulo):
    """
    Aplica uma rotação ao vetor, no sentido anti-horário, com um ângulo dado em graus.
    Utiliza uma matriz de rotação 2D.
    """
    # Convertendo o ângulo de graus para radianos (necessário para funções trigonométricas)
    angulo_rad = math.radians(angulo)
    
    # Matriz de rotação em 2D
    matriz_rotacao = np.array([[math.cos(angulo_rad), -math.sin(angulo_rad)],
                               [math.sin(angulo_rad), math.cos(angulo_rad)]])
    
    # Multiplicando a matriz de rotação pelo vetor para obter o vetor rotacionado
    vetor_rotacionado = np.dot(matriz_rotacao, vetor)
    return vetor_rotacionado

# Exemplo de vetor em R^2
vetor = np.array([1, 0])  # Vetor original

# Ângulo de rotação (em graus)
angulo = 90  # Rotação no sentido anti-horário

# Aplicando a rotação
vetor_rotacionado = rotacao(vetor, angulo)

# Exibindo os vetores
print("Vetor original:", vetor)
print(f"Vetor após rotação de {angulo}°:", vetor_rotacionado)


# Função para refletir um vetor no eixo X
def reflexao_x(vetor):
    """
    Reflete o vetor no eixo X.
    Utiliza uma matriz de reflexão que inverte o sinal do componente Y do vetor.
    """
    # Matriz de reflexão no eixo X
    matriz_reflexao_x = np.array([[1, 0],
                                  [0, -1]])
    
    # Multiplicando a matriz de reflexão pelo vetor para obter o vetor refletido
    vetor_refletido = np.dot(matriz_reflexao_x, vetor)
    return vetor_refletido

# Exemplo de vetor em R^2
vetor = np.array([2, 3])  # Vetor original

# Aplicando a reflexão no eixo X
vetor_refletido = reflexao_x(vetor)

# Exibindo os vetores
print("Vetor original:", vetor)
print("Vetor após reflexão no eixo X:", vetor_refletido)