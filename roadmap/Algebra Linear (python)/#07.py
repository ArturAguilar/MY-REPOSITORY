import matplotlib.pyplot as plt

# Definindo o vetor na base canônica
vetor_x = [1, 0]  # Vetor unitário ao longo do eixo x
vetor_y = [0, 1]  # Vetor unitário ao longo do eixo y

# Plotando os vetores na base canônica
plt.figure()  # Criando uma nova figura para o gráfico

# Plotando o vetor ao longo do eixo x
plt.quiver(0, 0, vetor_x[0], vetor_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='eixo x')
# Plotando o vetor ao longo do eixo y
plt.quiver(0, 0, vetor_y[0], vetor_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='eixo y')

# Configurações adicionais do gráfico
plt.xlim(-1, 1)  # Definindo os limites do eixo x
plt.ylim(-1.1, 1)  # Definindo os limites do eixo y (um pouco além de -1 e 1 para melhor visualização)
plt.xlabel('x')  # Rótulo do eixo x
plt.ylabel('y')  # Rótulo do eixo y
plt.axhline(0, color='black', linewidth=0.5)  # Linha do eixo x
plt.axvline(0, color='black', linewidth=0.5)  # Linha do eixo y
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adicionando uma grade com linhas tracejadas
plt.gca().set_aspect('equal', adjustable='box')  # Garantindo que os eixos tenham o mesmo comprimento
plt.legend()  # Adicionando legenda ao gráfico
plt.title("Base Canônica")  # Título do gráfico

# Exibindo o gráfico
plt.show()  # Mostra o gráfico gerado