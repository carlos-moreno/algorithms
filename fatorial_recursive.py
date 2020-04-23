def fatorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * fatorial(n - 1)
