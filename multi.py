import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Cargar los datos
df = pd.read_csv(r"C:\Users\dmarc\Downloads\mindfmulti.csv", encoding='utf-8', sep=';')
# Mostrar los nombres de las columnas reales
print("Columnas encontradas en el CSV:")
print(df.columns.tolist())

# (Opcional) ver las primeras filas
print("\nPrimeras filas del archivo:")
print(df.head())
X = df[['x1', 'x2', 'x3']]
X = sm.add_constant(X)  # añade la constante (intercepto)
# Modelo de regresión (opcional, para tener contexto)
# 4️⃣ Calcular el VIF para cada variable
vif_data = pd.DataFrame()
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i)
                   for i in range(X.shape[1])]

print(vif_data)

print(df[['x1', 'x2', 'x3']].corr())


