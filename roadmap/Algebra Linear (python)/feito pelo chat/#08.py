import numpy as np  # Importando a biblioteca NumPy para operações vetoriais

# Definindo os vetores a e b
a = np.array([3, 4])  # Vetor 'a' no espaço R^2
b = np.array([1, 2])  # Vetor 'b' no espaço R^2

# Calculando o produto escalar entre 'a' e 'b'
produto_escalar = np.dot(a, b)  # O produto escalar é a soma dos produtos das componentes correspondentes dos vetores
print("Produto escalar de a e b:", produto_escalar)  # Exibindo o valor do produto escalar

# Calculando as normas (módulos) dos vetores
norma_a = np.linalg.norm(a)  # Norma de 'a' é a raiz quadrada da soma dos quadrados das componentes de 'a'
norma_b = np.linalg.norm(b)  # Norma de 'b' é a raiz quadrada da soma dos quadrados das componentes de 'b'

# Calculando o cosseno do ângulo entre os vetores usando o produto escalar
cos_theta = produto_escalar / (norma_a * norma_b)  # A fórmula para o cosseno do ângulo entre os vetores

# Calculando o ângulo entre os vetores em radianos
angulo_rad = np.arccos(cos_theta)  # np.arccos retorna o ângulo cujo cosseno é 'cos_theta'

# Convertendo o ângulo para graus
angulo_deg = np.degrees(angulo_rad)  # Convertendo o ângulo de radianos para graus
print(f"Ângulo entre os vetores (em graus): {angulo_deg:.2f}°")  # Exibindo o ângulo em graus, com 2 casas decimais