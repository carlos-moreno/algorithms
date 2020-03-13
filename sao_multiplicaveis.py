def sao_multiplicaveis(m1: list, m2: list) -> bool:
    """
        Função que retorna True se as matrizes são multiplicáveis
        entre si, False caso contrário.

        >>> sao_multiplicaveis([[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]])
        False
        >>> sao_multiplicaveis([[1], [2], [3]], [[1, 2, 3]])
        True
    """
    if len(m1[0]) == len(m2):
        return True
    else:
        return False
