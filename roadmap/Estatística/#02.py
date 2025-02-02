import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do dataset Titanic
df_titanic = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Estatística/planilhas/titanic.csv')

# a) Exibe as primeiras linhas do dataset
a = df_titanic.head()
print("Primeiras linhas do dataset:\n", a)

# b) Mostra informações gerais do dataset
b = df_titanic.info()

# c) Valores únicos na coluna 'pclass'
c = df_titanic["pclass"].unique()
print("\nClasses únicas de passageiros (pclass):", c)

# d) Valores únicos na coluna 'survived'
d = df_titanic["survived"].unique()
print("\nValores únicos de 'survived':", d)

# e) Valores únicos na coluna 'embarked'
e = df_titanic["embarked"].unique()
print("\nPortos de embarque únicos (embarked):", e)

# f) Valores únicos na coluna 'age'
f = df_titanic["age"].unique()
print("\nIdades únicas (age):", f)

# g) Proporção de cada classe de passageiros (pclass)
g = df_titanic["pclass"].value_counts(normalize=True)
print("\nProporção de passageiros por classe (pclass):\n", g)

# h) Proporção de sobreviventes (survived)
h = df_titanic["survived"].value_counts(normalize=True)
print("\nProporção de sobrevivência (survived):\n", h)

# i) Taxa média de sobrevivência
i = df_titanic["survived"].mean()
print("\nTaxa média de sobrevivência:", i)

# j) Taxa média de sobrevivência na primeira classe
k = df_titanic.query("pclass == 1")["survived"].mean()
print("\nTaxa de sobrevivência na 1ª classe (pclass == 1):", k)

# k) Taxa média de sobrevivência por classe
l = df_titanic.groupby("pclass")[["survived"]].mean()
print("\nTaxa média de sobrevivência por classe (pclass):\n", l)