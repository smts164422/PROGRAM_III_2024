import matplotlib.pyplot as plt
#Gráfico de linea

#Se establecieron los datos en un diccionario
datos = {'Monaco': 26345,
         'Macao': 21645,
         'Singapore': 8358,
         'Hong Kong': 7140,
         'Gibraltar': 3369}

#Se le asignó a su respectivo eje x/y los datos correspondientes
pais = list(datos.keys())
densi = list(datos.values())
#Titulo del grafico
plt.title("Paises o Regiones con Mayor Densidad Poblacional (2020)")
plt.ylabel("Densidad Poblacional (P/Km2)")
plt.xlabel("Pais o Región")
plt.plot(pais, densi)
plt.show()