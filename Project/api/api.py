import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

# Asegúrate de instalar estos paquetes antes de ejecutar :
# pip install pandas
# pip install sodapy
# pip install matplotlib

# Credenciales de autenticación
app_token = "rSqn8HbsBYPEmB9xYmVfsQIgU"
user = "emmanuelvelezlopez@gmail.com"
clave = "cM#!8hxxf&cD+Q3"


# Autenticación con la clave de API
client = Socrata("www.datos.gov.co", app_token, user, clave)

# ID del conjunto de datos que deseas acceder
dataset_id = "ch4u-f3i5"

# Obtener datos de la API
results = client.get(dataset_id, limit=30)

# Convertir a un DataFrame de pandas
results_df = pd.DataFrame.from_records(results)

# Renombrar columnas
results_df.rename(columns={
    'ph_agua_suelo_2_5_1_0': 'ph', 
    'f_sforo_p_bray_ii_mg_kg': 'fosforo (p)', 
    'potasio_k_intercambiable_cmol_kg': 'potasio (k)'
}, inplace=True)

# Seleccionar columnas a mostrar
columns_to_display = ['departamento', 'municipio', 'cultivo', 'estado', 'tiempo_establecimiento', 'ph', 'fosforo (p)', 'potasio (k)']
results_df_subset = results_df[columns_to_display]

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 6))

# Crear tabla
tabla = plt.table(cellText=results_df_subset.values, colLabels=results_df_subset.columns, loc='center')

# Ocultar ejes
ax = plt.gca()
ax.axis('off')

# Mostrar tabla
plt.show()
