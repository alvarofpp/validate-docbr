def digitsAreRepeated(string: str) -> bool:
    if string == None: raise TypeError

    string = string.strip().rstrip()

    if string == '':
        return False

    return string[0] * len(string) == string
