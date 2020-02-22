import string
from typing import List, Any


def mult_two(a: int, b: int) -> int:
    """Return multiply of two numbers"""
    return a * b


def best_stock(a: dict) -> str:
    """
    You are given the current stock prices. You have to find out which stocks cost more.
    Input: The dictionary where the market identifier code is a key and the value is a stock price.
    Output: The market identifier code (ticker symbol) as a string.
    """
    new_stock = sorted(a.items(), key=lambda d: (d[1], d[0]), reverse=True)
    return new_stock[0][0]


def radix(str_number, radix):
    digits = list(string.digits) + list(string.ascii_uppercase)
    summation = 0
    str_number = str_number[::-1]
    for i, x in enumerate(str_number):
        if digits.index(x) >= radix:
            return -1
        summation += digits.index(x) * pow(radix, i)
    return summation


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    l = [i for i, x in enumerate(text) if x == symbol]
    if len(l) > 1:
        return l[1]


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return [x for x in text.split()][0]


def first_word_complex(text: str) -> str:
    """
        returns the first word in a given text.
    """
    l = []
    for x in text:
        if x.isalpha() or x == "'":
            l.append(x)
        else:
            l.append(" ")
    w = "".join(l)
    result = w.split()
    return result[0]


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    result = sorted(data, key=lambda k: k["price"], reverse=True)
    return result[:limit]


def popular_words(text: str, words: list) -> dict:
    """
        Shows the number of times a given word appears in the text
    """
    text = text.lower().split()
    result = {}
    for x in text:
        if x in words:
            result[x] = result.get(x, 0) + 1
    for x in words:
        if x not in result:
            result[x] = 0
    return result


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    a_index = text.index(begin)
    b_index = text.index(end)
    return text[a_index + 1 : b_index]


def between_markers_complex(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    length_begin = len(begin)
    index_begin = text.index(begin) if begin in text else None
    index_end = text.index(end) if end in text else None
    if begin in text and end in text and index_end < index_begin:
        return ""
    elif begin in text and end in text:
        return text[index_begin + length_begin : index_end]
    elif begin in text and end not in text:
        return text[index_begin + length_begin :]
    elif begin not in text and end in text:
        return text[:index_end]
    else:
        return text


def all_the_same(elements: List[Any]) -> bool:
    """
        return True if set(list) == 0 or list is empty
    """
    return True if len(set(elements)) in [0, 1] else False


def most_frequent_letter(text: str) -> str:
    """
        Return the most frequent letter in lower case as a string.
    """
    l = []
    d = {}
    text = text.lower()
    for x in text:
        if x.isalpha() and x not in d:
            d[x] = d.get(x, 0) + 1
            l.append({"name": x, "count": text.count(x)})

    result = sorted(l, key=lambda k: (-k["count"], k["name"]))
    return result[0].get("name")


def time_converter(time: str) -> str:
    """
        Returns the converted time
    """
    result = int(time.replace(":", ""))
    if result == 0:
        hour = str(result + 1200)
        return f"{hour[:2]}:{hour[2:]} a.m."
    elif result == 1200:
        return f"{time[:2]}{time[2:]} p.m."
    elif result > 1300:
        hour = str(result - 1200)
        if len(hour) > 3:
            return f"{hour[:2]}:{hour[2:]} p.m."
        else:
            return f"{hour[:1]}:{hour[1:]} p.m."
    elif result > 1200 < 1300:
        return f"{time[:2]}{time[2:]} p.m."
    elif result < 1000 < 1200:
        return f"{time[1:2]}{time[2:]} a.m."
    else:
        return f"{time[0:2]}{time[2:]} a.m."
