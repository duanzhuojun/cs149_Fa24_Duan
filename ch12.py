"""Review of Chapter 12: Recursion.

Author: Chris Mayfield
Version: 12/02/2024
"""


def search_json(data, term, expr="data"):
    """Search a json object for the given term.

    Args:
        data (any): The object to search recursively.
        term (str): The text to search for in the object.
        expr (str): Python expression of the current data.

    Returns:
        str: The value of expr if term is found, else None.
    """

    # Base case: found the search term
    if isinstance(data, str):
        if term in data:
            return expr

    # Recursive case: search the dictionary
    if isinstance(data, dict):
        for key, value in data.items():
            new_expr = f"{expr}['{key}']"
            result = search_json(value, term, new_expr)
            if result:
                return result

    # Recursive case: search the list
    if isinstance(data, list):
        for idx, value in enumerate(data):
            new_expr = f"{expr}[{idx}]"
            result = search_json(value, term, new_expr)
            if result:
                return result
