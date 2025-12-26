import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv(r"C:\Users\dmarc\Downloads\mindfmulti.csv", encoding='utf-8', sep=';')

# Seleccionar las variables
x = df[['x1', 'x2', 'x3', 'y']]


# Verificar que no hay valores missing
print("Valores missing:")
print(x.isnull().sum())
print(f"\nDimensión: {x.shape}")


#'frecuenciameditamusica (2)' es la variable dependiente
# y 'frecuenciamedita (2)' es una independiente

def prueba_white_multivariante(df, variable_y, variables_x):
    """
    Prueba de White para regresión múltiple
    """
    print(f"Prueba de White: {variable_y} ~ {', '.join(variables_x)}")
    print("=" * 60)
    
    # Preparar datos
    y = df[variable_y]
    X = sm.add_constant(df[variables_x])
    
    # 1. Estimar modelo original
    modelo = sm.OLS(y, X).fit()
    residuos = modelo.resid
    
    print("Modelo original:")
    print(f"R²: {modelo.rsquared:.4f}")
    print(f"N: {len(y)}")
    print("\nCoeficientes:")
    print(modelo.params)
    
    # 2. Prueba de White
    white_test = het_white(residuos, X)
    
    print(f"\nPRUEBA DE WHITE - Resultados:")
    print(f"Estadístico de White (LM): {white_test[0]:.4f}")
    print(f"p-valor: {white_test[1]:.6f}")
    print(f"Estadístico F: {white_test[2]:.4f}")
    print(f"p-valor F: {white_test[3]:.6f}")
    
    # Interpretación
    if white_test[1] < 0.05:
        print("\n🎯 CONCLUSIÓN: Hay evidencia significativa de HETEROCEDASTICIDAD (p < 0.05)")
        print("   → La varianza de los errores NO es constante")
    else:
        print("\n🎯 CONCLUSIÓN: No hay evidencia de heterocedasticidad (p ≥ 0.05)")
        print("   → La varianza de los errores es constante (homocedasticidad)")
    
    return white_test, modelo

def prueba_white_manual_multivariante(df, variable_y, variables_x):
    """
    Implementación manual paso a paso para múltiples variables
    """
    print(f"\nPrueba de White (Manual - Multivariante): {variable_y} ~ {', '.join(variables_x)}")
    print("=" * 60)
    
    y = df[variable_y]
    X_df = df[variables_x]
    X = sm.add_constant(X_df)
    
    # Paso 1: Modelo original
    modelo_original = sm.OLS(y, X).fit()
    residuos = modelo_original.resid
    
    # Paso 2: Residuos al cuadrado
    residuos_cuad = residuos ** 2
    
    # Paso 3: Crear matriz para regresión auxiliar de White
    # Incluye: términos originales, cuadrados y productos cruzados
    X_aux_list = [X]  # first términos originales
    
    # Añadir cuadrados de cada variable
    for var in variables_x:
        X_aux_list.append(df[var]**2)
    
    # Añadir productos cruzados (para 2 o más variables)
    if len(variables_x) >= 2:
        for i in range(len(variables_x)):
            for j in range(i+1, len(variables_x)):
                cross_product = df[variables_x[i]] * df[variables_x[j]]
                X_aux_list.append(cross_product)
    
    X_aux = np.column_stack(X_aux_list)
    
    # Paso 4: Regresión auxiliar
    modelo_auxiliar = sm.OLS(residuos_cuad, X_aux).fit()
    R2_aux = modelo_auxiliar.rsquared
    
    # Paso 5: Estadístico de White
    n = len(y)
    W = n * R2_aux
    
    # Paso 6: p-valor
    grados_libertad = X_aux.shape[1] - 1
    p_valor = 1 - chi2.cdf(W, grados_libertad)
    
    print(f"Detalles del cálculo:")
    print(f"R² regresión auxiliar: {R2_aux:.4f}")
    print(f"Número de observaciones (n): {n}")
    print(f"Estadístico de White (W = n × R²): {n} × {R2_aux:.4f} = {W:.4f}")
    print(f"Grados de libertad: {grados_libertad}")
    print(f"p-valor: {p_valor:.6f}")
    
    if p_valor < 0.05:
        print("🎯 CONCLUSIÓN: Hay evidencia de HETEROCEDASTICIDAD")
    else:
        print("🎯 CONCLUSIÓN: No hay evidencia de heterocedasticidad")
    
    return W, p_valor, grados_libertad

def grafico_heterocedasticidad_multivariante(df, variable_y, variables_x):
    y = df[variable_y]
    X = sm.add_constant(df[variables_x])
    
    modelo = sm.OLS(y, X).fit()
    y_pred = modelo.predict(X)
    residuos = modelo.resid
    
    n_vars = len(variables_x)
    fig, axes = plt.subplots(1, n_vars + 1, figsize=(15, 4))

    # 🔧 Asegurar que axes sea una lista de objetos de tipo Axes
    if isinstance(axes, np.ndarray):
        axes = axes.flatten().tolist()
    else:
        axes = [axes]

    # Gráfico 1: Residuos vs Valores ajustados
    axes[0].scatter(y_pred, residuos, alpha=0.6)
    axes[0].axhline(y=0, color='red', linestyle='--', alpha=0.8)
    axes[0].set_xlabel('Valores Ajustados')
    axes[0].set_ylabel('Residuos')
    axes[0].set_title('Residuos vs Valores Ajustados')
    
    # Gráficos para cada variable independiente
    for i, var in enumerate(variables_x):
        axes[i+1].scatter(df[var], residuos, alpha=0.6)
        axes[i+1].axhline(y=0, color='red', linestyle='--', alpha=0.8)
        axes[i+1].set_xlabel(var)
        axes[i+1].set_ylabel('Residuos')
        axes[i+1].set_title(f'Residuos vs {var}')
    
    plt.tight_layout()
    plt.show()
    
    # También gráfico de residuos estandarizados
    residuos_estandarizados = residuos / np.std(residuos)
    
    plt.figure(figsize=(10, 4))
    plt.scatter(y_pred, residuos_estandarizados, alpha=0.6)
    plt.axhline(y=0, color='red', linestyle='--', label='Línea cero')
    plt.axhline(y=2, color='orange', linestyle=':', label='±2 desviaciones')
    plt.axhline(y=-2, color='orange', linestyle=':')
    plt.xlabel('Valores Ajustados')
    plt.ylabel('Residuos Estandarizados')
    plt.title('Residuos Estandarizados vs Valores Ajustados')
    plt.legend()
    plt.show()

# EJECUTAR EL ANÁLISIS
# Asumiendo que 'frecuenciameditamusica (2)' es Y y 'frecuenciamedita (2)' es X
print("ANÁLISIS DE HETEROCEDASTICIDAD - PRUEBA DE WHITE")
print("=" * 60)

# Usar statsmodels
white_result, modelo = prueba_white_multivariante(
    df, 
    variable_y='y', 
    variables_x=['x1', 'x2', 'x3']
)

# Versión manual
w_manual, p_manual, gl_manual = prueba_white_manual_multivariante(
    df,
    variable_y='y',
    variables_x=['x1', 'x2', 'x3']
)

# Gráficos
grafico_heterocedasticidad_multivariante(
    df,
    variable_y='y',
    variables_x=['x1', 'x2', 'x3']
)