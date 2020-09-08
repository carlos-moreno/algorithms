def binary(num, l=[]):
    """Function to return a number decimal in binary

    >>> binary(20)
    '00010100'
    >>> binary(75)
    '01001011'

    :param num: number decimal
    """
    while num > 0:
        l.append(str(num % 2))
        num //= 2
    return ''.join(l[::-1]).zfill(8)

