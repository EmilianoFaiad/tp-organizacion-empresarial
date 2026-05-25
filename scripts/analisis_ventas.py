
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
datos = pd.read_csv("datos/ventas.csv")

# Mostrar primeras filas
print(datos.head())

# Ventas totales
ventas_totales = datos["sales_amount"].sum()

print("Ventas totales:", ventas_totales)

# Ventas por fecha
ventas_por_fecha = datos.groupby("sales_date")["sales_amount"].sum()

# Crear gráfico
ventas_por_fecha.plot()

plt.title("Ventas por fecha")
plt.xticks(rotation=45)

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado correctamente")
