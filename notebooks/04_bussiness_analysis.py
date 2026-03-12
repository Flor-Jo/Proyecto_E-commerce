#Importamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ecommerce_dataset.csv')

#------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------

#Visualizaciones
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12,6)
palette = sns.color_palette("Blues_r")

#Grafico top 10 Productos
top_productos.plot()
top_products = df.groupby("product_name")["Ingresos"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    palette="Blues_r"
)

plt.title("Top 10 productos", fontsize=16)
plt.xlabel("Ingrsos")
plt.ylabel("Productos")

plt.tight_layout()

plt.show()

#Grafico Top Ciudades 

city_sales = df.groupby("city")["Ingresos"].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))

sns.barplot(
    x=city_sales.values,
    y=city_sales.index,
    palette="viridis"
)

plt.title("Ingresos por ciudad", fontsize=16)
plt.xlabel("Ingresos")
plt.ylabel("Ciudad")

plt.show()

#Grafico de ingresos por categoria
category_sales = df.groupby("category_name")["Ingresos"].sum()

plt.figure(figsize=(10,6))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    palette="magma"
)

plt.title("Ingresos por categoria")
plt.xticks(rotation=45)

plt.show()

#----------------------------------------------------------------------------------------------------

#Analisis 1: Un pequeño número de productos genera la mayor parte del ingreso?
producto_Ingreso = df.groupby("product_name")["Ingresos"].sum().sort_values(ascending=False)

cum_porcentaje = producto_Ingreso.cumsum() / producto_Ingreso.sum() * 100

#Visualizacion
plt.figure(figsize=(12,6))

plt.plot(cum_porcentaje.values)

plt.axhline(80, color="red", linestyle="--")

plt.title("Pareto Analysis of Product Revenue")

plt.xlabel("Productos")
plt.ylabel("Acumulacion de ingresos por %")

plt.show()

#-----------------------------------------------------------------------------------------------------------

#Analisis 2: Cuanto gasta en promedio un cliente por compra?
average_ticket = df["Ingresos"].mean()

#----------------------------------------------------------------------------------------------------------

#Analisis 3: Los productos mas caros venden menos?
product_stats = df.groupby("product_name").agg({
    "price":"mean",
    "quantity":"sum"
})

plt.figure(figsize=(10,6))

sns.scatterplot(
    x=product_stats["price"],
    y=product_stats["quantity"]
)

plt.title("Price vs Quantity Sold")

plt.xlabel("Average Price")
plt.ylabel("Total Quantity Sold")

plt.show()

#---------------------------------------------------------------------------------------------------------------

#Analisis 4: Ticket promedio
average_ticket = df["Ingresos"].mean()

print("Ticket promedio:", average_ticket)

#---------------------------------------------------------------------------------------------------------------

#Analisis 5: Ingresos totales
total_ingresos = df["Ingresos"].sum()

print("Ingresos totales:", total_ingresos)

#-----------------------------------------------------------------------------------------------------------------

#Analisis 6: Clientes mas importantes
top_customers = df.groupby("customer_id")["Ingresos"].sum().sort_values(ascending=False)

print(top_customers.head(10))

#---------------------------------------------------------------------------------------------------------------

#Analisis 7: Segmentacion de clientes
rfm = df.groupby("customer_id").agg({
    "Ingresos": ["sum", "mean"],
    "quantity": "sum"
})

print(rfm.head())

#-------------------------------------------------------------------------------------------------------------

#Analisis 8: Estacionalidad de ventas

df["order_date"] = pd.to_datetime(df["order_date"])

df["month"] = df["order_date"].dt.month

ventas_mes = df.groupby("month")["Ingresos"].sum()

ventas_mes.plot()