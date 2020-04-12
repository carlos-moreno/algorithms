def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
        print(meio)
    return False

def bubble_sort(lst):
    """
        Must return list sort using the bubble sort.
    """
    end = len(lst)
    for i in range(end - 1, 0, -1):
        change = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(lst)
                change = True
        if not change:
            return lst

    return lst

if __name__ == "__main__":
    print(busca(['a', 'e', 'i'], 'e'))
    print(busca([1, 2, 3, 4, 5], 6))
    print(busca([1, 2, 3, 4, 5, 6], 4))

    print(bubble_sort([5, 1, 4, 2]))
