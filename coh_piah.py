import re
from statistics import median
from operator import itemgetter


def le_assinatira():
    """
        The function reads the values of the linguistic features 
        of the model and returns a signature to be compared with
        the texts provided.
    """
    print("Welcome to the automatic COH-PIAH detector.")

    wal = float(input("Enter the average word size: "))
    ttr = float(input("Enter the Type-Token interface: "))
    hlr = float(input("Enter the Reason Hapax Legomana: "))
    sal = float(input("Enter the sentence size: "))
    sac = float(input("Enter the average sentence complexity: "))
    pal = float(input("Enter the average sentence size: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input(f"Enter text {str(i)} (press enter to exit): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f"Enter text {str(i)} (press enter to exit): ")
    return textos


def separa_sentencas(texto: str) -> list:
    """
       The function receives a text and returns a list of sentences
       within the text. 
    """
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca: str) -> list:
    """
        The function receives a sentence and returns
        a list of phrases within the sentence.
    """
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase: str) -> list:
    """
        The function receives a sentence and returns a list
        of words within the sentence.
    """
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """
        This function receives a list of words and returns the 
        number of words that appear only once.
    """
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """
        This function receives a list of words and returns the 
        number of different words used.
    """
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """
        TO IMPLEMENT. This function receives two text signatures 
        and must return the degree of similarity in the signatures.
    """
    diferenca = sum(abs(a - b) for a, b in zip(as_a, as_b))
    print(diferenca)
    print(diferenca / 6)
    return diferenca / 6


def calcula_assinatura(texto):
    """
        TO IMPLEMENT. This function receives a text and must return 
        the text signature.
    """
    return [
        calcula_tamanho_medio_palavra(texto),
        calcula_type_token(texto),
        calcula_hapax_legomana(texto),
        calcula_tamanho_medio_sentenca(texto),
        calcula_complexidade_sentenca(texto),
        calcula_tamanho_medio_frase(texto),
    ]


def avalia_textos(textos, ass_cp):
    """
        TO IMPLEMENT. This function receives a list of texts and
        an ass_cp signature and must return the number (1 to n) of
        the text most likely to have been infected with COH-PIAH.
    """
    aux = {}
    for k, v in enumerate(textos):
        ass = calcula_assinatura(v)
        aux[k + 1] = compara_assinatura(ass_cp, ass)
    aux = sorted(aux.items(), key=itemgetter(1))
    return aux[0][0]


def calcula_tamanho_medio_palavra(texto: str) -> float:
    frases = retorna_lista_frases(texto)
    palavras = []
    for frase in frases:
        palavras.extend([len(palavra) for palavra in separa_palavras(frase)])

    return sum(palavras) / len(palavras)


def calcula_type_token(texto: str) -> float:
    frases = retorna_lista_frases(texto)
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))
    return n_palavras_diferentes(palavras) / len(palavras)


def calcula_hapax_legomana(texto: str) -> float:
    frases = retorna_lista_frases(texto)
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))
    return n_palavras_diferentes(palavras) / n_palavras_unicas(palavras)


def calcula_tamanho_medio_sentenca(texto: str) -> float:
    average = []
    for item in separa_sentencas(texto):
        average.append(len(item))
    return median(average)


def calcula_complexidade_sentenca(texto: str) -> float:
    sentencas = separa_sentencas(texto)
    return len(retorna_lista_frases(texto)) / len(sentencas)


def calcula_tamanho_medio_frase(texto: str) -> float:
    tamanho_das_frases = [len(item) for item in retorna_lista_frases(texto)]
    return sum(tamanho_das_frases) / len(retorna_lista_frases(texto))


def retorna_lista_frases(texto: str) -> list:
    frases = []
    sentencas = separa_sentencas(texto)
    for item in sentencas:
        frases.extend(separa_frases(item))
    return frases


if __name__ == "__main__":
    assinatura = le_assinatira()
    textos = le_textos()
    result = avalia_textos(textos, assinatura)
    print(result)
