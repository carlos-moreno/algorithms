import re


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
    pass


def calcula_assinatura(texto):
    """
        TO IMPLEMENT. This function receives a text and must return 
        the text signature.
    """
    pass


def avalia_textos(textos, ass_cp):
    """
        TO IMPLEMENT. This function receives a list of texts and
        an ass_cp signature and must return the number (1 to n) of
        the text most likely to have been infected with COH-PIAH.
    """
    pass
