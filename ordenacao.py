from random import randrange
from time import time


class Ordenacao:
    def __init__(self, size):
        self.size = size

    def bubblesort(self, lst):
        """
            Must return list sort using the bubble sort.
        """
        end = len(lst)
        for i in range(end - 1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return lst

    def bubblesort_v2(self, lst):
        """
            Must return list sort using the bubble sort.
        """
        end = len(lst)
        for i in range(end - 1, 0, -1):
            change = False
            for j in range(i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    change = True
            if not change:
                return lst

        return lst

    def direct_selection(self, lst):
        end = len(lst)

        for i in range(end - 1):
            min_position = i
            for j in range(i + 1, end):
                if lst[j] < lst[min_position]:
                    min_position = j
            lst[i], lst[min_position] = lst[min_position], lst[i]

        return lst

    def insertion_sort(self, lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i
            while j > 0 and key < lst[j - 1]:
                lst[j] = lst[j - 1]
                j -= 1
            lst[j] = key

    def list_generation(self):
        lst = [randrange(-10000, 10000) for _ in range(self.size)]
        return lst

    def list_generation_v2(self):
        lst = [x for x in range(self.size)]
        lst[self.size // 10] = randrange(len(lst))
        return lst


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
