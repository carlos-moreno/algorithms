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
