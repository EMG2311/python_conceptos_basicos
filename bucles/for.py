#TODOS ESTOS BUCLES FUNCIONAN PARA LISTAS, TUPLAS Y CONJUNTOS

animales=["gato","perro","loro","tortuga"]
numeros = [1,23,54,67]

for animal in animales:
    print(f"ahora la variable se llama: {animal}")
    
#para recorrer dos listas al mismo tiempo:
for animal,numero in zip(animales,numeros):
    print(f"hay {numero} de {animal}")
    #para usar esta forma las dos lsitas deb4en tener la mimsa cantidad de elementos

for num in range(5,10): #itera desde 5 a 10
    print(num)
    
for num in range(5): #itera desde 0 a 5
    print(num)

#forma correcta de recorrer una lista con indice
for num in enumerate(animales):
    print(num) #me devuelve una tupla con [indice,valor]
    
    
#for con else hace que cuando termina el programa hace lo qyue haya en el eles
for animal in animales:
    print("imprimiendo animales")
else:
    print("El bucle termino")
    