import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/flors/Desktop/Flor/Proyecto E-Commerce/data/ecommerce_dataset.csv')


#Distribucion de precios
plt.figure(figsize=(10,6))

sns.histplot(["price"], bins=30)

plt.title("Distribucion de precios")
plt.show()

#Distribucion de cantidades
sns.histplot(["quantity"])

#Correlaciones
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
