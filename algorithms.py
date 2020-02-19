import string


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
