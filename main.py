import numpy as np
from datasets import load_dataset
import pandas as pd

# Cargando el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convirtiendo el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separando el DataFrame en dos: uno con personas que perecieron (is_dead=1) y otro con el complemento (is_dead=0)
df_perecieron = df[df["is_dead"] == 1]
df_complemento = df[df["is_dead"] == 0]

# Calculando el promedio de edades en cada dataset
promedio_edad_perecieron = df_perecieron["age"].mean()
promedio_edad_complemento = df_complemento["age"].mean()

# Imprimiendo los promedios de edades
print("Promedio de edad de personas que perecieron:", promedio_edad_perecieron)
print("Promedio de edad del complemento (no perecieron):", promedio_edad_complemento)
