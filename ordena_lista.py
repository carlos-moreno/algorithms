def ordena(lst: list) -> list:
    tamanho = len(lst)
    for i in range(tamanho - 1):
        menor = i
        for j in range(i + 1, tamanho):
            if lst[j] < lst[menor]:
                menor = j
        lst[i], lst[menor] = lst[menor], lst[i]
    return lst




if __name__ == "__main__":
    print(ordena([3, 2, 1]))
    print(ordena([100, -40, 0, -32, 1, 28, 50]))

