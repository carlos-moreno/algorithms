def build_print(number, n):
    if n < 3:
        s = f'{"1" * n}'
    elif n > 2 and n <  number:
        s = f'{"1"}{" " * (n - 2)}{"1"}'
    else:
        s = f'{"1" * number}'
    return s

def print_(number):
    for n in range(1, number + 1):
        print(build_print(number, n))


if __name__ == "__main__":
    print_(5)
