import escritura as e
#e.escribir_lineas("texto","hola","como estas?","todo bien por suerte")

e.escribir_lineas("texto","nashei","opa")

archivo=open("Ejemplo\\texto.txt")
print(archivo.readlines())
archivo.close()