def build_print(number):
    n = 1
    while n < number:
        if n < 3:
            print(f'{"1" * n}')
        else:
            print(f'{1}{" " * (n - 2)}{"1"}')
        n += 1
    print(f'{"1" * number}')


if __name__ == "__main__":
    build_print(5)
