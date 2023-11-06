diccionario ={
    "nombre":"german",
    "apellido":"monti rubio",
    "edad":24
}

for key in diccionario: #Ese key va a mostrar la clave
    print(key)
    
    
for key in diccionario.items(): #Ese key va a mostrar la clave y el valor
    clave=key[0]
    valor=key[1]
    print(f"La clave es {clave} y tiene un valor de {valor}")