#Importamos librerias 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ecommerce_dataset.csv')

#----------------------------------------------------------

#Distribucion de precios

plt.figure(figsize=(10,6))

sns.histplot(df["price"], bins=30)

plt.title("Distribucion de precios")
plt.show()

#----------------------------------------------------------

#Distribucion de cantidades
plt.figure(figsize=(10,6))

sns.histplot(df["quantity"], bins=30)

plt.title("Distribución de cantidades")

plt.show()

#------------------------------------------------------------

#Correlaciones entre variables

plt.figure(figsize=(8,6))

sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title("Correlación entre variables")

plt.show()
