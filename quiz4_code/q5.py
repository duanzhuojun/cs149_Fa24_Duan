def get_positive_sum():
    """Calculate the sum of positive numbers entered by the user.

    Repeatedly prompts the user to input numbers (int) into a list until
    the user enters a negtive number, at which point it returns the sum of all positive 
    numbers.

    In the following example, get_positive_sum() is called. The user inputs
    the numbers 4, 3, and -2. The function then returns 7.

    >>> get_positive_sum()
    Enter a positive: 4
    Enter a positive: 3
    Enter a positive: -1
    7

    Returns:
        int: The sum of positive numbers.
    """
    total = 0
    while True:
        value = int(input("Enter a number: "))
        if value < 0:
            return total
        total += value

print(get_positive_sum())