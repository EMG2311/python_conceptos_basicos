import pandas as pa
with open("c:/Users/Usuario/Desktop/Curso/Python/Warap/chat.txt", "r", encoding="utf-8") as archivo:
    miguel=0
    for mensajes in archivo.readlines():
        if "legui" in mensajes:
            miguel=miguel+1
    print(miguel)
    