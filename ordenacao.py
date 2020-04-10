class Ordenacao:
    def __init__(self, lista):
        self.lista = lista

    def bubblesort(self):
        """
            Must return list sort using the bubble sort.
        """
        fim = len(self.lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

        return self.lista


if __name__ == "__main__":
    o1 = Ordenacao([2, 3, 10, -9, 50, 1])
    print(o1.bubblesort())
    o2 = Ordenacao([-13, 2, 100, -9230, 23, 10])
    print(o2.bubblesort())
    o3 = Ordenacao([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(o3.bubblesort())
