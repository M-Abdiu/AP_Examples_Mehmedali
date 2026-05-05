def calculate_discount(price, discount, is_member):
    """Calculates discount considering membership."""
    if is_member:
        discount = discount + 0.05
    return price * (1 - discount)


def main():
    # A first developer tries this:
    price_item1 = calculate_discount(100, 20, True)
    print(price_item1)

    # Another developer thinks it's a decimal
    price_item2 = calculate_discount(100, 0.2, True)
    print(price_item2)

    # Yet another developer thinks is_member is a string
    # Check the output and argue, why this this happens
    price_item2 = calculate_discount(100, 0.2, "yes")
    print(price_item2)

    # play around and see what happens when running the code
    # and in the IDE...


if __name__ == "__main__":
    main()
