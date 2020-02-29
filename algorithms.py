import string
from typing import List, Any
from collections.abc import Iterable
import re


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
    MIDDAY = 1200
    MIDNIGHT = 0
    THIRTEEN_HOURS = 1300
    TEN_HOURS = 1000
    result = int(time.replace(":", ""))
    if result == MIDNIGHT:
        hour = str(result + MIDDAY)
        return f"{hour[:2]}:{hour[2:]} a.m."
    elif result == MIDDAY:
        return f"{time[:2]}{time[2:]} p.m."
    elif result > THIRTEEN_HOURS:
        hour = str(result - MIDDAY)
        if len(hour) > 3:
            return f"{hour[:2]}:{hour[2:]} p.m."
        else:
            return f"{hour[:1]}:{hour[1:]} p.m."
    elif result > MIDDAY < THIRTEEN_HOURS:
        return f"{time[:2]}{time[2:]} p.m."
    elif result < TEN_HOURS:
        return f"{time[1:2]}{time[2:]} a.m."
    else:
        return f"{time[0:2]}{time[2:]} a.m."


def frequency_sort(items):
    """
        Return rating by frequency
    """
    if sorted(items) == list(set(items)):
        return items
    elif len(set([items.count(x) for x in items])) == 1:
        return sorted(items)
    else:
        return sorted(
            sorted(items, reverse=True), key=lambda k: (items.count(k)), reverse=True
        )


def chain(iterables):
    if isinstance(iterables, Iterable):
        for item in iterables:
            yield from flat_list(item)
    else:
        yield iterables


def flat_list(array):
    return list(chain(array))


def sun_angle(time):
    SIX_HOURS = "06:00"
    EIGHTEEN_HOURS = "18:00"
    if time >= SIX_HOURS and time <= EIGHTEEN_HOURS:
        if (int(time[3:]) / 4) > 0:
            return float(
                "{:.2f}".format(((int(time[:2]) * 15) - 90) + (int(time[3:]) / 4))
            )
        else:
            return (int(time[:2]) * 15) - 90
    else:
        return "I don't see the sun!"


def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    result = 0
    for item in line:
        x = len(max(re.findall(f"{item}+", line)))
        if x >= result:
            result = x
    return result


VOWELS = "aeiouy"


def translate(phrase):
    regex = re.compile(r"\W")
    result = []
    index = 0
    while index < len(phrase):
        if phrase[index].lower() in VOWELS:
            result.append(phrase[index])
            index += 3
        elif regex.findall(phrase[index]):
            result.append(phrase[index])
            index += 1
        else:
            result.append(phrase[index])
            index += 2

    return "".join(result)


VALUES = {
    "e": 1,
    "a": 1,
    "i": 1,
    "o": 1,
    "n": 1,
    "r": 1,
    "t": 1,
    "l": 1,
    "s": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10,
}


def worth_of_words(words):
    """
        Return the most valuable word.
    """
    result = {}
    for v in words:
        _sum = 0
        for it in v:
            _sum += VALUES.get(it)
        result[v] = _sum
    return sorted(result.items(), key=lambda k: (k[1]), reverse=True)[0][0]


def verify_anagrams(first_word, second_word):
    return sorted("".join(first_word.split()).lower()) == sorted(
        "".join(second_word.split()).lower()
    )


def restricted_sum(data):
    if len(data) > 1:
        data[1] = data[0] + data[1]
        data.remove(data[0])
        restricted_sum(data)
    if len(data) == 1:
        return data[0]
    if not data:
        return 0
