def saludar():
    print("hola que onda")
    

def calculo(numero):
    a=numero
    b=numero+1
    return numero,a,b

numero=calculo(4)
print(numero)


def sumar(*numeros): #con el * hace que todos los parametros que pasen va a ser una lista
    for numero in numeros:
        print(numero)
        
sumar(2,5,6,7,4,3,6)

#lambda, es una funcion sin nombre, esta se puede por ejemplo almacenar en una variable
#multiplicar_por_dos=lambda numero:numero*2
#print(multiplicar_por_dos(9))



#filter
numeros_pares=list(filter(lambda numero:numero%2==0,[1,5,6,3,2,5,5])) #filter va a ejecutar la funcion para cada uno de los valores de la lista

print(numeros_pares)