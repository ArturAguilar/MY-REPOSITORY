# Importando o módulo numpy, utilizado para realizar operações matemáticas avançadas e manipulação de arrays
import numpy as np

# Dados sobre as edições da Copa do Mundo FIFA, contendo país-sede, ano, e a média de gols por jogo
dados = """
Uruguay 1930 FIFA World Cup -- 4.375 

Italy 1934 FIFA World Cup -- 4.12

France 1938 FIFA World Cup -- 4.67

Brazil 1950 FIFA World Cup -- 4

Switzerland 1954 FIFA World Cup -- 5.38 

Sweden 1958 FIFA World Cup -- 3.6

Chile 1962 FIFA World Cup -- 2.79

England 1966 FIFA World Cup -- 2.79

Mexico 1970 FIFA World Cup -- 2.97

West Germany 1974 FIFA World Cup -- 2.55

Argentina 1978 FIFA World Cup -- 2.68

Spain 1982 FIFA World Cup -- 2.81

Mexico 1986 FIFA World Cup -- 2.54

Italy 1990 FIFA World Cup -- 2.21

United States 1994 FIFA World Cup -- 2.71

France 1998 FIFA World Cup -- 2.67

South Korea and Japan 2002 FIFA World Cup -- 2.52

Germany 2006 FIFA World Cup -- 2.30

South Africa 2010 FIFA World Cup -- 2.27

Brazil 2014 FIFA World Cup -- 2.67

Russia 2018 FIFA World Cup -- 2.64

Qatar 2022 FIFA World Cup --  2.69"""

# Exemplo de um único registro presente nos dados (não é utilizado no restante do código)
x = 'Uruguay 1930 FIFA World Cup -- 4.375'

# Criando uma lista com as médias de gols extraídas dos dados.
# Para cada linha separada por dois "Enter" (\n\n), obtemos a parte que vem após o separador ' -- ' e convertendo-a em número decimal (float)
media_de_gols = [float(x.split(' -- ')[1]) for x in dados.split("\n\n")]

# Exibindo a lista de médias de gols por edição
print(media_de_gols)

# Calculando a média geral das médias de gols utilizando a função mean() do numpy
y = np.array(media_de_gols).mean()

# Exibindo a média geral de gols por jogo ao longo das edições da Copa do Mundo
print(y)