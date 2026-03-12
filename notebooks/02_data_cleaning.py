#Importamos librerias
import pandas as pd
import numpy as np

#Carga de dataset
df = pd.read_csv('data/ecommerce_dataset.csv')

#------------------------------------------------------------

#eliminacion de valores nulos 
df = df.dropna()

#Eliminacion de duplicados
df = df.drop_duplicates()

#Eliminacion de valores negativos
df = df[(df["quantity"] > 0) & (df["price"] > 0)]

#--------------------------------------------------------

#Creacion de la variable "Ingresos"
df["Ingresos"] = df["quantity"] * df["price"]

print("Tipos de datos:")
print(df.dtypes)

print("Shape del dataset limpio:", df.shape)

#--------------------------------------------------------------

#Exportar dataset limpio
df.to_csv('data/ecommerce_dataset.csv', index=False)

