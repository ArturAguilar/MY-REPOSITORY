import numpy as np
import pandas as pd
import seaborn as sns
import scipy
import matplotlib.pyplot as plt

a, b = 0, 10

x = np.linspace(a, b, 10000)
y = np.ones(10000)/(b-a)

plt.plot(x, y)

plt.axvline(x=a, ymax=0.5)
plt.axvline(x=b, ymax=0.5)

plt.show()

c = 30
n_amostras = 100000

medias_amostrais = []

for _ in range(n_amostras):
    amostra = np.random.uniform(low=a, high=b, size=c)
    media_amostral = amostra.mean()
    medias_amostrais.append(media_amostral)
    #print(f"amostra: \n{amostra}\n\nmédia: {media_amostral}")

print(medias_amostrais)

sns.histplot(medias_amostrais)
plt.show()