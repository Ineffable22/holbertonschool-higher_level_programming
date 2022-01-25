#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    text is the text to evaluate
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for lim in ".:?":
        text = (lim + "\n\n").join(
            [line.strip(" ") for line in text.split(lim)])

    print("{}".format(text), end="")
