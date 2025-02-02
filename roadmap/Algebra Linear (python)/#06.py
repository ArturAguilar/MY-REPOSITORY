import matplotlib.pyplot as plt

# Definindo o vetor (2,2)
vetor = [2, 2]

# Definindo as origens para o vetor
origens = [(0, -1), (0, 1), (0, 0), (0, 2)]  # Listagem de diferentes pontos de origem para o vetor

# Extraindo as coordenadas x e y das origens
origem_x = [origem[0] for origem in origens]  # Extração das coordenadas x de cada origem
origem_y = [origem[1] for origem in origens]  # Extração das coordenadas y de cada origem

# Plotando o vetor (2,2) com as origens especificadas
plt.figure()  # Criando uma nova figura para o gráfico
plt.quiver(origem_x, origem_y, [vetor[0]]*len(origem_x), [vetor[1]]*len(origem_y), 
           angles='xy', scale_units='xy', scale=1, color='g')  # Plotando o vetor a partir de cada origem

# Configurações adicionais do gráfico
plt.xlim(-1, 5)  # Definindo os limites do eixo x
plt.ylim(-2, 5)  # Definindo os limites do eixo y
plt.xlabel('x')  # Rótulo do eixo x
plt.ylabel('y')  # Rótulo do eixo y
plt.axhline(0, color='black', linewidth=0.5)  # Linha do eixo x
plt.axvline(0, color='black', linewidth=0.5)  # Linha do eixo y
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adicionando uma grade com linhas tracejadas
plt.gca().set_aspect('equal', adjustable='box')  # Garantindo que os eixos tenham o mesmo comprimento
plt.title("Um vetor com diferentes pontos de origem")  # Título do gráfico

# Exibindo o gráfico
plt.show()  # Mostra o gráfico gerado