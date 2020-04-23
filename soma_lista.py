def soma_lista(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + soma_lista(lst[1:])
