"""Review of Chapter 9: Sequences.

Author: Chris Mayfield
Version: 12/02/2024
"""


def indent_stars(text):
    """Add four spaces to lines that start with "* ".

    Args:
        text (str): Multi-line string representing notes.

    Returns:
        text: The same notes with all "*" lines indented.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("* "):
            lines[i] = "    " + line
    return "\n".join(lines) + "\n"


def unindent_stars(text):
    """Remove four spaces from lines that start with "    * ".

    Args:
        text (str): Multi-line string representing notes.

    Returns:
        text: The same notes with all "*" lines unindented.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("    * "):
            lines[i] = line[4:]
    return "\n".join(lines) + "\n"
