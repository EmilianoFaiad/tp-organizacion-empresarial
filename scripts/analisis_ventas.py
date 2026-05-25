
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
datos = pd.read_csv("datos/ventas.csv")

# Mostrar primeras filas
print("\nPrimeros registros:")
print(datos.head())

# Ventas totales
ventas_totales = datos["sales_amount"].sum()
print("\nVentas totales:", ventas_totales)

# Promedio de ventas
promedio = datos["sales_amount"].mean()
print("Promedio:", promedio)

# Venta máxima
maxima = datos["sales_amount"].max()
print("Venta máxima:", maxima)

# Convertir fechas
datos["sales_date"] = pd.to_datetime(datos["sales_date"])

# Agrupar ventas por mes
ventas_mes = datos.groupby(
    datos["sales_date"].dt.month
)["sales_amount"].sum()

# Crear gráfico
ventas_mes.plot()

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto")

plt.savefig("resultados/grafico_ventas.png")

print("\nGráfico generado correctamente")
