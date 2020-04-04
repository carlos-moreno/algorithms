def busca(lista: list, elemento: object) -> object:
    for k, v in enumerate(lista):
        if lista[k] == elemento:
            return k
    return False

