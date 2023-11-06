nombres=["german","matias","lautaro"]
apellidos=["monti","rubio","godoy"]

#registrar esta informacion en txt de forma optima
with open("Resolviendo_problemas\\nombre_y_apelldos.txt","w") as archivo:
    archivo.writelines("Los datos son:\n")
    [archivo.writelines(f"Nomre: {n}\nApellido: {a}\n----------\n") for n,a in zip(nombres,apellidos)]
    
    