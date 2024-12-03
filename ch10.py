"""Review of Chapter 10: File I/O.

Author: Chris Mayfield
Version: 12/02/2024
"""


def search_file(path, term):
    """Search a file for the given term.

    Args:
        path (str): The path of the file to search.
        term (str): The text to search for in the file.

    Returns:
        int, int: The line number and column of the term,
                  or None if the term is not found.
    """
    with open(path) as file:
        for ln, line in enumerate(file):
            col = line.find(term)
            if col > -1:
                return (ln+1, col+1)


def strip_file(path):
    """Remove whitespace from the end of each line in a file.

    Args:
        path (str): Location of the file to strip whitespace.
    """
    with open(path) as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
            file.write(line.rstrip() + "\n")
