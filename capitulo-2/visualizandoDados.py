# objetivo do codigo a seguir e explorar e visualizar os dados do banco de dados
from conjuntoTeste import *
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np 
import matplotlib.pyplot as plt

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, 
             s=housing["population"]/100, label="population", figsize=(10,7),
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)

corr_matrix=housing.corr(numeric_only=True)
print(corr_matrix["median_house_value"].sort_values(ascending=False))
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()