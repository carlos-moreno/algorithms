def is_hypotenuse(number: int) -> bool:
    result = False
    if number < 1:
        return result
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if pow(number, 2) == pow(i, 2) + pow(j, 2):
                result = True
                break
    return result


def soma_hipotenusas(number: int) -> int:
    hypotenuse = []
    for v in range(1, number + 1):
        if is_hypotenuse(v) and v not in hypotenuse:
            hypotenuse.append(v)
    return sum(hypotenuse)
