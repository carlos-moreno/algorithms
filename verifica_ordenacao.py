def ordena(lst: list) -> list:
    tamanho = len(lst)
    for i in range(tamanho - 1):
        menor = i
        for j in range(i + 1, tamanho):
            if lst[j] < lst[menor]:
                menor = j
        lst[i], lst[menor] = lst[menor], lst[i]
    return lst

def ordenada(lst: list) -> bool:
    lst_comp = lst.copy()
    if lst_comp == ordena(lst):
        return True
    return False

