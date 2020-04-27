def build_print(number):
    n = 1
    while n <= number:
        if n < 3:
            print(f'{"1" * n}')
        n += 1


if __name__ == "__main__":
    print(build_print(2))
