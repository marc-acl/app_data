import pandas as pd
import plotly.express as px

# Ejemplo con muchas acciones
list1 = ["axa", 'AAPL', 'MSFT' ]
list2 =[1, 2, 3]
list3 = [4, 5, 6]
data = {
    "Acción": list1,  # 50 acciones
    "Precio Inicial": list2,
    "Precio Final": list3,
}
df = pd.DataFrame(data)
df["Variación %"] = ((df["Precio Final"] - df["Precio Inicial"]) / df["Precio Inicial"]) * 100

# Ordenar por variación descendente
df = df.sort_values("Variación %", ascending=True)

# Gráfico de barras horizontales
fig = px.bar(
    df,
    x="Variación %",
    y="Acción",
    orientation='h',
    text="Variación %",
    color="Variación %",
    color_continuous_scale="country",
)

# Mejoras estéticas
fig.update_traces(texttemplate="%{text:.2f}%", textposition='outside')
fig.update_layout(
    template="plotly_white",
    title="Variación porcentual de acciones",
    title_x=0.5,
    yaxis=dict(autorange="reversed"),  # la mayor arriba
    coloraxis_showscale=False,
    height=800  # ajusta según tu espacio disponible
)

fig.show()
