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


class Converter:
    def __init__(self, num):
        self.num = num
        self.lst = []

    def binary(self):
        """Function to return a number decimal in binary"""
        aux = self.num
        while aux > 0:
            self.lst.append(str(aux % 2))
            aux //= 2
        return ''.join(self.sort_list()).zfill(8)

    def sort_list(self):
        return self.lst[::-1]
