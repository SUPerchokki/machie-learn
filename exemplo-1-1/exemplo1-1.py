import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import sklearn.linear_model

# Carregando os dados
oecd_bli = pd.read_csv(r"C:\Users\gabri\OneDrive\Documentos\machine learn\machie-learn\exemplo-1-1\oecd_bli_2015.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")
gdp_per_capita = pd.read_csv(r"C:\Users\gabri\OneDrive\Documentos\machine learn\machie-learn\exemplo-1-1\gdp_per_capita.csv", thousands=',',delimiter='\t', encoding='latin1', na_values="n/a")

# Preparando os dados
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
Y = np.c_[country_stats["Life satisfaction"]]

# Visualizando os dados
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

# Selecionando um modelo linear
model = sklearn.linear_model.LinearRegression()

# Treina o modelo
model.fit(X, Y)

# Efetua a predição para o Chipre
X_new = [[22587]]
print(model.predict(X_new))
