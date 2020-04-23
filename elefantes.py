def incomodam(n: int) -> str:
    if n < 1:
        return f''
    return f'incomodam ' + incomodam(n - 1)


def elefantes(n: int, aux=1) -> str:
    if aux == 1:
        return f'Um elefante incomoda muita gente\n{elefantes(n, aux + 1)}'
    if aux <= n:
        if (aux + 1) > n:
            return f'{aux} elefantes {incomodam(aux)}muito mais'
        else:
            return f'{aux} elefantes {incomodam(aux)}muito mais\n{aux} elefantes incomodam muita gente\n{elefantes(n, aux + 1)}'
