def mult_two(a: int, b: int) -> int:
    """Return multiply of two numbers"""
    return a * b

def best_stock(a: dict) -> str:
    """
    You are given the current stock prices. You have to find out which stocks cost more.
    Input: The dictionary where the market identifier code is a key and the value is a stock price.
    Output: The market identifier code (ticker symbol) as a string.
    """
    new_stock = sorted(a.items(), key = lambda d: (d[1], d[0]), reverse = True)
    return new_stock[0][0]
