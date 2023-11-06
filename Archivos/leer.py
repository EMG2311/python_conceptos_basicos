archivo_hola=open("Archivos\\Hola.txt")

#print(archivo_hola.read())

#archivo_leer=archivo_hola.read() #una vez se lee un archivo no se puede volver a leer
#lineas=archivo_hola.readlines()#me devuelve un arreglo con todas las lineas

linea1=archivo_hola.readline()
linea2=archivo_hola.readline()
linea3=archivo_hola.readline()
print(linea1)
print(linea2)
print(linea3)
#print(lineas)

