import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

# Definindo as coordenadas do quadrado original
# O quadrado é definido pelas coordenadas de seus vértices no plano 2D.
# O quadrado tem vértices em (0,0), (1,0), (1,1) e (0,1)
square = np.array([[0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0]])

# Função para plotar o quadrado
def plot_square(ax, square, color, label):
    # Plota o quadrado usando as coordenadas e atribui uma cor e um rótulo
    ax.plot(square[0], square[1], color=color, label=label)

# Criando a figura com 2x2 subgráficos
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(hspace=0.5)  # Ajuste de espaço entre os subgráficos

# Definindo as transformações que serão aplicadas ao quadrado
transformations = [
    ("Rotação", Affine2D().rotate_deg(45)),  # Rotação de 45 graus
    ("Escalonamento", Affine2D().scale(2, 0.5)),  # Escalonamento com fator 2 no eixo x e 0.5 no eixo y
    ("Reflexão", Affine2D().scale(1, -1)),  # Reflexão no eixo x (inversão do eixo y)
    ("Cisalhamento", Affine2D().skew_deg(45, 0))  # Cisalhamento com ângulo de 45 graus no eixo x
]

# Aplicando as transformações e plotando o quadrado em cada subgráfico
for i, (name, transformation) in enumerate(transformations):
    ax = axs.flatten()[i]  # Obtendo o eixo correspondente
    transformed_square = transformation.transform(square.T).T  # Aplica a transformação ao quadrado
    plot_square(ax, transformed_square, color='blue', label='Transformado')  # Plota o quadrado transformado
    plot_square(ax, square, color='red', label='Original')  # Plota o quadrado original
    ax.set_title(name)  # Definir o título do gráfico
    ax.set_xlim(-2, 3)  # Ajuste dos limites do eixo x
    ax.set_ylim(-2, 3)  # Ajuste dos limites do eixo y
    ax.set_aspect('equal')  # Assegura que os eixos x e y tenham a mesma escala
    ax.grid(True)  # Adiciona a grade
    ax.legend()  # Adiciona a legenda

# Exibindo o gráfico
plt.show()