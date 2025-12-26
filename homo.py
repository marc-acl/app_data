import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Los residuos no están dispersos aleatoriamente alrededor de cero (por ejemplo, crecen con X),
# eso confirma que la heterocedasticidad está presente, y por eso es correcto aplicar HC3.

#HC3 no corrige visualmente los residuos, solo ajusta los errores estándar para que las conclusiones
# (p-values, intervalos) sean válidas.



# Cargar los datos
df = pd.read_csv(r"C:\Users\dmarc\Downloads\mindfmulti.csv", encoding='utf-8', sep=';')

# Seleccionar las variables
X = df[['x1', 'x2', 'x3']]
Y = df['y']

# agregamos constante
X_const = sm.add_constant(X)
# Ajustar el modelo de regresión lineal
modelo = sm.OLS(Y, X_const)

# Ajustar el modelo con errores robustos (HC3)
resultado = modelo.fit(cov_type='HC3')

print(resultado.summary())

# Graficar los residuos
residuos = resultado.resid
y_ajustado = resultado.fittedvalues

# Gráfico de residuos
plt.figure(figsize=(8, 6))
plt.scatter(y_ajustado, residuos, color='blue', alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Valores ajustados  (ŷ)')
plt.ylabel('Residuos (û)')
plt.title('Gráfico de Residuos vs Valores Ajustados')


#linea de tenddencia
z = np.polyfit(y_ajustado, residuos, 1)
p = np.poly1d(z)
plt.plot(y_ajustado, p(y_ajustado), color= 'green', label='Línea de tendencia')

plt.grid()
plt.show()

