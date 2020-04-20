class Busca:
    def __init__(self, sequencia, elemento):
        self.sequencia = sequencia
        self.elemento = elemento

    def busca_indice_elemento(self):
        """
            Retorna o indíce do elemento caso o mesmo se encontre na lista,
            caso o elemento não seja encontrado, o retorno será -1
        """
        for k, v in enumerate(self.sequencia):
            if self.sequencia[k] == self.elemento:
                return k
        return -1

    def busca_sequencial(self):
        """
            Retorna True caso o elemento esteja na sequência, caso contrário,
            retorna False
        """
        for item in range(len(self.sequencia)):
            if self.sequencia[item] == self.elemento:
                return True
            return False

    def binary_search(self):
        primeiro = 0
        ultimo = len(self.sequencia) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if self.sequencia[meio] == self.elemento:
                return meio
            elif self.elemento < self.sequencia[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
        return -1


def binary_search_recursive(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > elemento:
        return binary_search_recursive(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return binary_search_recursive(lista, elemento, meio + 1, max)
    else:
        return meio
