import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Carga de dataset
df = pd.read_csv('C:/Users/flors/Desktop/Flor/Proyecto E-Commerce/data/ecommerce_dataset.csv')

#elimina valores nulos 
df = df.dropna()

#Crea columna de ingresos
df["Ingresos"] = df["quantity"] * df["price"]

print(df.dtypes)

#Exportar dataset limpio
df.to_csv('C:/Users/flors/Desktop/Flor/Proyecto E-Commerce/data/ecommerce_dataset.csv', index=False)

