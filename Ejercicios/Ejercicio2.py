
contador=0
nombre=""
edad=""
alumnos=dict()
nombres=list()
edades=list()

while(nombre!="0"):
    nombre=input(f"Ingrese el nombre del alumno {contador+1}, ingrese 0 para dejar de cargar alumno ")
    if(nombre=="0"):
        print("dejando de cargar ")
        break
    nombres.append(nombre)
    edad=int(input(f"Ingrese la edad de {nombre} "))
    edades.append(edad)
    contador=contador+1
    
edades_ordenadas=list(edades)
edades_ordenadas.sort(reverse=True)
nombre_ordenado=list(nombres)
edades_aux=list(edades)


for indice_edad_ordenada,eo in enumerate(edades_ordenadas):
    for indice_edad,e in enumerate(edades_aux):
        if(e==eo):
            nombre_ordenado[indice_edad_ordenada]=nombres[indice_edad]
            edades_aux[indice_edad]="aa"
            break
            

diccionario_alumno=dict()
diccionarios_alumnos=list()
          
for na,eo in zip(nombre_ordenado,edades_ordenadas):
    diccionario_alumno={
        "nombre":na,
        "edad":eo
    }
    diccionarios_alumnos.append(diccionario_alumno)

print(diccionarios_alumnos)                

print(f"El profesor alumno es {nombre_ordenado[0]}")
print(f"El alumno asistente es {nombre_ordenado[len(nombre_ordenado)-1]}")
