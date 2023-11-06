with open("Archivos\\Hola.txt","t+w") as archivo:
    archivo.write("madre mia willy") #sobreescribe todo el archivo
    archivo.writelines("\nholis") #escribo solo una linea
    print(archivo.readlines())