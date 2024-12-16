def find_fraction(order):
    diagonal = 1
    while order > diagonal:
        order -= diagonal
        diagonal += 1

    if diagonal % 2 == 0:
        numerator = order
        denominator = diagonal - order + 1
    else:
        numerator = diagonal - order + 1
        denominator = order

    return f"{numerator}/{denominator}"

if __name__ == "__main__":
    order = int(input())
    print(find_fraction(order))