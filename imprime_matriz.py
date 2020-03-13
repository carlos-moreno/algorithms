def imprime_matriz(matriz: list) -> None:
    """
        Função que imprime a matriz em linhas e colunas

        >>> imprime_matriz([[1], [2], [3]])
        1
        2
        3
        >>> imprime_matriz([[1, 2, 3], [4, 5, 6]])
        1 2 3
        4 5 6
    """
    for linha in matriz:
        for coluna in linha:
            if coluna != linha[-1]:
                print(coluna, end=" ")
            else:
                print(coluna, end="")
        print()
