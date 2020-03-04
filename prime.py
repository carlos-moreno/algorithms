def is_prime(number: int) -> bool:
    result = False
    if number < 2:
        return result
    count = 0
    aux = number
    while aux > 0:
        if number % aux == 0:
            count += 1
        aux -= 1
    return False if count > 2 else True


def qtd_number_primes(number: int) -> int:
    count = 0
    if number < 2:
        return 0
    for v in range(2, number + 1):
        if is_prime(v):
            count += 1
    return count
