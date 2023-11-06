from itertools import groupby

def ordernar_palabras(palabras):
    lista_aux=list()
    abecedario="abcdefghijklmnñopqrstuvwxyz"
    abecedario_descendente=abecedario[::-1]
    lista_retornada=list()
    for letra in abecedario_descendente:
        for palabra in palabras:
            if letra==palabra[0]:
                lista_aux.append(palabra)
        if len(lista_aux)!=0:
            lista_retornada.append(lista_aux)
        lista_aux=list()
    return lista_retornada

print(ordernar_palabras(["avion","alambre","hola","hotel","sapo"]))

def ordenar(palabras):
    palabras.sort()
    grupos=groupby(palabras,lambda x:x[0])
    for key, group in grupos:
        print(f'Grupo {key}: {sorted(list(group), reverse=True)}')
    
print(ordenar(["hola","avion","tanque","bombas"]))
        
