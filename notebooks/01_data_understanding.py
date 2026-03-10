# Importamos las librerías principales para análisis de datos

import pandas as pd          # Librería principal para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para gráficos
import seaborn as sns        # Librería para visualizaciones más avanzadas

#Carga de dataset
df = pd.read_csv('C:/Users/flors/Desktop/Flor/Proyecto E-Commerce/data/ecommerce_dataset.csv')

#Vista inicial, coloco "print" porque no estoy trabajando en Jupiter
print(df.head())
print(df.columns)
print(df.info()) #tipos de datos, valores nulos, numero de registros

#elimina valores nulos 
df = df.dropna()

#Crea columna de ingresos
df["Ingresos"] = df["quantity"] * df["price"]

#Productos mas vendidos
top_productos = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
print(top_productos.head(10))

#Productos mas rentables
top_Ingresos = df.groupby("product_name")["Ingresos"].sum().sort_values(ascending=False)
print(top_Ingresos.head(10))

#Ventas por categoria
ventas_categoria = df.groupby("category_name")["Ingresos"].sum()
print(ventas_categoria)

#Ventas por ciudad
ventas_ciudad = df.groupby("city")["Ingresos"].sum().sort_values(ascending=False)
print(ventas_ciudad)

#Visualizaciones
import matplotlib.pyplot as plt

top_productos.head(10).plot(kind="bar")

plt.title("Top 10 Productos Más Vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")

plt.show()