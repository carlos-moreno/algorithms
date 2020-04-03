from random import randrange
def lista_grande(n: int) -> list:
    '''
        Must return one list of random numbers
    '''
    lst = [randrange(n) for _ in range(n)]
    return lst

