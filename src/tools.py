from transliterate import translit


def tr(s):
    """
    cyrillic to latin letters translation
    """
    return translit(s, reversed=True)
