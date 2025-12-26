import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt




# Cargar los datos
df = pd.read_csv(r"C:\Users\dmarc\Downloads\modelo_dummy.csv", encoding='utf-8', sep=';')
# Ver las primeras filas
print(df.head())
print(df.info())
print(df.describe())

X = df[['x1']]
y = df[['y']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("Intercepto:", modelo.intercept_)
print("Coeficientes:", modelo.coef_)

# Relacionar coeficientes con nombres de columnas
for col, coef in zip(X.columns, modelo.coef_):
    print(f"{col}: {coef}")


y_pred = modelo.predict(X_test)

print("R²:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))






# var_muestral = stats.variance(x['x1'])
# var_poblacional = stats.pvariance(x['x1'])
# var_muestral2 = stats.variance(y['y'])
# var_poblacional2 = stats.pvariance(y['y'])
# print(f"Varianza muestral: {var_muestral2}")    
# print(f"Varianza poblacional: {var_poblacional2}")
# print(f"Varianza muestral: {var_muestral}")    
# print(f"Varianza poblacional: {var_poblacional}")


#Modelo: Y = β₀ + β₁X + ε
# Agregar constante para el intercepto
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


residuals = model.resid
fitted = model.fittedvalues

plt.scatter(fitted, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Valores ajustados')
plt.ylabel('Residuos')
plt.title('Residuos vs Valores ajustados')
plt.show()



