def reverse() -> list:
    result_list = []
    number_informad = int(input("Enter a number: "))
    while number_informad != 0:
        result_list.append(number_informad)
        number_informad = int(input("Enter a number: "))

    print()
    for v in result_list[::-1]:
        print(v)


if __name__ == "__main__":
    reverse()
