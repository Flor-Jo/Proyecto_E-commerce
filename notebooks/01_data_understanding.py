#En este script realizamos una exploracion inicial del dataset
#para comprender su estructura, variables y posibles problemas.

# Importamos las librerías principales para análisis de datos

import pandas as pd          # Librería principal para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para gráficos
import seaborn as sns        # Librería para visualizaciones más avanzadas

#Carga de dataset
df = pd.read_csv('data/ecommerce_dataset.csv')

#----------------------------------------------------------

#Vista inicial. Coloco "print" porque no estoy trabajando en Jupiter
print("Primeras filas del dataset")
print(df.head())

print("\nColumnas del dataset:")
print(df.columns)

print("\nInformación general del dataset:")
print(df.info()) #tipos de datos, valores nulos, numero de registros

print("\nEstadísticas descriptivas:")
print(df.describe()) 

#-------------------------------------------------------

print("\nValores nulos por columna:")
print(df.isnull().sum())

#elimina valores nulos 
df = df.dropna()

#--------------------------------------------------------

#Crea una nueva columna de ingresos
df["Ingresos"] = df["quantity"] * df["price"]

#--------------------------------------------------------

#Productos mas vendidos
top_productos = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)

print("\nTop 10 productos màs vendidos:")
print(top_productos.head(10))

#--------------------------------------------------------

#Productos mas rentables
top_Ingresos = df.groupby("product_name")["Ingresos"].sum().sort_values(ascending=False)

print("\nTop 10 productos con mayor ingreso:")
print(top_Ingresos.head(10))

#-----------------------------------------------------------

#Ventas por categoria
ventas_categoria = df.groupby("category_name")["Ingresos"].sum()

print("\nIngresos por categoría:")
print(ventas_categoria)

#---------------------------------------------------------------

#Ventas por ciudad
ventas_ciudad = df.groupby("city")["Ingresos"].sum().sort_values(ascending=False)

print("\nIngresos por ciudad:")
print(ventas_ciudad)

#--------------------------------------------------------

#Visualizacion: Top productos

plt.figure(figsize=(10,6))
top_productos.head(10).plot(kind="bar")

plt.title("Top 10 Productos Más Vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")

plt.tight_layout()

plt.show()