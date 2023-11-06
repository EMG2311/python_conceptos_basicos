import pandas as pd
#leer el archivo (devuelve un dataframe)
archivo1=pd.read_csv(f"Leer_Archivos_CSV\\archivo.csv")#,names=["name","last_name","age"]) #el names me cambia el encabezado

archivo2=pd.read_csv(f"Leer_Archivos_CSV\\archivo.csv")

nombres=archivo1["nombre"] #si lo cambie arriba con el names pongo ese nuevo encabezado

#ordenar el dataframe por edad
ordenado_ascendentemente=archivo1.sort_values("edad")

#ordenando de forma decendente
ordenado_descendentemente=archivo1.sort_values("edad",ascending=False)


#concatenando dataframes
archivo_concatenado=pd.concat([archivo1,archivo2])

#accediendo a las primers 2 fila con head (cantidad de filas que quiero obtener)
primer_fila=archivo1.head(2)

#accediendo a las ultimas 2 filas con tail(cantidad de filas que quiero obtener)

ultimas_filas=archivo1.tail(2)

#accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales=archivo1.shape


#obteniendo data estadistica del datafram
archivo_info=archivo1.describe()

#accediendo a un elemento especidifco con loc
elemento_especifico=archivo1.loc[2,"edad"] #eccediendo al elemento de la fila 2, a la edad

#accediendo a un elemento especifico por el indice
elemento_especifico_indice=archivo1.iloc[1,2] #fila dos, columna 2}

#accediendo a todas las filas de una columna
apellidos=archivo1.iloc[:,1]

#accediendo a todas las columnas de una fila
alumno=archivo1.iloc[1,:]
print(alumno)
