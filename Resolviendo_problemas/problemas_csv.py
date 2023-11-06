import pandas as pd


archivo=pd.read_csv("Resolviendo_problemas\\archivo.csv")
#cambiar tipo de dato de una columna a string
archivo["edad"]=archivo["edad"].astype(str)

#remplazar valores. Remplaza el nombre lucas por marcos
archivo["nombre"].replace("lucas","marcos",inplace=True)

#borrar filas donde faltan datos
archivo=archivo.dropna()

#eliminando filas repetidas
archivo=archivo.drop_duplicates()

#creando un csv con el dataframe limpio

archivo.to_csv("Resolviendo_problemas\\archivo_limpio.csv")