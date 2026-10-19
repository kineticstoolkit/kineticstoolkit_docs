def print_header(text):
    """Print text between length-matching separators."""
    separator = ""
    for i in text:
        separator += "-"

    print("")
    print(text)
    print(separator)
