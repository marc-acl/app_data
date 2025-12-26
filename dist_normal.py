import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Datos de ejemplo ---
df = pd.read_csv(r"C:\Users\dmarc\Downloads\distnormal.csv", encoding='utf-8', sep=';')

# --- Calcular media y desviación por género ---
stats = df.groupby('Genero')['Frecuencia'].agg(['mean', 'std']).reset_index()

# --- Rango de valores para la curva ---
x = np.linspace(-2, 10, 160)

# --- Graficar la curva normal por género ---
plt.figure(figsize=(8,5))
colores = {1:'blue', 2:'red', 3:'green'}
labels = {1:'Hombres', 2:'Mujeres', 3:'No binario'}

for _, row in stats.iterrows():
    genero = row['Genero']
    media = row['mean']
    desv = row['std']
    y = norm.pdf(x, media, desv)  # densidad de probabilidad
    plt.plot(x, y, color=colores[genero], label=f"{labels[genero]} (σ={desv:.2f})")
    
    # Línea vertical y punto de la media
    plt.axvline(media, color=colores[genero], linestyle='--', alpha=0.7)
    y_media = norm.pdf(media, media, desv)
    plt.scatter(media, y_media, color=colores[genero], s=50)
    plt.text(media, y_media+0.02, f"{media:.2f}", color=colores[genero], ha='center')

    # Líneas ±1 desviación estándar
    for factor in [-1, 1]:
        x_desv = media + factor*desv
        y_desv = norm.pdf(x_desv, media, desv)
        plt.axvline(x_desv, color=colores[genero], linestyle=':', alpha=0.6)
        plt.scatter(x_desv, y_desv, color=colores[genero], s=30)
        plt.text(x_desv, y_desv+0.01, f"{x_desv:.2f}", color=colores[genero], ha='center', fontsize=8)

# --- Detalles finales ---
plt.title('Distribución Normal de Frecuencia de Meditación por Género')
plt.xlabel('Frecuencia de Meditación')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
