"""Solution for Quiz 3.

Author: Duan
Version: 10/13/2024
"""


def names_cap(names):
    """Find ---.

    Args:
        names (list): a list of names
    """
    for item in names:
        if str.isupper(item[0]):
            print(item)


def limit_letters(counts, limit):
    """Find the letters.

    Args:
        counts (dict): a dict of comuts
        limit (int): int value

    Returns:
        set: type for return
    """
    s = set()
    for letter in counts:
        if counts[letter] <= limit:
            s.add(letter)
    return s


if __name__ == "__main__":
    names = ["mayfield", "Sprague", "Shrestha", "wang", "Chao"]
    names_cap(names)
