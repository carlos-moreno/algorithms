vogais = ['a', 'e', 'i', 'o', 'u']

def conta_letras(frase, contar="vogais"):
    """
        Retorna o total de vogais ou consoantes, conforme parametro informado.
    """
    total_vogais = 0
    total_consoantes = 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
        if letra not in vogais and letra.isalpha():
            total_consoantes += 1
    if 'vogais' == contar:
        return total_vogais
    else:
        return total_consoantes
