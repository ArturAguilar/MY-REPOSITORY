import numpy as np
import matplotlib.pyplot as plt

# Definindo o vetor original
v = np.array([1, 1])  # O vetor original é [1, 1]

# Definindo as transformações lineares
theta = np.pi / 4  # Ângulo de rotação em radianos (45 graus)
tranformations = [
    ("rotação", np.array([[np.cos(theta), -np.sin(theta)],
                          [np.sin(theta), np.cos(theta)]])),  # Matriz de rotação
    
    ("escalonamento", np.array([[2, 0], 
                                [0, 0.5]])),  # Matriz de escalonamento (amplia o vetor no eixo x e diminui no eixo y)

    ("reflexão", np.array([[1, 0],
                           [0, -1]])),  # Matriz de reflexão (reflete o vetor no eixo x)

    ("cisalhamento", np.array([[1, 0.5],
                               [0, 1]]))  # Matriz de cisalhamento (aplica um deslocamento no eixo x proporcional ao valor de y)
]

# Laço para aplicar e exibir as transformações
for i, (name, T) in enumerate(tranformations, start=1):
    plt.subplot(2, 2, i)  # Organizando os subgráficos em uma grade 2x2
    plt.title(name)  # Adicionando o título do gráfico
    
    # Calculando o vetor transformado
    transformed_v = np.dot(T, v)  
    
    # Plotando o vetor original e o vetor transformado
    plt.quiver([0, 0], [0, 0], [v[0], transformed_v[0]], [v[1], transformed_v[1]], angles='xy', scale_units='xy', scale=1, color='blue')
    
    # Ajustando limites e grid do gráfico
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)
    plt.grid(True)

# Ajustando layout para evitar sobreposição
plt.tight_layout()

# Exibindo os gráficos
plt.show()