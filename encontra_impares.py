def encontra_impares(lista, aux=[]):
    lista_aux = aux
    if lista:
        if lista[0] % 2 != 0:
            lista_aux.append(lista[0])
        return encontra_impares(lista[1:], lista_aux)
    else:
        return lista_aux
