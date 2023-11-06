def encontrar_par_impar(numeros):
    par=list()
    impar=list()
    for numero in numeros:
        print(type(numero))
        if (numero%2==0):
            par.append(numero)
        else:
            impar.append(numero)
    return par,impar

def sumar_mostrar_numeros(numeros):
    suma=0
    for numero in numeros:
        suma=suma+numero
    return suma

