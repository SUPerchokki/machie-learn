# codigo feito para retornar diversos informes sobre os dados obtidos

import os
import tarfile
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt 

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def load_housing_data(housing_path =HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
print(housing.head()) # 5 primeiras linhas
print(housing.info()) #informações sobre cada coluna
print(housing["ocean_proximity"].value_counts()) # Vezes que um atributo da coluna se repete
print(housing.describe()) # exibe informações uteis da tabela

housing.hist(bins=50)
plt.show()


