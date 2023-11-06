import csv
with open("Leer_Archivos_CSV\\archivo.csv") as archivo:
    reader=csv.reader(archivo) 
    for row in reader:
        print(row)