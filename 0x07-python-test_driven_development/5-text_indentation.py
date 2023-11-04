#!/user/bin/python3
"""Defines a function that prints a text."""

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.
    Raises:
        TypeError: if the inputed text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    j = 0
    while j < len(text) and text[j] == ' ':
        j += 1

    while j < len(text):
        print(text[j], end="")
        if text[j] == "\n" or text[j] in ".?:":
            if text[c] in ".?:":
                print("\n")
            j += 1
            while j < len(text) and text[j] == ' ':
                j += 1
            continue
        j += 1
