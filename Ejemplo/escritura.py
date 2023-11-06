def leer_archivo(nombre):
    with open(f"Ejemplo\\{nombre}.txt") as archivo:
        return archivo.readLines()
    

def escribir_lineas(nombre,*mensajes):
    aux=list()
    with open(f"Ejemplo\\{nombre}.txt","a") as archivo:
        for mensaje in mensajes:
            mensaje=f"\n{mensaje}"
            aux.append(mensaje)
        archivo.writelines(aux)
        
def sobreescribir_archivo(nombre,*mensajes):
    with open(f"Ejemplo\\{nombre}.txt","w") as archivo:
        for mensaje_linea in mensajes:
            mensaje_linea=f"\n{mensaje_linea}"
            archivo.write(mensaje_linea)
