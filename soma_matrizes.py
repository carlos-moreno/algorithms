def dimensoes(matriz: list) -> str:
    return f"{len(matriz)}X{len(matriz[0])}"


def soma_matrizes(m1: list, m2: list) -> list:
    if dimensoes(m1) != dimensoes(m2):
        return False
    result = []
    for x in range(len(m1)):
        l = []
        for i_k, i_v in enumerate(m1[x]):
            for j_k, j_v in enumerate(m2[x]):
                if i_k == j_k:
                    l.append(i_v + j_v)
        result.append(l)
    return result
