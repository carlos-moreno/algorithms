import string as st

character = st.ascii_lowercase
word_cipher = []


def cesar(word: str, order: int) -> str:
    for v in word:
        if (character.index(v.lower()) + order) < 26:
            if v.isupper():
                word_cipher.append(
                    character[character.index(v.lower()) + order].upper()
                )
            else:
                word_cipher.append(character[character.index(v) + order])
        else:
            if v.isupper():
                word_cipher.append(
                    character[(character.index(v.lower()) + order) - 26].upper()
                )
            else:
                word_cipher.append(character[(character.index(v) + order) - 26])
    return "".join(word_cipher)
