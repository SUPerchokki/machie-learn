# objetivo do codigo a seguir e explorar e visualizar os dados do banco de dados
from conjuntoTeste import *
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, 
             s=housing["population"]/100, label="population", figsize=(10,7),
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
plt.show()
