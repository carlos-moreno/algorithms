def maiusculas(frase):
    """
        Retorna as letras em maiúsculo da frase.
    """
    result = []
    for letra in frase:
        if letra.isupper():
            result.append(letra)
    return ''.join(result)
