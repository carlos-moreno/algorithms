def menor_nome(nomes):
    result = []
    for nome in nomes:
        result.append(len(nome.strip()))
    return nomes[result.index(min(result))].strip().capitalize()
