# Importando bibliotecas necessárias
import pandas as pd  # Para criar tabelas e manipular dados
import numpy as np   # Para trabalhar com números e cálculos

# Passo 1: Tipos de dados
# Dados categóricos (nominais)
categorias = ['Azul', 'Verde', 'Azul', 'Vermelho', 'Verde', 'Azul', 'Amarelo']

# Dados numéricos (quantitativos contínuos e discretos)
dados_continuos = [1.2, 2.3, 3.5, 4.0, 5.1, 3.8, 2.5]
dados_discretos = [1, 2, 2, 3, 4, 4, 5]

# Exibindo os dados
print("Dados Categóricos:", categorias)
print("Dados Contínuos:", dados_continuos)
print("Dados Discretos:", dados_discretos)

# Passo 2: Tabela de Frequência Simples (para dados categóricos)
tabela_frequencia_categorias = pd.Series(categorias).value_counts()
print("\nTabela de Frequência - Dados Categóricos:")
print(tabela_frequencia_categorias)

# Passo 3: Tabela de Frequência para dados numéricos (Distribuição de Frequência)
# Criando faixas de valores (intervalos de classe) para dados contínuos
intervalos = pd.cut(dados_continuos, bins=3)  # Dividimos em 3 faixas
tabela_frequencia_continuos = intervalos.value_counts()

print("\nTabela de Frequência - Dados Contínuos (Intervalos de Classe):")
print(tabela_frequencia_continuos)

# Passo 4: Adicionando colunas de frequências relativas e acumuladas
# Frequência relativa: frequência absoluta dividida pelo total
frequencia_absoluta = tabela_frequencia_continuos
frequencia_relativa = tabela_frequencia_continuos / len(dados_continuos)
frequencia_acumulada = np.cumsum(frequencia_relativa)  # Soma acumulada das frequências relativas

# Montando uma tabela completa com Pandas
tabela_completa = pd.DataFrame({
    'Intervalos': tabela_frequencia_continuos.index.astype(str),  # Convertendo os intervalos para texto
    'Frequência Absoluta': frequencia_absoluta.values,
    'Frequência Relativa (%)': (frequencia_relativa.values * 100).round(2),
    'Frequência Acumulada (%)': (frequencia_acumulada.values * 100).round(2)
})

print("\nTabela Completa de Distribuição de Frequência:")
print(tabela_completa)