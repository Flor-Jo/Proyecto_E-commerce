# 🛒 Proyecto E-commerce: Análisis de Ventas

## 📌 Descripción del Proyecto

Este proyecto consiste en el análisis de un conjunto de datos de comercio electrónico (E-commerce) con el objetivo de obtener información relevante para la toma de decisiones de negocio.

A través de distintas etapas del proceso analítico se realizó la exploración, limpieza, análisis exploratorio y análisis de negocio utilizando Python y librerías especializadas en análisis de datos.

---

## 🎯 Objetivos

* Comprender la estructura y calidad de los datos.
* Identificar y tratar valores faltantes y registros inconsistentes.
* Analizar el comportamiento de las ventas.
* Detectar los productos y categorías más rentables.
* Identificar patrones de compra y comportamiento de clientes.
* Explorar la estacionalidad de las ventas.

---

## 📂 Estructura del Proyecto

```text
proyecto-ecommerce/
│
├── data/
│   └── ecommerce_dataset.csv
│
├── notebooks/
│   ├── 01_data_understanding.py
│   ├── 02_data_cleaning.py
│   ├── 03_exploratory_analysis.py
│   └── 04_business_analysis.py
│
└── README.md
```

---

## 🛠 Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🔍 Etapas del Análisis

### 1. Comprensión de los Datos (`01_data_understanding.py`)

En esta etapa se realizó una exploración inicial del dataset para conocer:

* Estructura de los datos.
* Variables disponibles.
* Tipos de datos.
* Estadísticas descriptivas.
* Valores faltantes.
* Creación de la variable **Ingresos**.

Además, se identificaron:

* Productos más vendidos.
* Productos con mayores ingresos.
* Ventas por categoría.
* Ventas por ciudad.

---

### 2. Limpieza de Datos (`02_data_cleaning.py`)

Se aplicaron tareas de preparación de datos tales como:

* Eliminación de valores nulos.
* Eliminación de registros duplicados.
* Eliminación de valores inválidos (cantidades o precios negativos).
* Creación de la variable **Ingresos**.

Finalmente, el dataset limpio fue exportado para su posterior análisis.

---

### 3. Análisis Exploratorio de Datos (`03_exploratory_analysis.py`)

Se realizaron visualizaciones para comprender la distribución de las variables:

* Distribución de precios.
* Distribución de cantidades vendidas.
* Matriz de correlación entre variables numéricas.

---

### 4. Análisis de Negocio (`04_business_analysis.py`)

Se desarrollaron distintos análisis orientados a responder preguntas de negocio:

* ¿Cuáles son los productos más vendidos?
* ¿Qué productos generan mayores ingresos?
* ¿Qué ciudades concentran más ventas?
* ¿Qué categorías son más rentables?
* ¿Existe una distribución tipo Pareto (80/20)?
* ¿Cuál es el ticket promedio por compra?
* ¿Quiénes son los clientes más importantes?
* ¿Existen patrones de estacionalidad en las ventas?
* ¿Los productos más caros venden menos unidades?

---

## 📈 Principales Métricas Analizadas

* Ingresos totales.
* Ticket promedio.
* Ingresos por categoría.
* Ingresos por ciudad.
* Top 10 productos.
* Top 10 clientes.
* Segmentación básica de clientes.

---

## 🚀 Cómo ejecutar el proyecto

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-ecommerce
```

Instalar dependencias:

```bash
pip install pandas numpy matplotlib seaborn
```

Ejecutar los scripts en el siguiente orden:

```bash
python notebooks/01_data_understanding.py
python notebooks/02_data_cleaning.py
python notebooks/03_exploratory_analysis.py
python notebooks/04_business_analysis.py
```

---

## 💡 Posibles mejoras futuras

* Implementar segmentación RFM completa (Recency, Frequency y Monetary).
* Incorporar dashboards interactivos con Power BI o Tableau.
* Aplicar modelos de Machine Learning para predicción de ventas.
* Automatizar el pipeline de procesamiento de datos.

---

## 👩‍💻 Autora

**Florencia Salinas**

Estudiante de Ciencia de Datos, Analítica y Testing QA, interesada en transformar datos en información útil para la toma de decisiones.
