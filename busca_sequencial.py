class Busca:
    def __init__(self, sequencia, elemento):
        self.sequencia = sequencia
        self.elemento = elemento

    def busca_indice_elemento(lista: list, elemento: object) -> int:
        """
            Retorna o indíce do elemento caso o mesmo se encontre na lista,
            caso o elemento não seja encontrado, o retorno será -1
        """
        for k, v in enumerate(lista):
            if lista[k] == elemento:
                return k
        return -1


    def busca_sequencial(seq: list, elemento: object) -> bool:
        """
            Retorna True caso o elemento esteja na sequência, caso contrário,
            retorna False
        """
        for item in range(len(seq)):
            if seq[item] == elemento:
                return True
            return False


