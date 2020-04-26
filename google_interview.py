"""
Give a number N, write a code to print all positive numbers less than N in
which all adjacent digits differ by 1

>>> number_adjacent(105)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101

>>> number_adjacent(30)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23
"""

def number_is_valid(number):
    return (
        number < 11
        or abs(int(str(number)[-2]) - int(str(number)[-1])) == 1
    )


def number_adjacent(number: int) -> str:
    l = []
    for n in range(number):
        if number_is_valid(n):
            l.append(n)
    print(", ".join(str(n) for n in l))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
